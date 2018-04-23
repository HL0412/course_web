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
    def get(self, request):
        return render(request, 'course/data_download.html')
