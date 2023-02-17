from django.db import models
from django.forms import CharField

class CheckBox(models.Model):

    name = models.CharField(max_length=150)
    is_cheked = models.BooleanField(default=False)
