from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationForm, CustomerChangeForm

# Register your models here.

CustomUser =  get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomerCreationForm

    form =  CustomerChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


admin.site.register(CustomUser, CustomUserAdmin)
