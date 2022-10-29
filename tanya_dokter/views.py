from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm

import datetime
from django.http import HttpResponse
# from django.urls import reverse

from django.core import serializers

# from django.views.generic import ListView, View
# from tanya_dokter.forms import ForumForm
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
#         form = ForumForm(request.
# )

#         # form.instance.user = request.user
#         form.instance.date = datetime.datetime.now()

#         if form.is_valid():
#             form.save()
#             return redirect('forum')
#             # return redirect('forum')    ngarang wey

#     else:
#         form = ForumForm()
#         return render(request, 'create-task.html', {'form': form})

# class ForumView(ListView):
#     model = Forum
#     template_name = 'tanya_dokter/form.html'
#     context_object_name = 'forum'


# class CreateForum(View):
#     @login_required(login_url='/authentication/login/')
#     def get(self, request):
#         specialization1 = request.GET.get('specialization', None)
#         title1 = request.GET.get('title', None)
#         question_text1 = request.GET.get('question_text', None)

#         obj = Forum.objects.create(
#             specialization=specialization1,
#             title=title1,
#             question_text=question_text1,
#             date=datetime.datetime.now(),
#             # user=request.user,
#         )

#         forum = {
#             # 'user': obj.user,
#             'specialization': obj.specialization,
#             'title': obj.title,
#             'question_text': obj.question_text,
#             'date': obj.date
#         }

#         data = {
#             'forum': forum
#         }
#         return JsonResponse(data)


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
    # try:
    user = request.user
    data = Forum.objects.filter(user=user)
    context = {
        'forum': data,
        'nama': user.username,
    }
    return render(request, "tanya_dokter/landing.html", context)
    # except KeyError:
    #     return redirect('authentication:login')


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
    }
    return render(request, "tanya_dokter/forum.html", context)


# MASI ERROR INI, GAMAU MASUK KE IF
@login_required(login_url='/authentication/login/')
def add_question_ajax(request):
    form = Forum.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        question = request.POST.get('question')
        specialization = request.POST.get('specialization')
      
        addedForm = Forum.objects.create(
            title=title,
            question=question,
            specialization=specialization,
            date=datetime.datetime.now(),
            user=request.user,
        )

        addedForm.save()
        return render(request, "tanya_dokter/add_forum.html",
                      {'tanya_dokter': form})
    return render(request, "tanya_dokter/add_forum.html",
                  {'tanya_dokter': form})

    # form_class = ForumForm
    # form = form_class(request.POST)

    # if request.method == 'POST':

    #     if form.is_valid():
    #         form.save()
    #         return JsonResponse({
    #             'message': 'success'
    #         })
    
    # return render(request, 'tanya_dokter/form.html', {'tanya_dokter': form})
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
