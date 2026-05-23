from django.urls import path
from . import views

app_name = 'academics'

urlpatterns = [
    path('faculties/', views.faculty_list, name='faculties'),
    path('departments/', views.department_list, name='departments'),
    path('programmes/', views.programme_list, name='programmes'),
    path('courses/', views.course_list, name='courses'),
]
