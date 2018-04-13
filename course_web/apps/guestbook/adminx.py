from django.contrib import admin

# Register your models here.
import xadmin
from guestbook.models import GuestBook

class GuestBookAdmin:
    list_display = ['title', 'ID_Card', 'author', 'sex', 'checkout', 'type', 'add_time']
    search_fileds = ['title', 'ID_Card', 'author']
    list_filter = ['title', 'ID_Card', 'author']

xadmin.site.register(GuestBook, GuestBookAdmin)