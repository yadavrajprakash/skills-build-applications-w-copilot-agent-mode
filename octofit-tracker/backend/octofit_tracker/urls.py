"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

import os

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"http://{codespace_name}-8000.app.github.dev/"
    else:
        base_url = request.build_absolute_uri('/')
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'workouts': base_url + 'api/workouts/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
    })

urlpatterns = [
    path('', lambda request: redirect('api/', permanent=False)),
    path('api/', api_root, name='api-root'),
    path('api/activities/', ActivityViewSet.as_view({'get': 'list', 'post': 'create'}), name='activity-list'),
    path('api/activities/<int:pk>/', ActivityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='activity-detail'),
    path('api/users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('api/users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
    path('api/teams/', TeamViewSet.as_view({'get': 'list', 'post': 'create'}), name='team-list'),
    path('api/teams/<int:pk>/', TeamViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='team-detail'),
    path('api/workouts/', WorkoutViewSet.as_view({'get': 'list', 'post': 'create'}), name='workout-list'),
    path('api/workouts/<int:pk>/', WorkoutViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='workout-detail'),
    path('api/leaderboard/', LeaderboardViewSet.as_view({'get': 'list'}), name='leaderboard-list'),
    path('admin/', admin.site.urls),
]
