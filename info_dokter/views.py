from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from .models import InfoDokter, ReviewDokter
from flutter_authentication.views import *
import json 
from collections import namedtuple
from django.contrib import auth
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def show_info_dokter (request):
    orang = request.user
    data_info_dokter = InfoDokter.objects.all()
    data_review = ReviewDokter.objects.filter(user= orang)
    context = {
        'list_info' : data_info_dokter,
        'list_review' : data_review,
    }
    return render (request, "info_dokter.html", context )

def add_review (request):
    if request.method == 'POST':
        task = ReviewDokter()
        task.dokter =InfoDokter.objects.filter(pk= request.POST.get('idDokter'))
        task.user = request.user
        task.review = request.POST.get('Review')
        task.save()
    return redirect('info_dokter:show_info_dokter')

@csrf_exempt
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_review_flutter (request,userId):
    if request.method == 'POST':
        task = ReviewDokter()
        task.dokter =InfoDokter.objects.filter(pk= request.POST.get('idDokter'))
        task.user = request.user
        task.review = request.POST.get('Review')
        task.save()
        return HttpResponse(b"Create", status=200)
    
def show_json(request):
    dataDokter = InfoDokter.objects.all()
    return HttpResponse(serializers.serialize("json", dataDokter), content_type="application/json")

def show_json2(request): 
    orang = request.user
    dataReview2 = ReviewDokter.objects.filter(user = orang)
    return HttpResponse(serializers.serialize("json", dataReview2), content_type="application/json")
def show_json_flutter(request, userId):
    infoDokter_objects = ReviewDokter.objects.filter(user=userId)
    return HttpResponse(serializers.serialize("json", infoDokter_objects), content_type="application/json")


