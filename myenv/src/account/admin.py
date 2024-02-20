from django.contrib import admin
from .models import UserModel, RegistrationModel

# Register your models here.
admin.site.register(UserModel) ## register secondary user model  in DB
admin.site.register(RegistrationModel)