from rest_framework import viewsets, filters
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'email', 'id']

class TeamViewSet(viewsets.ModelViewSet):
    """API endpoint for teams."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']

class WorkoutViewSet(viewsets.ModelViewSet):
    """API endpoint for workouts."""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'difficulty']
    ordering_fields = ['name', 'difficulty', 'id']

class ActivityViewSet(viewsets.ModelViewSet):
    """API endpoint for activities."""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__name', 'workout__name']
    ordering_fields = ['date', 'duration_minutes', 'calories_burned', 'id']

class LeaderboardViewSet(viewsets.ModelViewSet):
    """API endpoint for leaderboard."""
    queryset = Leaderboard.objects.all().order_by('-total_points')
    serializer_class = LeaderboardSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['total_points', 'rank', 'id']
