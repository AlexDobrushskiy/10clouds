from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import string
import random
from django.conf import settings
# Create your models here.

LETTERS_AND_DIGITS = string.letters + string.digits


def generate_shortened_url_path(max_length):
    result = []
    for i in range(max_length):
        result.append(random.choice(LETTERS_AND_DIGITS))
    return ''.join(result)


class URLStorageManager(models.Manager):
    def get_or_create_by_url(self, url):
        qs = self.filter(url=url)
        if qs:
            return qs.first()
        postfix = generate_shortened_url_path(settings.SHORT_URL_MAX_LEN)
        user_cnt = User.objects.count()
        user = User.objects.all()[random.randint(0, user_cnt-1)]
        return self.create(url=url, shortened_postfix=postfix, user=user)


class URLStorage(models.Model):
    objects = URLStorageManager()

    url = models.URLField(unique=True)
    shortened_postfix = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User)
