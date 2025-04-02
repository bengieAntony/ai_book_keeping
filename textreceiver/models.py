from django.db import models

class TextInput(models.Model):
    user_id = models.CharField(max_length=100, default="default_user")
    text = models.TextField()
