from rest_framework import serializers
from myapp.models import Task
# from myapp.models import Car

# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Car
#         fields=('name', 'top_speed')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields=('TaskId', 'Text', 'Day', 'Reminder')