from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from .models import InfoDokter, ReviewDokter

# Create your views here.
@login_required(login_url='/authentication/login/')
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
        task.dokter =InfoDokter.objects.filter(pk= request.POST.get('Pilih Dokter'))[0]
        task.user = request.user
        task.review = request.POST.get('Review')
        task.save()
    return redirect('info_dokter:show_info_dokter')


def show_json(request):
    dataDokter = InfoDokter.objects.all()
    return HttpResponse(serializers.serialize("json", dataDokter), content_type="application/json")

def show_json2(request): 
    orang = request.user
    dataReview2 = ReviewDokter.objects.filter(user = orang)
    return HttpResponse(serializers.serialize("json", dataReview2), content_type="application/json")



