from django.db import models
from django.utils import timezone

class Quote(models.Model):
    content = models.TextField()
    added_timestamp = models.DateTimeField(default=timezone.now)
