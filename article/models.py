from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    data_time = models.DateField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-data_time']

