from urllib import request
from django.shortcuts import render

from .models import BMI

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

import datetime

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from django.core import serializers


# Create your views here.


# def register(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Akun telah berhasil dibuat!')
#             return redirect('bmi_calculator:login')
    
#     context = {'form':form}
#     return render(request, 'register.html', context)



# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user) # melakukan login terlebih dahulu
#             response = HttpResponseRedirect(reverse("bmi_calculator:show_bmi_calculator")) # membuat response
#             #response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
#             return response
#         else:
#             messages.info(request, 'Username atau Password salah!')
#     context = {}
#     return render(request, 'login.html', context)



# def logout_user(request):
#     logout(request)
#     response = HttpResponseRedirect(reverse('bmi_calculator:login'))
#     #response.delete_cookie('last_login')
#     return response



############################################################################################################################


@login_required(login_url='/authentication/login/')
def show_bmi_calculator(request):
    current_user = auth.get_user(request)
    bmi_objects = BMI.objects.filter(user = current_user)
    context = {
        'bmi_objects': bmi_objects,
    }
    
    return render(request, "bmi_calculator.html", context)

def show_json(request):
    # print("asijdoasdjka")
    current_user = auth.get_user(request)
    bmi_objects = BMI.objects.filter(user=current_user)
    return HttpResponse(serializers.serialize("json", bmi_objects), content_type="application/json")

def add_bmi(request):
    if(request.method == 'POST'):
        print("adiojasodija")
        user = request.user
        jenis_kelamin = request.POST.get('jenis_kelamin')
        umur = request.POST.get('umur')
        tinggi = request.POST.get('tinggi')
        berat = request.POST.get('berat')
        date_created = datetime.datetime.now()

        new_bmi = BMI(user=user, jenis_kelamin=jenis_kelamin, umur=umur, tinggi=tinggi, berat=berat, date_created=date_created)
        new_bmi.save()

        print("add berhasil")

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_bmi(request, id):
    if(request.method == 'GET'):
        bmi_obj = BMI.objects.get(pk=id)
        bmi_obj.delete()

        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()


############################################################################################################################
