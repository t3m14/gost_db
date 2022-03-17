from django.db import models

class Gost(models.Model):
    name = models.CharField(max_length="")
    type = models.CharField(max_length="")
    number = models.CharField(max_length="")
    sphere = models.CharField(max_length="")
    keywords = models.CharField(max_length="")
    oks = models.CharField(max_length="")
    accepted_body = models.CharField(max_length="")
    accepted_date = models.CharField(max_length="")
    effective_date = models.CharField(max_length="")
