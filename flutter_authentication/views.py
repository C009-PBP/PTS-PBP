from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required

from authentication.forms import PasienSignUpForm, DokterSignUpForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


@csrf_exempt
def register_pasien(request):
    form = PasienSignUpForm()
    
    print("Hoi")
    if request.method == "POST":
        print("tes form PASIEN")
        form = PasienSignUpForm(request.POST)
        if form.is_valid():
            # print("tes form PASIEN IS VALID")
            form.save()

            # print("tes form PASIEN SAVED")
            # messages.success(request, 'Akun telah berhasil dibuat!')
            
            return JsonResponse({
            "status": True,
            "message": "Register berhasil dilakukan!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
    
    # print("tes form PASIEN GET")
    # context = {'form':form}
    return JsonResponse({
            "status": False,
            "message": "Register gagal. Cek kembali username dan password Anda!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=401)

@csrf_exempt
def register_dokter(request):
    form = DokterSignUpForm()

    if request.method == "POST":
        # print("tes form DOKTER")
        form = DokterSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Akun telah berhasil dibuat!')
                        
            return JsonResponse({
            "status": True,
            "message": "Register berhasil dilakukan!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)

    # context = {'form':form}
    return JsonResponse({
            "status": False,
            "message": "Register gagal. Cek kembali username dan password Anda!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=401)


# @csrf_exempt
# def registerFlutter(request):
#     # TODO: IMPLEMENT REGISTER
#     if request.method == 'POST':
#         data = json.loads(request.body)

#         username = data["username"]
#         password = data["password1"]

#         newUser = UserModel.objects.create_user(
#         username = username, 
#         password = password,
#         )

#         newUser.save()
#         return JsonResponse({"status": True, "message": "Register berhasil!"}, status=200)
#     else:
#         return JsonResponse({"status": False, "message": "Register gagal."}, status=401)



@csrf_exempt
def login(request):

    if(request.method == "GET"):
        print("NYASAR")

    username = request.POST.get('username')
    password = request.POST.get('password')
        # request.POST['username'] = username
        # request.POST['password'] = password

    # print(username)
    # print(password)

    user = authenticate(username=username, password=password)
    
    print(user)

    
    if user is not None:
        if user.is_active:
            print("AKTIF")
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Login berhasil dilakukan!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            print("GA AKTIF")
            return JsonResponse({
            "status": False,
            "message": "Login gagal, akun telah dinonaktifkan."
            }, status=401)

    else:
        print("NONE")
        return JsonResponse({
        "status": False,
        "message": "Login gagal, cek username dan passwordmu!."
        }, status=401)
    


@login_required(login_url='/login/')
def get_user_data(request):
    # TODO: GET USER DATA 

    print(request.user.is_pasien)
    
    # print(request.user.is_dokter)
    if(request.user.is_authenticated):
        return JsonResponse({
            'username': str(request.user),
            'role': 'pasien' if request.user.is_pasien else 'dokter' if request.user.is_dokter else 'admin',
            'pk' : request.user.pk,
            # 'user' : request.user
        }, status=200)
        
    else:
        return JsonResponse({
            'message': "Kamu belum terautentikasi!"
        }, status=401)


@csrf_exempt
def logout(request):
    try:
        auth_logout(request)
        return JsonResponse({
                    "status": True,
                    "message": "Log out berhasil dilakukan."
                }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Logout gagal."
        }, status=401)

