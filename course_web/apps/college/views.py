from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from college.models import Teacher, Department


class CollegeView(View):
    '''课程教学单位'''
    def get(self, request):
        # 所有教学单位
        all_departments = Department.objects.objects.all().order_by('-publish_time')
        # 所有班级
        print(all_departments)
        all_classrooms = Department.objects.objects.all().order_by('-department_id')

        # 教学单位搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            # 在name字段进行操作,做like语句的操作。i代表不区分大小写
            # or操作使用Q
            all_departments = all_departments.filter(Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords))
        # 教学单位筛选
        department_id = request.GET.get('department','')
        if department_id :
            all_departments = all_departments.filter(department_id=int(department_id ))

        # 班级筛选
        classroom_id = request.GET.get('classroom', '')
        if classroom_id:
            all_departments = all_departments.filter(id=int(classroom_id))

        # 年级筛选
        grade = request.GET.get('grade', '')
        if grade:
            all_departments = all_departments.filter(grade=grade)

        # 学习人数和课程数筛选
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_departments = all_departments.order_by("-students")
            elif sort == "courses":
                all_departments = all_departments.order_by("-course_nums")

        # 有多少个班级
        classroom_nums = all_classrooms.count()
        # 对教学单位进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 这里指从所有的教学单位中取五个出来，每页显示5个
        p = Paginator(all_departments, 2, request=request)
        department = p.page(page)

        return render(request, "department_list.html", {
            # "grade": grade,
            "all_department": department,
            "all_classrooms": all_classrooms,
            "classroom_nums": classroom_nums,
            'classroom_id': classroom_id,
            "department_id": department_id,
            'sort':sort,
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

    def get(self,request,department_id):
        current_page = 'home'
        # 根据id找到教学单位
        course_department = Department.objects.get(id=int(department_id))
        course_department.click_nums += 1
        course_department.save()

        # 反向查询到教学单位的所有班级,再根据班级查询老师，课程
        course_classroom = course_department.classroom_set.all()
        all_courses = course_classroom.course_set.all()[:4]
        all_teacher = course_classroom.teacher_set.all()[:2]
        return render(request,'college/department_detail_homepage.html',{
            'course_department':course_department,
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
        course_department = Department.objects.get(id= int(department_id))
        # 通过教学单位找到班级。内建的变量，找到指向这个字段的外键引用
        course_classroom = course_department.classroom_set.all()
        #通过班级找到课程
        all_courses = course_classroom.course_set.all()

        return render(request, 'department-detail-course.html',{

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

        return render(request, 'department_detail_desc.html',{
            'course_department': course_department,
            'current_page':current_page,
        })
class DpartmentClassrom(View):
    """
        教学单位班级页
    """
    def get (self, request, department_id):
        current_page = 'classroom'
        course_department = Department.objects.get(id=int(department_id))
        all_teacher = course_department.teacher_set.all()

        return render(request, 'department_detail_teachers.html', {
            'all_teacher': all_teacher,
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

        return render(request, 'department_detail_teachers.html',{
            'all_teacher':all_teacher,
            'course_department': course_department,
            'current_page':current_page,
        })
