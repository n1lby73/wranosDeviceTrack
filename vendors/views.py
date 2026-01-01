from rest_framework import viewsets
from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorSerializer

class vendorViewSet(viewsets.ViewSet):

    def list(self, request):

        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = VendorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vendor = serializer.save()
        return Response(VendorSerializer(vendor).data)
