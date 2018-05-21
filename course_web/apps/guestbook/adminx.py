from django.contrib import admin

# Register your models here.
import xadmin
from guestbook.models import GuestBook

class GuestBookAdmin:
    list_display = ['title', 'user', 'checkout', 'type']
    search_fileds = ['title',  'user']
    list_filter = ['title',  'user']
    model_icon = 'fa fa-list'

xadmin.site.register(GuestBook, GuestBookAdmin)