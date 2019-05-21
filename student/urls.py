
from django.urls import path,include
from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$',views.StudentListView.as_view(),name='student_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^student/(?P<pk>\d+)$',views.StudentDetailView.as_view(),name='student_detail'),
    url(r'^student/new/$',views.CreateStudentView.as_view(),name='student_new'),
    url(r'^student/(?P<pk>\d+)/edit/$',views.StudentUpdateView.as_view(),name='student_edit'),
    url(r'^student/(?P<pk>\d+)/remove/$',views.DeleteStudentView.as_view(),name='student_remove'),


]