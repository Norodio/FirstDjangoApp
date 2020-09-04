from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import User


def index(request):
    all_users = User.objects.all()[:5]
    context = {
        'all_users': all_users,
    }
    return render(request, 'userPage/index.html', context)


def connexionPage(request):
    return HttpResponse("You're at the connexion page")

def informationPage(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request,"userPage/informationPage.html",{"user":user})
