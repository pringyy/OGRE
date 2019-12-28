from django.contrib import admin
from points.models import StudentProfileInfo

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'StudentID')


admin.site.register(StudentProfileInfo,StudentProfileAdmin)
