from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm

# import datetime
from django.http import HttpResponse, JsonResponse
# from django.urls import reverse

from django.core import serializers

from tanya_dokter.forms import ForumForm
from tanya_dokter.models import Forum


# Create your views here.
# def view_example(request):
#     my_var = {
#         'lst': [1, 2, 4],
#         'user_logged_in': True
#     }
#     return render(request, 'tanya_dokter/base.html', context=my_var)

# def create_forum(request):
#     form = ForumForm()
#     if request.method == 'POST':
#         form = ForumForm(request.POST)

#         # form.instance.user = request.user
#         form.instance.date = datetime.datetime.now()

#         if form.is_valid():
#             form.save()
#             return redirect('forum')
#             # return redirect('forum')    ngarang wey

#     else:
#         form = ForumForm()
#         return render(request, 'create-task.html', {'form': form})

def forum(request):
    post = Forum.objects.all()
    response = {'post': post}
    return render(request, 'tanya_dokter/forum.html', response)

# @login_required(login_url='/authentication/login/')
# def show_landing_page(request):
#     post = Forum.objects.all()
#     response = {'post': post}
#     return render(request, 'tanya_dokter/landing.html', response)


# @login_required(login_url='/todolist/login/')
# def show_todolist(request):
#     try:
#         user = request.user
#         data = Task.objects.filter(user=user)
#         context = {
#             'todolist': data,
#             'nama': user.username,
#             'last_login': request.COOKIES['last_login'],
#         }
#         return render(request, "todolist.html", context)
#     except KeyError:
#         return redirect('todolist:login')


@login_required(login_url='/authentication/login/')
def show_landing_page(request):
    try:
        user = request.user
        data = Forum.objects.filter(user=user)
        context = {
            'forum': data,
            'nama': user.username,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, "tanya_dokter/landing.html", context)
    except KeyError:
        return redirect('authentication:login')


@login_required(login_url='/authentication/login/')
def form_ajax(request):
    user = request.user
    data = Forum.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data),
                        content_type="application/json")


@login_required(login_url='/authentication/login/')
def show_forum(request):
    user = request.user
    data = Forum.objects.filter(user=user)
    context = {
        'forum': data,
        # 'last_login': request.COOKIES['last_login'],
    }
    return render(request, "tanya_dokter/forum.html", context)


# MASI ERROR INI, GAMAU MASUK KE IF
@login_required(login_url='/authentication/login/')
def add_question_ajax(request):
    form_class = ForumForm
    form = form_class(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    
    return render(request, 'tanya_dokter/form.html', {'tanya_dokter': form})
    #     # forums = ForumForm.objects.all()
    #     # title = request.POST.get('title')
    #     # question_text = request.POST.get('question_text')

    #     data = {}
    #     if request.is_ajax():
    #         if form.is_valid():
    #             addedTask = ForumForm.objects.create(
    #             title=form.cleaned_data['title'],
    #             question_text=form.cleaned_data['question_text'],
    #             date=datetime.datetime.now(),
    #             user=request.user,
    #         )

    #         addedTask.save()
    #     #         form.save()
    #     #         data['name'] = form.cleaned_data.get('name')
    #     #         data['status'] = 'ok'
    #     #         return JsonResponse(data)
                
    #     # context = {
    #     #     'form': form}
    #     return HttpResponse("")

    # return render(request, "tanya_dokter/forum.html")
    # return render(request, 'tanya_dokter/form.html', {'tanya_dokter': form})


# @login_required(login_url='/todolist/login/')
# def create_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)

#         form.instance.user = request.user
#         form.instance.date = datetime.datetime.now()

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("todolist:
#               show_todolist_ajax"))

#     else:
#         form = TaskForm()

#         return render(request, 'create-task.html', {'form':form})
