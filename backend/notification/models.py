from django.db import models


class FCM(models.Model):
    token = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return self.token
