from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
# from django.views.generic import CreateView,UpdateView

# from account.views import login
from .models import *

from .forms import Place_OrderForm

# Create your views here.
# @TODO: Index Page Route 
def index(request):
    return render(request, 'order/index.html')

# def order(request):
#     return render(request, 'order/order.html')

# @TODO: Order Page route 
@login_required
def order(request):
    cur_user = request.user
    form = Place_OrderForm()

    if request.method == 'POST':
        form = Place_OrderForm(request.POST)
        if form.is_valid():

            cur_price = {}

            from_location = request.POST.get('from_location')
            to_location = request.POST.get('to_location')

            price = TransportCost.objects.filter(from_location = from_location, to_location = to_location)
            # print('##########')
            # print(cur_price)
            for price in price:
                if price.to_location == to_location and price.from_location == from_location:
                    cur_price = price
                    # print('##########')
                    # print(cur_price)
            new_order = form.save(commit=False)
            new_order.user = cur_user
            new_order.price = cur_price
            new_order.save()

            messages.success(request, 'update successful!')
            return redirect('details')
  
    context = {'form':form}
    return render(request, 'order/order.html', context)


# class CreateOrderView(LoginRequiredMixin,CreateView):
#     model = Order
#     form = Place_OrderForm()

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
    

# @TODO: order details route 
@login_required
def details(request):
    orders = Order.objects.filter(user = request.user)

    return render(request, 'order/details.html',{'orders':orders})

# class OrderListView(LoginRequiredMixin,ListView):
#     model = Order
#     template_name = 'order/details.html'
#     context_object_name = 'orders'
#     ordering = ['-placed_at']


# update form before submit 

# class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
#     model = Order
#     fields = ['item_name','from_location','to_location','receipient_name', 'receipient_contact']

#     def form_valid(self, form):
#         form.instance.user.user_id = self.request.user
#         return super().form_valid(form)
    
#     def test_func(self):
#         order = self.get_object()
#         if self.request.user == order.user_id:
#             return True
#         return False


