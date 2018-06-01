import os
import time

from django.http import StreamingHttpResponse
from pure_pagination import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from college.models import Classroom
from course_manager.models import Teacher, Course, PPT, Data
from platfrom.models import Notice, WorkCommit, News


class NoticeListView(View):
    def get(self, request):
        all_notice = Notice.objects.all().order_by('-publish_time')
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_notice, 10, request=request)
        all_notice = p.page(page)
        return render(request, 'platfrom/notice_list.html', {'all_notice' : all_notice})


class NoticeDetailView(View):
    def get(self, request, notice_id):
        notice = Notice.objects.get(id=int(notice_id))
        return render(request, 'platfrom/notice_detail.html', {'notice' : notice})


class NewsListView(View):
    def get(self, request):
        all_news = News.objects.all().order_by('-publish_time')

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_news, 10, request=request)
        all_news = p.page(page)
        return render(request, 'platfrom/news_list.html', {'all_news': all_news})


class NewsDetailView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=int(news_id))
        return render(request, 'platfrom/news_detail.html', {'news': news})


class WorkListView(View):

    def get(self, request):

        all_work = WorkCommit.objects.all().order_by('-commit_time')
        students = WorkCommit.objects.all()[:10]
        grade = request.GET.get('grade', "")
        if grade:
            if grade == 'freshman':
                all_work = all_work.filter(grade=grade)
            elif grade == 'sophomore':
                all_work = all_work.filter(grade=grade)
            elif grade == 'junior':
                all_work = all_work.filter(grade=grade)
            elif grade == 'senior':
                all_work = all_work.filter(grade=grade)
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_work, 10, request=request)
        works = p.page(page)
        return render(request, 'platfrom/work_list.html', {
            'works': works,
            'grade': grade,
            'students':  students
        })


class WorkDetailView(View):
    def get(self, request, work_id):
        work = WorkCommit.objects.get(id=int(work_id))
        return render(request, 'platfrom/work_detail.html', {'work': work})

class PlatfromView(View):
    def get(self, request):
        if request.user.is_authenticated is False:
            current_page = "platfrom"
            return render(request, 'platfrom/platfrom_home.html', {'current_page': current_page})
        else:
            if request.user.is_student:
                current_page = "commitWork"
                return render(request, 'platfrom/platfrom_commitWork.html', {'current_page': current_page})
            elif request.user.is_teacher:
                current_page = "publishWork"
                return render(request, 'platfrom/platfrom_publishWork.html', {'current_page': current_page})


class CommitWorktView(View):
    def get(self, request):
        current_page = "commitWork"
        all_teacher = Teacher.objects.all()
        print(all_teacher)
        all_course = Course.objects.all()
        return render(request, 'platfrom/platfrom_commitWork.html',{'current_page':current_page, 'all_teacher': all_teacher, 'all_course': all_course})

    # def post(self, request, f):
    #     file_name = ""
    #     try:
    #         path = "media/commitWork" + time.strftime('/%Y/%m/%d/')
    #         if not os.path.exists(path):
    #             os.makedirs(path)
    #             file_name = path + f.name
    #             destination = open(file_name, 'wb+')
    #             for chunk in f.chunks():
    #                 destination.write(chunk)
    #             destination.close()
    #     except Exception as e:
    #         print(e)
    #     return file_name


class DownPPTView(View):
    def get(self, request):
        current_page = "down_ppt"
        course = request.POST.get('course')
        print(course)
        all_teacher = Teacher.objects.all()
        all_course = Course.objects.all()
        all_ppt = PPT.objects.all()
        return render(request, 'platfrom/platfrom_downPPT.html',{'current_page':current_page, 'all_teacher': all_teacher, 'all_course': all_course, 'all_ppt': all_ppt})

    def file_download(request):
        print("111111111111111")
        def file_iterator(file_name, chunk_size=512):
            with open(file_name) as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        the_file_name = "file_name.txt"
        response = StreamingHttpResponse(file_iterator(the_file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
        return response


class DownDataView(View):
    def get(self, request):
        current_page = "down_data"
        all_teacher = Teacher.objects.all()
        all_course = Course.objects.all()
        # course = request.POST.get('course')
        # all_data = Course.objects.get(name=course).data_set.all()
        # print(all_data)
        return render(request, 'platfrom/platfrom_downdata.html',
                      {'current_page': current_page, 'all_teacher': all_teacher, 'all_course': all_course,
                        })

    def post(self, request):
        current_page = "down_data"
        all_teacher = Teacher.objects.all()
        course = request.POST.get('course')
        print(course)
        all_course = Course.objects.all()
        all_data = Course.objects.get(name=course).data_set.all()
        print(all_data)
        return render(request, 'platfrom/platfrom_downdata.html',
                      {'current_page': current_page, 'all_teacher': all_teacher, 'all_course': all_course,
                       'all_data': all_data})


class PublishWorkView(View):
    def get(self, request):
        current_page = "publishWork"
        return render(request, 'platfrom/platfrom_publishWork.html',{'current_page':current_page})

class UpPPTView(View):
    def get(self, request):
        current_page = "up_ppt"
        return render(request, 'platfrom/platfrom_uploadPPT.html',{'current_page':current_page})

class UpDataView(View):
    def get(self, request):
        current_page = "up_data"
        return render(request, 'platfrom/platfrom_uploadData.html',{'current_page':current_page})

class UpVideoView(View):
    def get(self, request):
        current_page = "up_video"
        return render(request, 'platfrom/platfrom_uploadVideo.html',{'current_page':current_page})

class VideoView(View):
    def get(self, request):
        current_page = "video"
        return render(request, 'platfrom/platfrom_video.html',{'current_page':current_page})
