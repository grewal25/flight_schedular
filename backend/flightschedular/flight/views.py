from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .serializers import UserSerializer, ScheduleSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Schedule
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse('hey there!')

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class =UserSerializer

#API
# /flights/

@csrf_exempt
def flight_list(request):
    if request.method=='GET': #get method
        schedules=Schedule.objects.all() #collecting all objects
        schedule_serializer=ScheduleSerializer(schedules, many=True) #seralizing it
        return JsonResponse(schedule_serializer.data, safe=False) #sending as JSON data

    if request.method=='POST':
        schedule_data=JSONParser().parser(request)
        schedule_serializer=ScheduleSerializer(data=schedule_data)
        if schedule.serializer.is_valid():  #check
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        Schedule.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def flight_detail(request, primary_key):
    try:
        schedule=Schedule.objects.get(pk=primary_key)
    except Schedule.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #retrieve one
    if request.method=='GET':
        schedule_serializer=ScheduleSerializer(schedule)
        return JsonResponse(schedule_serializer.data)

    #update on record
    if request.method=='PUT':
        schedule_data=JSONParser().parser(request)
        schedule_serializer=ScheduleSerializer(schedule, data=schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save() #updating with save
            return JsonResponse(schedule_serializer.data)
        return JsonResponse(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete one record
    if schedule.method=='DELETE':
        Schedule.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
