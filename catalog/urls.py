from django.urls import path
from . import views
from django.urls import include, re_path


urlpatterns = [
    re_path(r'^$', views.ScheduleView.as_view(), name='index'),
    re_path(r'^students/$', views.StudentListView.as_view(), name='students'),
    re_path(r'^student/(?P<pk>\d+)$', views.StudentDetailView.as_view(), name='student-detail'),
    re_path(r'^teachers/$', views.TeacherListView.as_view(), name='teachers'),
    re_path(r'^teacher/(?P<pk>\d+)$', views.TeacherDetailView.as_view(), name='teacher-detail'),
    re_path(r'^groups/$', views.GroupListView.as_view(), name='groups')
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

