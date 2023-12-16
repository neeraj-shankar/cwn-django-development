from django.urls import path
from function_based import views

urlpatterns = [
    path('employee-list/', views.employee_list, name='function_based__employee-list'),
    path('employee_update/<int:emp_id>/', views.employee_update, name='function_based__employee-update'),
    path('employee_create/', views.employee_create, name='function_based__employee-create'),
    path('employee_delete/<int:emp_id>/', views.employee_delete, name='function_based__employee-delete'),
]