from django.urls import pathfrom college import viewsfrom course_manager.views import CourseListView, DataDownloadView, CourseVideoView, CourseDataView, CoursePPTView, \    CourseWorkView, CourseDetailViewapp_name = 'course'       #这里一定要写urlpatterns = [    path('course_detail/', CourseDetailView.as_view(), name='course_detail'),    path('course_list/', CourseListView.as_view(), name='course_list'),    path('data_download/', DataDownloadView.as_view(), name='data_download'),    path('course_video/', CourseVideoView.as_view(), name='course_video'),    path('course_data/', CourseDataView.as_view(), name='course_data'),    path('course_PPT/', CoursePPTView.as_view(), name='course_PPT'),    path('course_work/', CourseWorkView.as_view(), name='course_work'),]