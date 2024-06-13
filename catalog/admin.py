from django.contrib import admin

# Register your models here.

from .models import Group, Student, Teacher, Time, Class, Schedule

admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Time)
admin.site.register(Class)
admin.site.register(Schedule)
# admin.site.register(TemporaryBanIp, TemporaryBanIpAdmin)
