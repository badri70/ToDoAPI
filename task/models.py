from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=250, verbose_name="Title")
    memo = models.TextField(blank=True, verbose_name="Memo")
    created_date = models.DateField(auto_now_add=True, verbose_name="Date of creation")
    date_complete = models.DateField(null=True, blank=True)
    important = models.BooleanField(default=False, verbose_name="Important?")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")

    def __str__(self):
        return f"{self.title}-{self.user}"

