from django.http import HttpResponse
from django.shortcuts import  get_object_or_404, render
from employees . models import Employee

def employee_details(request, pk):
  employees = get_object_or_404(Employee, pk=pk)
  context = {
    'employees' : employees
  }
  return render(request, 'employee_details.html', context)  