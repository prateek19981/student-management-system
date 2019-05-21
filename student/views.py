from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from student.models import Student
from student.forms import StudentForm
from django.urls import reverse_lazy

# Create your views here.

class AboutView(TemplateView):
	template_name='student/about.html'





class StudentListView(ListView):
	model=Student


	def get_queryset(self):
		return Student.objects.order_by('name')



class StudentDetailView(DetailView):
	model=Student
	context_object_name = 'student'



class CreateStudentView(LoginRequiredMixin,CreateView):
	login_url='/login/'
	redirect_field_name='student/student_detail.html'
	form_class=StudentForm
	model=Student




class StudentUpdateView(LoginRequiredMixin,UpdateView):
	login_url='/login/'
	redirect_field_name='student/student_detail.html'
	form_class=StudentForm
	model=Student



class DeleteStudentView(LoginRequiredMixin,DeleteView):
	model=Student
	success_url=reverse_lazy('student_list')
	

