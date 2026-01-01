from rest_framework import viewsets
from rest_framework.response import Response
from .models import vendor
from .serializers import vendorSerializer

class vendorViewSet(viewsets.ViewSet):

    def list(self, request):

        vendors = vendor.objects.all()
        serializer = vendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = vendorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vendor = serializer.save()
        return Response(vendorSerializer(vendor).data)
