from django.urls import path
from .views import AddCompany, AddEmployee


urlpatterns = [
     path("add-company/", AddCompany,name="add-company"),
     path("add-employee/", AddEmployee, name="add-employee"),
]
