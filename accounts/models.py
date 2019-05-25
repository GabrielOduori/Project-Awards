from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.CharField(max_length =200, default = '')
    phone = models.CharField(null=False,max_length  = 12)
    photo = models.ImageField(default='default.jpg',upload_to = 'profile_pictures')
    
    def __str__(self):
        return f'{self.user}'

'''
We dont have to create profiles every time a user signs up. Instead,
we are going to use django signals to get that done automatically.
'''
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user = kwargs['instance'])
        
post_save.connect(create_profile, sender=User) 