from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    lastedit = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to="media", null=True, blank=True, default='media/body.png')

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-lastedit']
