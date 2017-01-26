from django.db import models
from django.utils import timezone
from django.urls import reverse
from pygments import highlight
from pygments.lexers.textfmts import IrcLogsLexer
from pygments.formatters import HtmlFormatter

class Quote(models.Model):
    content = models.TextField()
    added_timestamp = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("render_quote", args=(self.pk,))

    def formatted(self):
        return highlight(self.content, IrcLogsLexer(), HtmlFormatter(style='colorful'))
