from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(unique=True)
    email = models.EmailField()
    first_name = models.CharField()
    last_name = models.CharField()
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Session(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    participant = models.ManyToManyField(User)

    def __str__(self):
        return self.title
