from mongoengine import Document, StringField, EmailField, BooleanField, DateTimeField, IntField
from datetime import datetime

class vendor(Document):

    meta = {

        'dbAlias': 'default',
        'collection': 'vendors'
    }

    address = StringField(required=True)
    createdAt = DateTimeField(default=datetime.utcnow)
    personalName = StringField(required=True, max_length=100)
    businessName = StringField(required=True, max_length=100, unique=True)
    phoneNumber = StringField(required=True, unique=True, min_length=11, max_length=11)

    def __str__(self):
        return str(self.businessName)