
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from track import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('insert', views.insert, name = 'insert'),
    path('insert/insert_flight1', views.insert_flight1, name = 'insert_flight1'),
    path('insert/insert_customer1', views.insert_customer1, name = 'insert_customer1'),
    path('insert/insert_flight1/error', views.error, name = 'error'),
    path('query', views.query, name = 'query'),
    ]