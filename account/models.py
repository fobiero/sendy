from email.policy import default
import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) #user who is authenticated
    contact = models.CharField(max_length=100) #phone number
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    adress = models.CharField(max_length=100) #user street adress
    email = models.EmailField('User Email') #location of the user
    user_image = models.ImageField(upload_to='media/profile/', default='default.png') #user image optional

    # class Meta:
    #     db_table = 'UserProfile'

    def __str__(self):
        return f'{self.user.username}'
