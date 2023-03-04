from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from .models import Company, Employee, Device


#Sign Up as a company
@api_view(['POST'])
def AddCompany(request):
    name = request.POST.get("name")
    address = request.POST.get("address")
    email = request.POST.get("email")
    password = request.POST.get("password")
   
    hashed_password = make_password(password)

    company = Company(
        name=name,
        address=address,
        email=email,
        password = hashed_password
    )
    company.save()

    return Response("Company added successfully")




# Add employees for the company
@api_view(['POST'])
def AddEmployee(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    company= request.POST.get("company")

    company_instanse = Company.objects.get(id=company)


    employee = Employee(
        name=name,
        email = email,
        company = company_instanse,
    )
    employee.save()

    return Response("Employee added successfully")




@api_view(['POST'])
def AddDevice(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    company = request.POST.get("company")
    staff = request.POST.get("staff")

    company_instanse = Company.objects.get(id = company)
    staff_instanse = Employee.objects.get(id = staff)

    device = Device(
        name = name,
        description = description,
        company = company_instanse,
        staff = staff_instanse
    )

    device.save()

    return Response("Device added successfully")
