from django.contrib import admin
from profiles_api import models

# Register your models here.

admin.site.register(models.UserProfile)  # register our user profile model with the admin site
