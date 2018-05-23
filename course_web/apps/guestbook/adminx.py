from django.contrib import admin

# Register your models here.
import xadmin
from guestbook.models import GuestBook, Reply


class GuestBookAdmin:
    list_display = ['title', 'user', 'g_time']
    search_fileds = ['title',  'user']
    list_filter = ['title',  'user']
    model_icon = 'fa fa-list'

class ReplyAdmin:
    list_display = ['user','guestbook', 'r_time']
    search_fileds = [  'user']
    list_filter = [ 'user']
    model_icon = 'fa fa-list'


xadmin.site.register(GuestBook, GuestBookAdmin)
xadmin.site.register(Reply, ReplyAdmin)