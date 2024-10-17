

# Register your models here.
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prénom', 'email', 'sexe', 'date_naissance')
