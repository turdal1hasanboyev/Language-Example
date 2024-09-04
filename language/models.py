from django.db import models

from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.username


class Language(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    code = models.CharField(max_length=10)
    bio = models.TextField()

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name
