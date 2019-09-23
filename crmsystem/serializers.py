from crmsystem.models import Customer
from rest_framework_mongoengine import serializers


class CustomerSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
