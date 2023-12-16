from django.db import models

STATUS_CHOICES = (
    ("ACTIVE", "ACTIVE"),
    ("RESIGNED", "RESIGNED"),
    ("TERMINATED", "TERMINATED"),
)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # max_digits determines the maximum number of digits that can be stored, including both the integer and fractional parts.
    # decimal_places specifies the number of decimal places to store. max value --> "999999.99"
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField() # YYYY-MM-DD

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        indexes = [
            models.Index(
                fields=["first_name", "last_name", "email"], name="employee_idx"
            )
        ]


class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    employees = models.ManyToManyField(Employee, related_name="departments")


class Position(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


class Payroll(models.Model):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="payroll"
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2)
    # Other payroll-related fields


class TimeSheet(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="timesheets"
    )
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)


class Leave(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="leave_requests"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # Other leave-related fields
