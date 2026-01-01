from rest_framework import viewsets
from rest_framework.response import Response
from .models import customer
from .serializers import customerSerializer

class customerViewSet(viewsets.ViewSet):

    def list(self, request):

        customers = customer.objects.all()
        serializer = customerSerializer(customers, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = customerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.save()
        return Response(customerSerializer(customer).data)