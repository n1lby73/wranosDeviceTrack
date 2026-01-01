from rest_framework import serializers
from .models import customer

class customerSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)  # MongoDB ObjectId
    address = serializers.CharField()
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    completedOrders = serializers.IntegerField(default=0)
    createdAt = serializers.DateTimeField(read_only=True)
    phoneNumber = serializers.CharField(min_length=11, max_length=11)

    def validate_email(self, value):   

        if customer.objects(email=value).first():

            raise serializers.ValidationError("Email already exists.")

        return value

    def validate_phoneNumber(self, value):

        if customer.objects(phoneNumber=value).first():

            raise serializers.ValidationError("Phone number already exists.")

        return value
    
    def create(self, validated_data):

        customers = customer(**validated_data)
        customers.save()
        return customers

    def update(self, instance, validated_data):

        for field, value in validated_data.items():

            setattr(instance, field, value)

        instance.save()
        return instance