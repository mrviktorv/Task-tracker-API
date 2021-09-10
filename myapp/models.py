from django.db import models

# class Car(models.Model):
#     name = models.CharField(max_length=100)
#     top_speed = models.IntegerField()
# Create your models here.

class Task(models.Model):
    TaskId = models.AutoField(primary_key=True)
    Text = models.CharField(max_length=50)
    Day = models.CharField(max_length=200, default='DEFAULT VALUE')
    Reminder = models.BooleanField(default=False)