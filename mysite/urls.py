from django.urls import path
from . import views

urlpatterns = [
    #path('',views.login,name='Login'),
    path('',views.index,name='Home'),
    path('about', views.about,name='about'),
    path('img4',views.img4,name='img4'),

]
