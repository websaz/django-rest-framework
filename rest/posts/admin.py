from django.contrib import admin
from .models import Posts
# Register your models here.

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    '''Admin View for Posts'''

    list_display = ('title','date')
    list_filter = ('author','date')

    search_fields = ('title','content')
   