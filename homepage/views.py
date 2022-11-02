from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from homepage.models import Review

def show_review(request):
    review_objects = Review.objects.all()
    context = {
        'review_objects': review_objects,
    }
    
    return render(request, "index.html", context)

def show_json(request):
    review_objects = Review.objects.all()
    return HttpResponse(serializers.serialize("json", review_objects), content_type="application/json")


def add_review(request):
    if(request.method == 'POST'):
        print("abcaaaaaaaaaaaaaaaaaaaaaaaa")

        current_user = auth.get_user(request)
        username = current_user.get_username()
        review = request.POST.get('review')
        date_created = datetime.datetime.now()
        
        print("tesssssssss")
        
        new_review = Review(user=current_user,username=username, date_created=date_created, review=review)
        new_review.save()
        
        print("abc")

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_review(request, id):
    if(request.method == 'GET'):
        review_obj = Review.objects.get(pk=id)
        review_obj.delete() 
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()
