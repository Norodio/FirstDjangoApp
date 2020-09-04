from django.urls import path

from . import views

app_name="userPage"
urlpatterns = [
    path('', views.index, name='index'),
    path('connexionPage/', views.connexionPage, name='connexionPage'),
    path('informationPage/<int:user_id>/', views.informationPage, name='informationPage')
]
