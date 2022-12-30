from django.contrib import admin
from django.urls import path
from backendsite import views

urlpatterns = [
    path("", views.index, name="home"),
    path("copyright/", views.copyright, name="copyright"),
    path("sent/", views.sent, name="sent"),
    path("comment/", views.comment, name="comment"),
]

