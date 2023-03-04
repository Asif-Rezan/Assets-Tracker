from django.urls import path
from .views import AddCompany, AddEmployee, AddDevice, AddDeviceLog, CheckDeviceLog


urlpatterns = [
     path("add-company/", AddCompany,name="add-company"),
     path("add-employee/", AddEmployee, name="add-employee"),
     path("add-device/", AddDevice, name="add-device"),
     path("add-device-log/", AddDeviceLog, name="add-device-log"),
     path("check-log/", CheckDeviceLog,name="check-device-log")
]
