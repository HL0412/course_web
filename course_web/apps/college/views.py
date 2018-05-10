from pure_pagination import Paginator, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from college.models import Teacher, Department, Classroom


class CollegeView(View):
    '''课程教学单位'''
    def get(self, request):

        # 所有班级
        all_classroom = Classroom.objects.all()

        # 所有教学单位
        all_department = Department.objects.all()
        for department in all_department:

            if department.name == 'djx':
                department.name = '电子信息与计算机工程系'
            if department.name == 'tmx':
                department.name = ' 资源勘查与土木工程系'
            if department.name == 'ysx':
                department.name = '艺术设计系'
            if department.name == 'wyx':
                department.name = '外语系'
            if department.name == 'hnx':
                department.name = '核工程与新能源技术系'
            if department.name == 'glx':
                department.name = '管理系'
            if department.name == 'jjx':
                department.name = '经济系'
            if department.name == 'zdh':
                department.name = '自动化工程系'

        # 教学单位筛选
        department_id = request.GET.get('department', '')
        if department_id:
            all_classroom = all_classroom.filter(department_id=int(department_id))

        # 年级筛选
        grade = request.GET.get('grade', "")
        if grade:
            if grade == 'freshman':
                all_classroom = all_classroom.filter(grade=grade)
            elif grade == 'sophomore':
                all_classroom = all_classroom.filter(grade=grade)
            elif grade == 'junior':
                all_classroom = all_classroom.filter(grade=grade)
            elif grade == 'senior':
                all_classroom = all_classroom.filter(grade=grade)

        # 热门教学单位班级
        hot_classroom = all_classroom.order_by('course_nums')[:10]

        # 排序筛选
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_classroom = all_classroom.order_by("-students")
            elif sort == "courses":
                all_classroom = all_classroom.order_by("-course_nums")

        classroom_num = all_classroom.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从all_department中取五个出来，每页显示5个
        p = Paginator(all_classroom, 5, request=request)
        classroom = p.page(page)



        return render(request, "college/department_list.html", {
            "all_classroom": classroom,
            "all_department": all_department,
            "classroom_num": classroom_num,
            "department_id": department_id,
            "grade": grade,
            'hot_classroom': hot_classroom,
            'sort': sort
        })

class TeacherListView(View):
    # 教师列表
    def get(self, request):
        rank = ['教授', '副教授', '讲师']
        perfessor = Teacher.objects.filter(rank=rank[0])
        associate_perfessor = Teacher.objects.filter(rank=rank[1])
        teach = Teacher.objects.filter(rank=rank[2])
        return render(request, 'college/teacher_list.html',
                      {'perfessor' : perfessor, 'associate_perfessor':associate_perfessor, 'teach':teach})


class TeacherDetailView(View):
    # 教师详情
    def get(self, request):
        return render(request, 'college/teacher_detail.html')


class MessageView(View):
    # 关于我们
    def get(self, request):

        return render(request, 'college/message.html')

class DepartmentView(View):
    # 教学单位
    def get(self, request):

        return render(request, 'college/department_list.html')

class DepartmentHomeView(View):
    '''教学单位首页'''

    def get(self, request, department_id):
        current_page = 'home'
        course_department = Department.objects.get(id=int(department_id))
        # 反向查询到教学单位的所有班级,再根据班级查询老师，课程
        all_classroom = course_department.classroom_set.all()[:4]
        all_courses = course_department.course_set.all()[:4]
        all_teacher = course_department.teacher_set.all()[:4]
        return render(request,'college/department_detail_homepage.html',{
            'course_department': course_department,
            'all_classroom': all_classroom,
            'all_courses':all_courses,
            'all_teacher':all_teacher,
            'current_page':current_page,
        })

class DepartmentCourseView(View):
    """
    教学单位课程列表页
    """
    def get(self, request, department_id):
        current_page = 'course'
        # 根据id取到教学单位
        course_department = Department.objects.get(id=int(department_id))
        all_courses = course_department.course_set.all()
        return render(request, 'college/department_detail_course.html',{
            'all_courses':all_courses,
            'course_department': course_department,
            'current_page':current_page,

        })


class DepartmentDescView(View):
    '''教学单位介绍页'''
    def get(self, request, department_id):
        current_page = 'desc'
        # 根据id取到教学单位
        course_department = Department.objects.get(id= int(department_id))

        return render(request, 'college/department_detail_desc.html',{
            'course_department': course_department,
            'current_page':current_page,
        })
class  DepartmentClassroomView(View):
    """
        教学单位班级页
    """
    def get (self, request, department_id):
        current_page = 'classroom'
        course_department = Department.objects.get(id=int(department_id))
        all_classroom = course_department.classroom_set.all()

        return render(request, 'college/department_detail_classroom.html', {
            'all_teacher': all_classroom,
            'course_department': course_department,
            'current_page': current_page,
        })
class DepartmentTeacherView(View):
    """
    班级教师页
    """
    def get(self, request, department_id):
        current_page = 'teacher'
        course_department = Department.objects.get(id=int(department_id))
        all_teacher = course_department.teacher_set.all()

        return render(request, 'college/department_detail_teachers.html',{
            'all_teacher':all_teacher,
            'course_department': course_department,
            'current_page':current_page,
        })


from django.http import HttpResponse
from .forms import UserAskForm


class AddUserAskView(View):
    """
    用户添加学习
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            # 如果保存成功,返回json字符串,后面content type是告诉浏览器返回的数据类型
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            # 如果保存失败，返回json字符串,并将form的报错信息通过msg传递到前端
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')