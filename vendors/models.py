# vendors/models.py
from mongoengine import Document, StringField, EmailField, BooleanField, DateTimeField, IntField
from datetime import datetime

class Vendor(Document):

    meta = {

        'dbAlias': 'vendorDB',
        'collection': 'vendors'
    }

    address = StringField(required=True)
    verifiedEmail = BooleanField(default=False)
    verifiedAddress = BooleanField(default=False)
    email = EmailField(required=True, unique=True)
    createdAt = DateTimeField(default=datetime.utcnow)
    password = StringField(required=True, max_length=128)
    businessName = StringField(required=True, max_length=100)
    otp = IntField(min_value=100000, max_value=999999, required=False, null=True)
    RCNumber = StringField(required=True, unique=True, min_length=7, max_length=7)
    phoneNumber = StringField(required=True, unique=True, min_length=11, max_length=11)

    def __str__(self):
        return str(self.RCNumber)
    # def getVendorBusinessName(self):
    #     return str(self.BusinessName)