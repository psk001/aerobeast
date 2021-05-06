from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'user_designation', ] # new
    fieldsets = UserAdmin.fieldsets + ( 
                                        (None, {'fields': ('user_designation',)}),
                                      )
    add_fieldsets = UserAdmin.add_fieldsets + (
                                                (None, {'fields': ('user_designation',)}),
                                              )
    
admin.site.register(CustomUser, CustomUserAdmin)