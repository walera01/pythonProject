from django.db import models
from django.urls import reverse


class Regis(models.Model):
    name = models.EmailField()
    password = models.CharField(max_length=256)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('form', kwargs={'form_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

