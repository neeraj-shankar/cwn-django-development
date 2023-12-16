from django.shortcuts import render
from utils.logger import setup_logger
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from function_based.models import Employee

# Create your views here.

log = setup_logger(__name__)


@csrf_exempt
def create_employee(request):
    if request.method == "POST":
        log.info(f"The payload received: ")
        log.info(request.body)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        salary = request.POST.get("salary")
        hire_date = request.POST.get("hire_date")

        # Storing in the dictionary just for logging
        received_data = {
            "name": f"{first_name} {last_name}",
            "email": email,
            "salary": salary,
            "hire_date": hire_date,
        }
        log.info(f"Received Data --> {received_data}")

        with transaction.atomic():
            try:
                employee_detail = Employee.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    salary=salary,
                    hire_date=hire_date,
                )
            except Exception as ex:
                transaction.set_rollback(True)
                log.error(f"Error Ocurred: {str(ex)}")
                response_data = {"message": str(ex)}
        transaction.commit()

        log.info(f"{response_data}")

        return JsonResponse(response_data)

@csrf_exempt
def delete_employee(request):
    pass
