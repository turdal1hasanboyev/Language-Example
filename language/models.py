from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.username


class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name
