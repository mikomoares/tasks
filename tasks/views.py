from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.serializer import TaskSerializer
from tasks.models import Task
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_tasks(request):
    if request.method == 'GET':
        serializer = TaskSerializer(Task.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def post_task(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def delete_tasks(request):
    if request.method == 'DELETE':
        task = Task.objects.all().delete()
        return HttpResponse("Tasks deletada") 