from django.db import models


# Create your models here.
class Match(models.Model):
    begin_at = models.DateTimeField(blank=False)
    name = models.TextField(blank=False, max_length=250)
    league_id = models.IntegerField(blank=False)
