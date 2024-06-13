from django.db import models
import uuid
from django.urls import reverse
from django.contrib import admin

class Group(models.Model):
    number = models.CharField(max_length=12, help_text="Введите номер группы (например, 4443-100301D)")

    def __str__(self):
        return self.number

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])


    def __str__(self):

        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)


class Teacher(models.Model):
    # number_teacher = models.IntegerField(help_text="Введите порядковый номер преподавателя", null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)

    def get_absolute_url(self):
        return reverse('teacher-detail', args=[str(self.id)])


    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)


class Time(models.Model):
    number_pair = models.IntegerField(help_text="Введите порядковый номер занятия (например, 1)")
    start_pair = models.TimeField(auto_now=False, auto_now_add=False)
    end_pair = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return (f'{self.start_pair}-{self.end_pair}')

class Class(models.Model):
    number_class = models.CharField(max_length=12, help_text="Введите номер аудитории")

    def __str__(self):
        return self.number_class

class Schedule(models.Model):
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    class_number = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)
    number_pair = models.ForeignKey('Time', on_delete=models.SET_NULL, null=True)
    discipline = models.CharField(max_length=100, help_text='Введите название предмета')
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.group} {self.date}'

# class TemporaryBanIp(models.Model):
#     class Meta:
#         db_table = "TemporaryBanIp"
#
#     ip_address = models.GenericIPAddressField("IP адрес")
#     attempts = models.IntegerField("Неудачных попыток", default=0)
#     time_unblock = models.DateTimeField("Время разблокировки", blank=True)
#     status = models.BooleanField("Статус блокировки", default=False)
#
#     def __str__(self):
#         return self.ip_address
#
#
# class TemporaryBanIpAdmin(admin.ModelAdmin):
#     list_display = ('ip_address', 'status', 'attempts', 'time_unblock')
#     search_fields = ('ip_address',)