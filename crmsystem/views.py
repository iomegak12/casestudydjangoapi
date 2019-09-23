from rest_framework_mongoengine import viewsets as meviewsets

from crmsystem.models import Customer
from crmsystem.serializers import CustomerSerializer


class CustomersView(meviewsets.ModelViewSet):
    lookup_field = 'customerId'
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
