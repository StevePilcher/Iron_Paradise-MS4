from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Forum(models.Model):
    name = models.CharField(max_length=50, unique=True, default=True)
    description = models.CharField(max_length=80)

    def __str__(self):
        return str(self.name)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    Forum = models.ForeignKey(Forum, related_name='topics', on_delete=models.CASCADE)
    originator = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.subject)


class Messages(models.Model):
    message = models.TextField(max_length=1000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.message)
