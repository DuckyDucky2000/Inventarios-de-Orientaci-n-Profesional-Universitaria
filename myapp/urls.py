from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name ="hello"),
    path('projects/', views.projects, name="projects"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_tasks, name="create_task"),
    path('create_projects/', views.create_project, name="create_projects"),
    path('formtest', views.formtest, name="forms")
]