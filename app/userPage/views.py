from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate
from django.urls import reverse
from django.views.generic import UpdateView, ListView

from django.contrib.auth.models import User
import re


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

def update(request,user_id):
    user = get_object_or_404(User,pk=user_id)

    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not EMAIL_REGEX.match(request.POST['email']):
        raise Exception ('email do not match regex')
    try:
        user.email = request.POST['email']
        user.save()
    except Exception as e:
        raise e
    return HttpResponseRedirect(reverse('userPage:informationPage', args=(user.id,)))
