from pyexpat import model
from django.conf import settings
from django.db import models


class Books(models.Model):
    key = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    cover_i = models.IntegerField()

    added_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="added_by_user",
        blank=True,
        null=True,
    )


class Collections(models.Model):
    book_id = models.ForeignKey(
        Books,
        on_delete=models.SET_NULL,
        related_name="book_id",
        blank=True,
        null=True,
    )
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="user_id",
        blank=True,
        null=True,
    )
