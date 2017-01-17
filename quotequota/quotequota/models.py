from django.db import models
from django.utils import timezone
from django.urls import reverse

class Quote(models.Model):
    content = models.TextField()
    added_timestamp = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("render_quote", args=(self.pk,))

    def as_lines(self):
        return content.strip().split("\n")
