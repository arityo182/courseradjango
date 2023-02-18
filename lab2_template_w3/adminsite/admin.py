from django.contrib import admin
from .models import Course, Instructor, Lesson

# Customize Admin Size
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']

class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)


