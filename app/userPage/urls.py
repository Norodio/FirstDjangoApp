from django.urls import path

from . import views

app_name="userPage"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.connexionPage, name='connexionPage'),
    path('informationPage/<int:user_id>/', views.informationPage, name='informationPage'),
    path('connect/', views.connect, name='connect'),
    path('update/<int:user_id>/',views.update,name='update')
]
