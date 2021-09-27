from django.db import models

class Task(models.Model):
    TaskId = models.AutoField(primary_key=True)
    Text = models.CharField(max_length=50)
    Day = models.CharField(max_length=200, default='DEFAULT VALUE')
    Reminder = models.BooleanField(default=False)
