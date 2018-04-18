from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse

def login_user(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponsePermanentRedirect(reverse('index'))
        else:
            messages.error(request, "WRONG USERNAME OR PASSWORD!")
    return render(request, 'accounts/login.html', {})
