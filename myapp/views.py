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
        # try:
        return JsonResponse(tasks_serializer.data, safe=False)
        # except:
        #     return JsonResponse("No entry with this ID!", safe=False)
        # if tasks_serializer.is_valid():
        #     return JsonResponse(tasks_serializer.data, safe=False)
        # else: 
        #     return JsonResponse("Failed to Add", safe=False)
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






# ------------------------Get all tasks----------------------------
# @csrf_exempt
# def taskApi(request,id=0):
#     if request.method=='GET':
#         tasks = Task.objects.all()
#         response = []
#         for x in tasks:
#             response.append(json.dumps([{'TaskId': x.TaskId, 'Text': x.Text, 'Day': x.Day, 'Reminder' : x.Reminder}]))
#         return HttpResponse(response, content_type='text/json')

    # -------------------Crud per 1 task ------------------------------

#     if request.method == 'POST':
#             payload = json.loads(request.body)
#             # TaskId = payload['TaskId']
#             text = payload['Text']
#             day = payload['Day']
#             reminder = payload['Reminder']
#             task = Task(Text=text, Day=day, Reminder=reminder)
#             try:
#                 task.save()
#                 response = json.dumps([{ 'Success': 'Task added successfully!'}])
#             except:
#                 response = json.dumps([{ 'Error': 'Task could not be added!'}])
#     return HttpResponse(response, content_type='text/json')

# @csrf_exempt
# def taskOneApi(request, TaskId):
#     if request.method=='GET':
#         x = Task.objects.get(TaskId=TaskId)
#         response = json.dumps([{'TaskId': x.TaskId, 'Text': x.Text, 'Day': x.Day}])
#         return HttpResponse(response, content_type='text/json')

#  ----------------------------------------------------------------
# from myapp.models import Car
# from myapp.serializers import CarSerializer

# def index(request):
#     if request.method == 'GET':
#         cars = Car.objects.all()
#         response=CarSerializer(cars, many=True)
#         return JsonResponse(response.data, safe=False)
      

# def get_car(request, car_name):
#     if request.method == 'GET':
#         try:
#             car = Car.objects.get(name=car_name)
#             response = json.dumps([{ 'Car': car.name, 'Top Speed': car.top_speed}])
#         except:
#             response = json.dumps([{ 'Error': 'No car with that name'}])
#     return HttpResponse(response, content_type='text/json')

# @csrf_exempt
# def add_car(request):
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         car_name = payload['car_name']
#         top_speed = payload['top_speed']
#         car = Car(name=car_name, top_speed=top_speed)
#         try:
#             car.save()
#             response = json.dumps([{ 'Success': 'Car added successfully!'}])
#         except:
#             response = json.dumps([{ 'Error': 'Car could not be added!'}])
#     return HttpResponse(response, content_type='text/json')