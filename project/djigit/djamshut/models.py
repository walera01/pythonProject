from django.db import models
from django.urls import reverse


class Regis(models.Model):
    name = models.EmailField()
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('form', kwargs={'form_id': self.pk})

