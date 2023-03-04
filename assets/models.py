from django.db import models

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    staff = models.ForeignKey(Employee, on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    check_out_date = models.DateTimeField(null=True, blank=True)
    check_in_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.device} condition {self.condition} checked out by {self.employee} on {self.check_out_date}"

