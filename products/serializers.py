from rest_framework import serializers
from .models import product
from vendors.models import vendor
from customers.models import customer
from mongoengine import ListField, StringField

class productSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)
    createdAt = serializers.DateTimeField(read_only=True)

    deviceName = serializers.CharField(max_length=100)
    imeiOrSerialNumber = serializers.CharField(max_length=100, allow_blank=True)
    gadgetType = serializers.ChoiceField(choices=("smartphone", "laptop", "accessories"))

    vendorBusinessName = serializers.CharField(write_only=True)
    customerEmail = serializers.EmailField(write_only=True)

    configuration = serializers.CharField(max_length=100)
    vendorPrice = serializers.CharField(max_length=11)
    wranosPrice = serializers.CharField(max_length=11)

    deviceCondition = ListField(StringField(max_length=200))

    vendorName = serializers.SerializerMethodField()
    customerEmailRead = serializers.SerializerMethodField()

    def get_vendorName(self, obj):
        return obj.vendor.businessName if obj.vendor else None

    def get_customerEmailRead(self, obj):
        return obj.customer.email if obj.customer else None


    def validate_imeiOrSerialNumber(self, value):
        gadgetType = self.initial_data.get("gadgetType")

        # Accessories: IMEI optional
        if gadgetType == "accessories":

            if not value:

                return None # Accessories can have no IMEI/Serial Number

        else:

            if not value:
                raise serializers.ValidationError("IMEI/Serial Number is required")

            length = len(value)
            if gadgetType == "smartphone" and length != 15:

                raise serializers.ValidationError("Smartphone IMEI must be exactly 15 digits")

            if gadgetType == "laptop" and not (5 <= length <= 10):

                raise serializers.ValidationError("Laptop IMEI must be between 5 and 10 digits")

        if value and product.objects(imeiOrSerialNumber=value).first():

            raise serializers.ValidationError("IMEI or Serial Number already exists.")

        return value

    def validate_vendorBusinessName(self, value):
        vendors = vendor.objects(businessName=value).first()
        if not vendors:
            raise serializers.ValidationError("Vendor not found")
        return vendors

    def validate_customerEmail(self, value):
        customer_obj = customer.objects(email=value).first()
        if not customer_obj:
            raise serializers.ValidationError("Customer not found")
        return customer_obj

    def create(self, validated_data):
        vendor = validated_data.pop("vendorBusinessName")
        customer_obj = validated_data.pop("customerEmail")

        new_product = product.objects.create(
            vendor=vendor,
            customer=customer_obj,
            **validated_data
        )

        # Prevent double-counting
        if not new_product.isCounted:
            customer_obj.update(inc__completedOrders=1)
            new_product.update(set__isCounted=True)

        return new_product

    def update(self, instance, validated_data):
        # Prevent IMEI overwrite
        validated_data.pop("imeiOrSerialNumber", None)

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()
        return instance