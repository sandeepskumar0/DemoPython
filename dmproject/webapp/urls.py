from django.urls import path
from webapp import views

urlpatterns = [

    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about')



]
