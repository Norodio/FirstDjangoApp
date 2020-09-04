from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate
from django.urls import reverse

from django.contrib.auth.models import User


def index(request):
    all_users = User.objects.all()[:5]
    context = {
        'all_users': all_users,
    }
    return render(request, 'userPage/index.html', context)


def connexionPage(request):
    user = authenticate(username='Thomas', password='mdp')
    if user is not None:
        print("ok")
    else:
        print("not ok")
    return render(request,"userPage/connexionPage.html")

def informationPage(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request,"userPage/informationPage.html",{"user":user})


def connect(request):

    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        try:
            connected_user = get_object_or_404(User,username=request.POST['username'])
        except (KeyError, User.DoesNotExist):
            return HttpResponseRedirect(reverse('userPage:connexionPage'))
        else:
            return HttpResponseRedirect(reverse('userPage:informationPage', args=(connected_user.id,)))
    else:
        return HttpResponseRedirect(reverse('userPage:connexionPage'))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
