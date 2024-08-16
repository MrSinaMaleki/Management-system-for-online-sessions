from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    # class Meta:
    #     verbose_name = "User"
    #     ordering = ['-date_joined']

    def __str__(self):
        return f"username: {self.username}"


class Session(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(User, related_name="sessions")

    # class Meta:
    #     verbose_name = "Session"
    #     # ordering = ['-start_time']

    def __str__(self):
        return f"title: {self.title}"
