from django.conf import settings
from django.db import models


class Member(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField()
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="added_by",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.first_name
