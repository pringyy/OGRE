from django.contrib import admin
from points.models import StudentProfileInfo, Avatars

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'StudentID')

class AvatarsAdmin(admin.ModelAdmin):
	list_display = ('avatar', 'pointsCost', 'avatarID')  

admin.site.register(StudentProfileInfo,StudentProfileAdmin)
admin.site.register(Avatars,AvatarsAdmin)

