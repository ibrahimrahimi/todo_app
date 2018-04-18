from django.shortcuts import render, redirect

from .models import Task
from .forms import SignInForm


def index(request):
    tasks = Task.objects.order_by('-due_date')
    context = {'tasks' : tasks}
    return render(request, 'todo/index.html', context)

def sign(request):

    if request.method=='POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            new_user = SignInForm(name=request.POST['user_name'],
                                email=request.POST['user_email'],
                                password = request.POST['user_password']
                                )
            new_user.save() 
            return redirect('home')
    else:
        form = SignInForm()

    context = {'form' :  form}
    return render(request, 'todo/signup.html', context)


def home(request):
    return render(request, 'todo/home.html' )

def add_task(request):
    return render(request, 'In near future this capibility would be add to this app.' )