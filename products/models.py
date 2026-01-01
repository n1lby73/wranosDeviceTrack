from mongoengine import Document, StringField, ReferenceField, DateTimeField, IntField, BooleanField, ListField
from datetime import datetime
from vendors.models import vendor
from customers.models import customer

class product(Document):

    meta = {

        'dbAlias': 'default',
        'collection': 'products',
        "indexes": [
            "imeiOrSerialNumber",
            "deviceName",
            "vendor",
            "customer",
            "createdAt",
        ]
    }

    isCounted = BooleanField(default=False)
    deviceName = StringField(required=True, max_length=100)
    imeiOrSerialNumber = StringField(unique=True, allow_blank=True, sparse=True)
    vendor = ReferenceField(vendor, required=True, reverse_delete_rule=3)
    customer = ReferenceField(customer, null=True, reverse_delete_rule=3)
    configuration = StringField(max_length=100)
    vendorPrice = IntField(required=True)
    wranosPrice = IntField(required=True)
    deviceCondition = ListField(StringField(max_length=200))
    createdAt = DateTimeField(default=datetime.utcnow)
    gadgetType = StringField(required=True, choices=("smartphone", "laptop", "accessories"))
    

    def __str__(self):
        return f"{self.deviceName} - {self.imeiOrSerialNumber}"
