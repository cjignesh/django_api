from django.shortcuts import render
from django.http import JsonResponse
from firstApp import models
# Create your views here.

def employeeView(request):
    emp = {
        'id': 123,
        'name': 'John',
        'sal': 15000
    }

    data = models.Employee.objects.all()
    response = {'employees': list(data.values('id', 'name', 'sal'))}
    return JsonResponse(response)
