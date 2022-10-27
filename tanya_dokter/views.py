from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm

# import datetime
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,
# HttpResponseBadRequest
# from django.urls import reverse

# from django.core import serializers

from tanya_dokter.forms import ForumForm

import datetime


# Create your views here.
# def view_example(request):
#     my_var = {
#         'lst': [1, 2, 4],
#         'user_logged_in': True
#     }
#     return render(request, 'tanya_dokter/base.html', context=my_var)

def create_forum(request):
    form = ForumForm()
    if request.method == 'POST':
        form = ForumForm(request.POST)

        # form.instance.user = request.user
        form.instance.date = datetime.datetime.now()

        if form.is_valid():
            form.save()
            return redirect('forum')
            # return redirect('forum')    ngarang wey

    else:
        form = ForumForm()

        return render(request, 'create-task.html', {'form': form})
