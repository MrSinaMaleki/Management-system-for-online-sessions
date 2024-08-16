from django.contrib import admin
from online_classes import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Session)

