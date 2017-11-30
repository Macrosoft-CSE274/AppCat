from django.contrib import admin
from accounts.models import UserProfile, ApplicationEntry

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ApplicationEntry)