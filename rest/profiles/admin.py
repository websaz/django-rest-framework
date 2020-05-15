from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('phone_number','first_name','last_name')
    search_fields = ('phone_number','first_name','last_name')


admin.site.register(Profiles, ProfileAdmin)
