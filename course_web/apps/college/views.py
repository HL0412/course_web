from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from college.models import Teacher
from course_manager.models import Course


class TeacherListView(View):
    # 课程列表
    def get(self, request):
        rank = ['教授', '副教授', '讲师']
        perfessor = Teacher.objects.filter(teacher_rank=rank[0])
        associate_perfessor = Teacher.objects.filter(teacher_rank=rank[1])
        teach = Teacher.objects.filter(teacher_rank=rank[2])
        return render(request, 'college/teacher_list.html',
                      {'perfessor' : perfessor, 'associate_perfessor':associate_perfessor, 'teach':teach})


class TeacherDetailView(View):
    def get(self, request):
        return render(request, 'college/teacher_detail.html')


class MessageView(View):
    # 关于我们信息
    def get(self, request):

        return render(request, 'college/message.html')

