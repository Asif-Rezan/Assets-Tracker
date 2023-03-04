from django.urls import path
from .views import AddCompany, AddEmployee, AddDevice


urlpatterns = [
     path("add-company/", AddCompany,name="add-company"),
     path("add-employee/", AddEmployee, name="add-employee"),
     path("add-device/", AddDevice, name="add-device"),
]
