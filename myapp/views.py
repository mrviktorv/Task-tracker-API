# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

import json

from myapp.models import Task
from myapp.serializers import TaskSerializer

@csrf_exempt
def taskApi(request,id=0):
    if request.method=='GET':
        tasks = Task.objects.all()
        tasks_serializer=TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
    elif request.method=='POST':
        task_data=JSONParser().parse(request)
        tasks_serializer=TaskSerializer(data=task_data)
        if tasks_serializer.is_valid():
            tasks_serializer.save()
            return JsonResponse(tasks_serializer.data, safe=False)
        else: 
            # tasks_serializer.errors
            # print(tasks_serializer.errors)
            return JsonResponse("Failed to Add", safe=False)



@csrf_exempt
def taskOneApi(request, TaskId):
    if request.method=='GET':
        tasks = Task.objects.get(TaskId=TaskId)
        tasks_serializer=TaskSerializer(tasks, many=False)
        return JsonResponse(tasks_serializer.data, safe=False)
    elif request.method=='PUT':
        task_data=JSONParser().parse(request)
        tasks=Task.objects.get(TaskId=task_data['TaskId'])
        tasks_serializer=TaskSerializer(tasks, data=task_data)
        if tasks_serializer.is_valid():
            tasks_serializer.save()
            return JsonResponse(tasks_serializer.data, safe=False)
        else: 
            tasks_serializer.errors
            print(tasks_serializer.errors)
            return JsonResponse("Failed to Add", safe=False)
    elif request.method=='DELETE':
        tasks=Task.objects.get(TaskId=TaskId)
        tasks.delete()
        return JsonResponse("Deleted successfully!", safe=False)






