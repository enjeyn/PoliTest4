from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=150, blank=True,)
    birth_date = models.DateField(blank=True,)
    sex = models.CharField(max_length=10, blank=True, )
    region = models.CharField(max_length=50, blank=True,)
    ideology = models.CharField(max_length=150, blank=True, )
    religion = models.CharField(max_length=150, blank=True, )
    avatar = models.ImageField(blank=True, upload_to='static/uploads')
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name


class WallPost(models.Model):
    receiver = models.ForeignKey(UserProfile)
    sender = models.ForeignKey(UserProfile, related_name="sender")

    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.body[:20]

