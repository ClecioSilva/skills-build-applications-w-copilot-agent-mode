
from django.contrib import admin
from .models import Team, UserProfile, Activity, Leaderboard, Workout

admin.site.register(Team)
admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
