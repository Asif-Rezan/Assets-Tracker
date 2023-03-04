from django.urls import path
from .views import AddCompany


urlpatterns = [
     path("add-company/", AddCompany,name="add-company"),
]
