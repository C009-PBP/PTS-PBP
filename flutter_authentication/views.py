from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required


@csrf_exempt
def registerFlutter(request):
    # TODO: IMPLEMENT REGISTER

    return 

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
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
    if(request.user.is_authenticated):
        return JsonResponse({
            'username': request.user,
            'role': 'pasien' if request.user.is_pasien else 'dokter' if request.user.is_dokter else 'admin',
            'pk' : request.user.pk
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

