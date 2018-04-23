from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from platfrom.models import Notice, WorkCommit


class NoticeListView(View):
    def get(self, request):
        all_notices = Notice.objiect.all().order_by('-publish_time')
        return render(request, 'index.html', {'notices' : all_notices})



class WorkListView(View):
    def get(self, request):
        all_work = WorkCommit.objects.all()
        return render(request, 'platfrom/work_list.html', {'work': all_work})
