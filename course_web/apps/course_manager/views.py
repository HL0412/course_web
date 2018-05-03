from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from course_manager.models import Course


class CourseListView(View):
    # 课程列表
    def get(self, request):
        course_name = request.GET.get('course_name')
        courses = Course.objects.filter(course_name = course_name)
        return render(request, 'course/course_list.html', {'courses' : courses})



class DataDownloadView(View):
    #资料下载
    def get(self, request):
        return render(request, 'course/data_download.html')


class CourseVideoView(View):
    #课程视屏
    def get(self, request):
        return render(request, 'course/course_video.html')


class CourseDataView(View):
    #课程资料
    def get(self, request):
        return render(request, 'course/course_data.html')


class CoursePPTView(View):
    #课件
    def get(self, request):
        return render(request, 'course/course_PPT.html')


class CourseWorkView(View):
    #课程作业
    def get(self, request):
        return render(request, 'course/course_work.html')