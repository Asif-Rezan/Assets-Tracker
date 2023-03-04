from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import DeviceLog


class DeviceLogSerilizer(ModelSerializer):
    class Meta:
        model= DeviceLog
        fields = "__all__"