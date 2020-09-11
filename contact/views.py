from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as lgn, logout as lgt, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

@login_required(login_url='login')
def home(request):
    logo = Logo.objects.last()
    personal_info = PersonalInfo.objects.last()
    context = {
        'logo': logo, 'personal_info': personal_info
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def contact(request):
    logo = Logo.objects.last()
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            messages.success(request, 'Спасибо !, Успешно отправлено, можно отправить еще раз')
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('contact')

    context = {
        'logo': logo, 'form': form
    }
    return render(request, 'contact.html', context)

@login_required(login_url='login')
def my_apps(request):
    logo = Logo.objects.last()
    task = Task.objects.order_by('-id').filter(user=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(task, 50)

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    context = {
        'logo': logo, 'task': task, 'tasks': tasks
    }
    return render(request, 'my_apps.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            lgn(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Something get wrong')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    lgt(request)
    return redirect('home')