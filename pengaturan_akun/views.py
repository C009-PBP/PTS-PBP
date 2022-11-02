from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from pengaturan_akun.models import Profile
import datetime
from django.urls import reverse

# Create your views here.

@login_required(login_url='/authentication/login')
def show_profile(request):
    username = request.user.username
    profile_form = EditProfile(instance=request.user.profile)
    context = {
    'username': username,
    'profile_form': profile_form,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/authentication/login')
def show_profile_json(request):
    profile = Profile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", profile), content_type="application/json")

@login_required(login_url='/authentication/login')
def update_profile_ajax(request, pk):
    if request.method == "POST":
        user_profile = Profile.objects.get(pk=pk)
        form = EditProfile(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            user_profile.first_name = form.cleaned_data['first_name']
            user_profile.last_name = form.cleaned_data['last_name']
            user_profile.phone_no = form.cleaned_data['phone_no']
            user_profile.email = form.cleaned_data['email']
            user_profile.birth_date = form.cleaned_data['birth_date']
            user_profile.gender = form.cleaned_data['gender']
            user_profile.street = form.cleaned_data['street']
            user_profile.city = form.cleaned_data['city']
            user_profile.province = form.cleaned_data['province']
            user_profile.profile_pic = form.cleaned_data['profile_pic']
            user_profile.save()
        return JsonResponse({"message": "Validation Failed"})

    return JsonResponse({"message": "Wrong Request"})