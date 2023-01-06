from stikers import views

from django.urls import path


urlpatterns = [

    path('', views.stiker),
    path('info/', views.info),

    ]