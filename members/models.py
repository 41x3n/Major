from django.db import models


class Member(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
