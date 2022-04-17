
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
    path('',views.index, name='index'),
    path('order/',views.order, name='order'),
    path('details/',views.details, name='details'),
    # change view 
    # path('details/',OrderListView.as_view(), name='details'),
    # path('order/',CreateOrderView.order, name='order'),


]
