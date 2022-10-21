from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    lastedit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-lastedit']
