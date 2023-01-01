from django.urls import path
from demoapp import views

urlpatterns = [

    path('', views.demo, name='demo'),
    #path('operation/', views.operation, name='operation'),


]
