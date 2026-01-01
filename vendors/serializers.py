from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)  # MongoDB ObjectId
    address = serializers.CharField()
    createdAt = serializers.DateTimeField(read_only=True)
    personalName = serializers.CharField(max_length=100)
    businessName = serializers.CharField(max_length=100)
    phoneNumber = serializers.CharField(min_length=11, max_length=11)

    def validate_businessName(self, value):

        if Vendor.objects(businessName=value).first():

            raise serializers.ValidationError("Business name already exists.")

        return value

    def validate_phoneNumber(self, value):

        if Vendor.objects(phoneNumber=value).first():

            raise serializers.ValidationError("Phone number already exists.")

        return value

    def create(self, validated_data):

        vendor = Vendor(**validated_data)
        vendor.save()
        return vendor

    def update(self, instance, validated_data):

        for field, value in validated_data.items():

            setattr(instance, field, value)

        instance.save()
        return instance