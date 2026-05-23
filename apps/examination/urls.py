from django.urls import path
from . import views

app_name = 'examination'

urlpatterns = [
    path('timetable/', views.exam_timetable, name='timetable'),
    path('clearance/', views.exam_clearance, name='clearance'),
]
