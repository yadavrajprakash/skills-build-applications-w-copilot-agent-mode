from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body workout', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration_minutes=30, calories_burned=200)
        self.leaderboard = Leaderboard.objects.create(user=self.user, total_points=100, rank=1)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Marvel')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Spider-Man')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Pushups')

    def test_activity_str(self):
        self.assertIn('Spider-Man', str(self.activity))

    def test_leaderboard_str(self):
        self.assertIn('Spider-Man', str(self.leaderboard))
