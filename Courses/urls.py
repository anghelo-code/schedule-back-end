from django.urls import path
from . import views

urlpatterns = [
  path('courses/<int:id_careers>', views.Courses_v),
  path('careers/', views.Careers_v),
  path('createTables/', views.CreateTable, name='createTables'),
]