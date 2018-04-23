from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from course_manager.models import Course


class GuestbookView(View):
    def get(self, request):
        return render(request, 'guestbook/guestbook.html')
