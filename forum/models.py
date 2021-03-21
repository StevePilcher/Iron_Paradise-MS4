from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile


# Create your models here.
class Forum(models.Model):
    name = models.CharField(max_length=50, unique=True, default=True)
    description = models.CharField(max_length=80)

    def __str__(self):
        return str(self.name)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    forum = models.ForeignKey(Forum, related_name='topics', on_delete=models.CASCADE)
    originator = models.ForeignKey(UserProfile, related_name='topics', on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.subject)


class Posts(models.Model):
    message = models.TextField(max_length=500)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(UserProfile, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(UserProfile, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.message)
