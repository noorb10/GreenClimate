from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=200, null=True, default='') 
    profile_pic = models.ImageField(default="pfp.png",blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     #blank=True means; allowed to create profile without a user attached to it
#     name = models.CharField(max_length=200, null=True, default='')
#     # email = models.CharField(max_length=200, null=True)
#     email = models.EmailField(max_length=200, null=True)
#     # email = models.OneToOneField(User, max_length=200, on_delete=models.CASCADE, related_name='email')
#     profile_pic = models.ImageField(default="pfp.png",blank=True, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         if self.user:
#             return self.user.username
#         else:
#             return str(self.id)