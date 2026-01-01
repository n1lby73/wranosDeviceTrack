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


# class vendorRegSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(write_only=True)

#     class Meta:

#         model = vendorModel
#         fields = ('address', 'email', 'password', 'businessName', 'phoneNumber', 'RCNumber', 'verifiedAddress', 'verifiedEmail')

#         def validateEmail(self, value):

#             if User.objects.filter(email=value.lower()).exists():

#                 raise serializers.ValidationError("Email already exists.")

#             return value.lower()

#         def validateBusinessName(self, value):

#             if User.objects.filter(businessName=value.lower()).exists():

#                 raise serializers.ValidationError("Business name already exists.")

#             return value.lower()

#         def validatePhoneNumber(self, value):

#             if User.objects.filter(phoneNumber=value).exists():

#                 raise serializers.ValidationError("Phone number already exists.")

#             return value

#         def validateRCNumber(self, value):

#             if vendorModel.objects.filter(RCNumber=value).exists():

#                 raise serializers.ValidationError("Registration number already exists.")

#             return value

        
#         def create(self, validatedData):

#             vendor = vendorModel(
#                 address=validatedData['address'],
#                 email=validatedData['email'],
#                 businessName=validatedData['businessName'],
#                 phoneNumber=validatedData['phoneNumber'],
#                 RCNumber=validatedData['RCNumber'],
#                 verifiedAddress=validatedData['verifiedAddress'],
#                 verifiedEmail=validatedData['verifiedEmail']
#             )

#             vendor.set_password(validatedData['password'])
#             vendor.save()
#             return vendor



# class VendorLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         # Extract values directly
#         email = data['email'].lower()
#         password = data['password']

#         # Find vendor by email
#         vendor = Vendor.objects(email=email).first()
#         if vendor is None:
#             raise serializers.ValidationError("Invalid email or password.")

#         # Check password hash
#         if not check_password(password, vendor.password):
#             raise serializers.ValidationError("Invalid email or password.")

#         # Attach vendor to validated data
#         data['vendor'] = vendor
#         return data
