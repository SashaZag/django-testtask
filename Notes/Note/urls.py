from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_all, name='view_all'),
    path('add', views.add_new, name='add_new'),
]