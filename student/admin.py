from django.contrib import admin
from student.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
	list_display=('id','name','rollno','course','year','address')
	list_display_links=('id','name')
	search_fields=('name','rollno','course','year','address')
	list_per_page=25

admin.site.register(Student,StudentAdmin)
