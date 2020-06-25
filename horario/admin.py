from django.contrib import admin

from .models import Course, Laboratory, Semester, Schedule

# Register your models here.
admin.site.register(Course)
admin.site.register(Laboratory)
admin.site.register(Semester)
admin.site.register(Schedule)
