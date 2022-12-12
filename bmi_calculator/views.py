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

from authentication.decorators import pasien_required, dokter_required

from django.utils.decorators import method_decorator

from .forms import Form_BMI

from flutter_authentication.views import *


import json
from collections import namedtuple

import ast


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

@login_required(login_url='/authentication/login')
# @login_required(login_url='/auth/login')
# @login_required
def show_bmi_calculator(request):
    current_user = auth.get_user(request)

    # print(request.user)
    # print(request.user.get_username)
    # print(request.user.is_pasien)
    # print(request.user.pk)

    if(not current_user.is_pasien):
        # return messages("Register sebagai pasien untuk melihat fitur ini!")
        # messages.info(request, 'Anda perlu register sebagai Pasien untuk melihat fitur ini.')
        return redirect('authentication:login')

    bmi_objects = BMI.objects.filter(user = current_user)
    form_bmi = Form_BMI()
    context = {
        'bmi_objects': bmi_objects,
        'form_bmi' : form_bmi,
    }
    
    return render(request, "bmi_calculator.html", context)

def show_json(request):
    # print("asijdoasdjka")
    current_user = auth.get_user(request)
    # current_user = request.user
    # print(current_user)
    # print(current_user.pk)
    
    # Parse JSON into an object with attributes corresponding to dict keys.
    # user_obj = json.loads(get_user_data(request), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    
    # print(request)
    # print(current_user)

    bmi_objects = BMI.objects.filter(user=current_user)
    # bmi_objects = BMI.objects.all()

    return HttpResponse(serializers.serialize("json", bmi_objects), content_type="application/json")



def show_json_flutter(request, userPK):
    # print("asijdoasdjka")
    # current_user = auth.get_user(request)
    # current_user = request.user
    # print(current_user)
    # print(current_user.pk)
    
    # Parse JSON into an object with attributes corresponding to dict keys.
    # user_obj = json.loads(get_user_data(request), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    
    # print(request)
    # print(current_user)

    bmi_objects = BMI.objects.filter(user=userPK)
    # bmi_objects = BMI.objects.all()

    return HttpResponse(serializers.serialize("json", bmi_objects), content_type="application/json")



# def get_bmi(request):
#     print("tes get bmi")
#     current_user = auth.get_user(request)
#     bmi_object = BMI.objects.filter(user=current_user).last()
    
#     print(bmi_object)
#     return bmi_object

def add_bmi(request):
    # print("tesssssssss")
    if(request.method == 'POST'):
        # print("adiojasodija")
        current_user = auth.get_user(request)
        # jenis_kelamin = request.POST.get('jenis_kelamin')
        umur = int(request.POST.get('umur'))
        tinggi = int(request.POST.get('tinggi'))
        berat = int(request.POST.get('berat'))


        date_created = datetime.datetime.now()
        meter_tinggi = tinggi / 100
        bmi_result = berat/(meter_tinggi**2)
        
        if(bmi_result < 18.5):
            deskripsi_hasil = "Underweight"
        elif(bmi_result < 25):
            deskripsi_hasil = "Normal"
        elif(bmi_result < 30):
            deskripsi_hasil = "Overweight"
        else:
            deskripsi_hasil = "Obesitas"
        
        if(umur < 19):
            deskripsi_hasil = "Tidak diketahui"
        
        # print("tesssssssss")
        

        new_bmi = BMI(user=current_user, umur=umur, tinggi=tinggi, berat=berat, date_created=date_created, bmi_result=bmi_result, deskripsi_hasil=deskripsi_hasil)
        new_bmi.save()
        
        # print("add berhasil")

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


# @login_required(login_url='/auth/login/')
@csrf_exempt
def add_bmi_flutter(request, userPK):

    print("tesssssssss")
    print(request.user.is_pasien)
    if(request.method == 'POST'):
        print("adiojasodija")
        print(request.POST)

        # ast reference : https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
        # request_data = ast.literal_eval(request.body.decode("utf-8"))
        
        # print(ast.literal_eval(.get('umur'))

        
        print(request.user.is_pasien)


        umur = int(request.POST.get('umur'))
        tinggi = int(request.POST.get('tinggi'))
        berat = int(request.POST.get('berat'))
        # print(current_user)

        print(umur)
        print(tinggi)
        print(berat)

        date_created = datetime.datetime.now()
        meter_tinggi = tinggi / 100
        bmi_result = berat/(meter_tinggi**2)
        
        if(bmi_result < 18.5):
            deskripsi_hasil = "Underweight"
        elif(bmi_result < 25):
            deskripsi_hasil = "Normal"
        elif(bmi_result < 30):
            deskripsi_hasil = "Overweight"
        else:
            deskripsi_hasil = "Obesitas"
        
        if(umur < 19):
            deskripsi_hasil = "Tidak diketahui"
        
        print("tesssssssss")



        new_bmi = BMI(user= request.user, umur=umur, tinggi=tinggi, berat=berat, date_created=date_created, bmi_result=bmi_result, deskripsi_hasil=deskripsi_hasil)
        new_bmi.save()
        
        print("add berhasil")

        return JsonResponse({
            'status': True,
            'message': 'BMI Berhasil ditambahkan!',
            # 'bmi_result' : ,

        }, status=200)


    return JsonResponse({
            'message': "BMI gagal ditambahkan."
        }, status=401)




def delete_bmi(request, id):
    if(request.method == 'GET'):
        bmi_obj = BMI.objects.get(pk=id)
        bmi_obj.delete()

        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()



@csrf_exempt
def delete_bmi_flutter(request, id):
    if(request.method == 'POST'):
        bmi_obj = BMI.objects.get(pk=id)
        bmi_obj.delete()

        return JsonResponse({
            "status" : True,
            "message": "Berhasil menghapus histori BMI!"
        }, status= 200)
    
    return JsonResponse({
            "status" : False,
            "message": "Gagal menghapus histori BMI."
        }, status = 401)



############################################################################################################################
