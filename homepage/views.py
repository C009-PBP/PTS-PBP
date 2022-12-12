from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from .models import Review
from flutter_authentication.views import *
import json 
from collections import namedtuple
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.contrib import auth
from django.contrib.auth import authenticate, login
from urllib import request
from django.shortcuts import render
import datetime

def show_review(request):
    review_objects = Review.objects.all()
    context = {
        'review_objects': review_objects,
    }
    
    return render(request, "index.html", context)

def show_json(request):
    review_objects = Review.objects.all()
    return HttpResponse(serializers.serialize("json", review_objects), content_type="application/json")

def show_json_flutter(request, userPK):
    review_objects = Review.objects.all()
    return HttpResponse(serializers.serialize("json", review_objects), content_type="application/json")

@login_required(login_url='/authentication/login/')
def add_review(request):
    if(request.method == 'POST'):
        # print("abcaaaaaaaaaaaaaaaaaaaaaaaa")

        current_user = auth.get_user(request)
        username = current_user.get_username()
        review = request.POST.get('review')
        date_created = datetime.datetime.now()
        
        # print("tesssssssss")
        
        new_review = Review(user=current_user,username=username, date_created=date_created, review=review)
        new_review.save()
        


        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

# @login_required(login_url='/authentication/login/')
@csrf_exempt
def add_review_flutter(request):
    if(request.method == 'POST'):

        # current_user = auth.get_user(request)
        username = request.user.get_username()
        review = request.POST.get('review')
        date_created = datetime.datetime.now()
        
        print("tesssssssss")
        
        new_review = Review(user=request.user,username=username, date_created=date_created, review=review)
        new_review.save()

        print("abcaaaaaaaaaaaaaaaaaaaaaaaa")
        


        return JsonResponse({
            'status': True,
            'message': 'BMI Berhasil ditambahkan!',
            # 'bmi_result' : ,

        }, status=200)

    return JsonResponse({
            'status': False,
            'message': 'BMI gagal ditambahkan!',
            # 'bmi_result' : ,

        }, status=200)


    
@login_required(login_url='/authentication/login/')
def delete_review(request, id):
    if(request.method == 'GET'):
        review_obj = Review.objects.get(pk=id)
        review_obj.delete() 
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

# @login_required(login_url='/authentication/login/')
@csrf_exempt
def delete_review_flutter(request, id):
    if(request.method == 'POST'):
        review_obj = Review.objects.get(pk=id)
        review_obj.delete() 
        return JsonResponse({
            'status': True,
            'message': 'Review berhasil dihapus!',

        }, status=200)
    return JsonResponse({
            'status': False,
            'message': 'Review gagal dihapus!',

        }, status=200)
