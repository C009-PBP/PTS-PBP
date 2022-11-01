from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import HttpResponseRedirect, reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from tanya_dokter.models import Question, Answer, Comment
from django.core.paginator import Paginator
from .forms import AnswerForm, QuestionForm
from django.core import serializers
from django.db.models import Count


@login_required(login_url='/authentication/login/')
def show_landing_page(request):
    try:
        user = request.user
        context = {
            'nama': user.username,  # user.username atau user.user HAYO
        }
        return render(request, "tanya_dokter/forum.html", context)

    except KeyError:
        return redirect('authentication:login')


@login_required(login_url='/authentication/login/')
def show_forum(request):
    user = request.user
    data = Question.objects.filter(user=user)
    context = {
        'forum': data,
    }
    return render(request, "tanya_dokter/forum.html", context)


def form_ajax(request, id):
    quest = Question.objects.get(pk=id)
    data = Answer.objects.filter(question=quest)
    return HttpResponse(serializers.serialize("json", data),
                        content_type="application/json")


# Home Page Tanya Dokter
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        quests = Question.objects.annotate(total_comments=Count('answer__comment')).filter(title__icontains=q).order_by('-id')

    else:
        quests = Question.objects.annotate(total_comments=Count('answer__comment')).all().order_by('-id')

    paginator = Paginator(quests, 3)
    page_num = request.GET.get('page', 1)
    quests = paginator.page(page_num)
    return render(request, 'tanya_dokter/forum.html', {'quests': quests})


# detail question
def show_detail(request, id):
    quest = Question.objects.get(pk=id)
    tags = quest.tags.split(',')
    answers = Answer.objects.filter(question=quest)
    answerform = AnswerForm

    if request.method == "POST":
        answerData = AnswerForm(request.POST)

        if answerData.is_valid():
            answer = answerData.save(commit=False)
            answer.question = quest
            answer.user = request.user
            answer.save()

    context = {
        'quest': quest,
        'tags': tags,
        'answers': answers,
        'answerform': answerform
    }
    return render(request, "tanya_dokter/detail.html", context)


# save comment
def save_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        answerid = request.POST['answerid']
        answer = Answer.objects.get(pk=answerid)
        user = request.user
        Comment.objects.create(
            answer=answer,
            comment=comment,
            user=user
        )
        return JsonResponse({'bool': True})


# Ask Form
def ask_form(request):
    form = QuestionForm
    if request.method == 'POST':
        questForm = QuestionForm(request.POST)

        if questForm.is_valid():
            questForm = questForm.save(commit=False)
            questForm.user = request.user
            questForm.save()
            return HttpResponseRedirect(reverse("tanya_dokter:home"))

    return render(request, 'tanya_dokter/ask-question.html', {'form': form})
