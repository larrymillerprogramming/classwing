"""classwing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newpost", views.newpost, name="newpost"),
    path("newmaterial", views.newmaterial, name="newmaterial"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("following", views.following, name="following"),

    # API paths
    path("alllikes", views.alllikes, name="alllikes"),
    path("alllikes/<int:id>", views.likeid, name="likeid"),
    path("follows", views.follows, name="follows"),
    path("follows/<int:id>", views.followid, name="followid"),
    path("postsapi", views.postsapi, name="postsapi"),
    path("postsapi/<int:id>", views.postsapiid, name="postsapiid")    
]
