from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admina'),
    path('', views.index, name='home'),
    path('a', views.a, name='a'),
    path('base', views.contact, name='contact'),
    path('table', views.table, name='table'),
    path('create', views.create, name='create'),
]
