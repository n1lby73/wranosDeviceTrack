# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics, status
# from rest_framework.response import Response
# from .serializers import VendorLoginSerializer
# from rest_framework.authtoken.models import Token

# class VendorLoginView(generics.GenericAPIView):
#     serializer_class = VendorLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         vendor = serializer.validated_data['vendor']  # Get the authenticated vendor
        
#         # Generate a token (if you're using token-based authentication)
#         token, created = Token.objects.get_or_create(user=vendor)
        
#         return Response({
#             'token': token.key,  # Response returns the auth token
#             'vendor_id': vendor.id,
#             'businessName': vendor.businessName,  # Return relevant vendor info
#         }, status=status.HTTP_200_OK)
# from rest_framework.views import APIView
# class VerifyPhoneView(APIView):
#     def post(self, request):
#         # Logic here to validate OTP and mark phone_verified True
#         pass

# class VerifyEmailView(APIView):
#     def get(self, request):
#         # Logic here to verify email using token
#         pass

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
