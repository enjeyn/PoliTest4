from django.contrib import admin
from person.models import UserProfile, WallPost

admin.site.register(UserProfile)
from .models import UserProfile, WallPost


admin.site.register(WallPost)
