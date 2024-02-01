from django.contrib import admin
from django.urls import include, path
from . import views
from customUser import views as user_views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomLoginView

urlpatterns = [
    path('dashboard/', views.dashboard, name="participant_dashboard"),
    path('leaderboard', views.leaderboard, name='participant_leaderboard'),
    path('result', views.result, name='participant_result'),
    path('connect', views.connect, name='participant_connect'),


    path('login/', CustomLoginView.as_view(template_name='customUser/login.html',), name='participant_login'),

]

# Add this pattern to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)