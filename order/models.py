
from django.db import models
from django.contrib.auth.models import User

class TransportCost(models.Model):
    from_location = models.CharField(max_length=100) 
    to_location = models.CharField(max_length=100) 
    cost = models.IntegerField()

    class Meta:
        db_table = 'Orders'

    def __str__(self):
        return self.to_location

class Order(models.Model):
    LOCATION_CHOICES = (('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Nakuru', 'Nakuru'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100) 

    from_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    to_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)

    receipient_name = models.CharField(max_length=100)
    receipient_contact = models.IntegerField() #Contact
    placed_at = models.DateField(auto_now=True) #date when item was shipped
    order_status = models.CharField(max_length=100, default='on_transit') # on transit, pending or delived.

    price = models.ForeignKey(TransportCost,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.item_name


# calculate distance 

