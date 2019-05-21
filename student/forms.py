from django import forms
from student.models import Student



class StudentForm(forms.ModelForm):

	class Meta():
		model=Student
		fields=('name','rollno','course','year','address','phonenumber','photo')
		widgets={'name':forms.TextInput(attrs={'class':' textinputclass'})}