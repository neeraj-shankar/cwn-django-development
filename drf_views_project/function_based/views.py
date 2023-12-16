from django.shortcuts import render
from rest_framework.response import Response
from function_based.models import Employee
from function_based.serializer import EmployeeSerializer
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from utils.logger import setup_logger
import json


log = setup_logger(__name__)
# Create your views here.


def employee_list(request):
    employee_queryset = Employee.objects.all()
    serializer = EmployeeSerializer(employee_queryset, many=True)

    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@csrf_exempt
def employee_create(request):
    if request.method == "POST":
        byte_data_from_request = request.body
        log.info(f"Actual Payload: {byte_data_from_request}")
        payload_str = byte_data_from_request.decode('utf-8')
        log.info(f"Str data: {payload_str}")
        python_dict_data = json.loads(payload_str)
        log.info(f"The dictionary data: {python_dict_data}")
        serializer = EmployeeSerializer(data=request.body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)


def employee_update(request, emp_id):
    log.info(f"The payload received --> {request.body}")
    try:
        employee_queryset = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        error_message = {"message": "The requested Employee does not exist."}
        return JsonResponse(error_message, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = EmployeeSerializer(employee_queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def employee_delete(request, emp_id):

    try:
        employee_queryset = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        error_message = {"message": "The requested Employee does not exist."}
        return JsonResponse(error_message, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        employee_queryset.delete()
        success_message = {"message": "The requested Employee deleted from database."}
        return JsonResponse(success_message, status= status.HTTP_410_GONE)
        
