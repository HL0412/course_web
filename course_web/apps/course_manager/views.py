from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from course_manager.models import Course
class CourseListView(View):

    # 课程列表
    def get(self, request):
        coursees = Course.objects.all().order_by('-add_time'),
        teachers = Course.objects.all()
