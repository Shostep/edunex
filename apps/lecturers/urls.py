from django.urls import path
from . import views

app_name = 'lecturers'

urlpatterns = [
    path('', views.lecturer_dashboard, name='dashboard'),
    path('courses/', views.my_courses, name='courses'),
    path('attendance/<int:course_id>/', views.mark_attendance, name='attendance'),
    path('ca/<int:course_id>/', views.enter_ca_scores, name='ca_entry'),
    path('exam/<int:course_id>/', views.enter_exam_scores, name='exam_entry'),
    path('performance/<int:course_id>/', views.class_performance, name='performance'),
    path('submit-results/<int:course_id>/', views.submit_results, name='submit_results'),
]
