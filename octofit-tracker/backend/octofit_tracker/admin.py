from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team')
    search_fields = ('name', 'email')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty')
    search_fields = ('name',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout', 'date', 'duration_minutes', 'calories_burned')
    list_filter = ('user', 'workout', 'date')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points', 'rank')
    search_fields = ('user__name',)
