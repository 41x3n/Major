from pyexpat import model
from django.conf import settings
from django.db import models


class Member(models.Model):
    key = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length = 150)
    year = models.IntegerField()
    cover_i = models.IntegerField()
	
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="added_by",
        blank=True,
        null=True,
    )