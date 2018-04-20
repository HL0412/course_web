from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from platfrom.models import Notice


class NoticeListView(View):
    def get(self, request):
        all_notices = Notice.objiect.all().order_by('-publish_time')
        return render(request, 'index.html', {'notices' : all_notices})
