from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

import datetime

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from django.core import serializers

from .forms import PasienSignUpForm, DokterSignUpForm

from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def register(request):
    form = UserCreationForm()
    
    context = {'form':form}
    return render(request, 'register.html', context)

def register_pasien(request):
    form = PasienSignUpForm()

    if request.method == "POST":
        print("tes form PASIEN")
        form = PasienSignUpForm(request.POST)
        if form.is_valid():
            print("tes form PASIEN IS VALID")
            form.save()

            print("tes form PASIEN SAVED")
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('authentication:login')
    
    print("tes form PASIEN GET")
    context = {'form':form}
    return render(request, 'register_pasien.html', context)


def register_dokter(request):
    form = DokterSignUpForm()

    if request.method == "POST":
        print("tes form DOKTER")
        form = DokterSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('authentication:login')
    
    context = {'form':form}
    return render(request, 'register_dokter.html', context)



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("homepage:index")) # membuat response
            #response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)



def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('homepage:index'))
    #response.delete_cookie('last_login')
    return response
