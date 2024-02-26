from django.db import models
from django.contrib.auth.models import User


class PageVisit(models.Model):
    user_id = models.IntegerField(null=True)
    page_id = models.IntegerField(null=True)
    start_time = models.DateTimeField(null=True)
    stop_time = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.user_id} visited page {self.page_id} at {self.start_time}"
