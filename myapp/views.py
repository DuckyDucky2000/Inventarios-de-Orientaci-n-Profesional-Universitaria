from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task, Test, Dato
from .forms import CreateNewTask, CreateNewProject, FormTest


# Create your views here.
def index(request):
    title = 'Patito'
    return render(request, 'index.html', {
        'titulo': title
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    username = 'Patito'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    #tasks = list(Project.objects.values())
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_tasks(request):  
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask
        })
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2
        )
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_projects.html', {
        'form': CreateNewProject()
    })
    else:
        Project.objects.create(
            name=request.POST["name"]
        )
        return redirect('projects')

def formtest(request):
    if request.method == 'GET':
        return render(request, 'testform.html', {
        'form': FormTest()
    })
    else:
        Test.objects.create(
            num1=request.POST["num1"],
            num2=request.POST["num2"],
            num3=request.POST["num3"]
        )
        return redirect('forms')

def datos(request):
    datos = Dato.objects.all()
    return render(request, '.html', {
        'datos': datos
    })