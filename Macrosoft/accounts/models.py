from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Comment(models.Model):
    authorName = models.CharField(max_length=100, default="default")
    content = models.CharField(max_length=300, default="This app seems good. no error detected.")
    appName = models.CharField(max_length=30, default="")

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class ApplicationEntry(models.Model):
    name = models.CharField(max_length=30, default='default')
    developer = models.CharField(max_length=30, default='default')
    platform = models.CharField(max_length=30, default='default')
    versions = models.CharField(max_length=30, default='default')
    rating = models.CharField(max_length=30, default='default')

class ApplicationAddRequest(models.Model):
    name = models.CharField(max_length=30, default="default")
    approved = models.BooleanField(default=False)
    developer = models.CharField(max_length=30, default='default')
    platform = models.CharField(max_length=30, default='default')
    versions = models.CharField(max_length=30, default='default')
    price = models.FloatField()
    feedback = models.CharField(max_length=300, default= "I am sorry that your application is not approved.")


    





