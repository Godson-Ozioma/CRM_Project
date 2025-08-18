from django.db import models

class Lead(models.Model):
    created_by = models.ForeignKey()
