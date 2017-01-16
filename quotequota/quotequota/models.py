from django.db import models
from django.utils import timezone
from django.urls import reverse

class Quote(models.Model):
    content = models.TextField()
    added_timestamp = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("render-quote", args=(self.pk,))
