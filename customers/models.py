from mongoengine import Document, StringField, EmailField, BooleanField, DateTimeField, IntField
from datetime import datetime

class customer(Document):

    meta = {

        'dbAlias': 'default',
        'collection': 'customers'
    }

    address = StringField(required=True)
    completedOrders = IntField(default=0)
    name = StringField(required=True, max_length=100)
    createdAt = DateTimeField(default=datetime.utcnow)
    email = EmailField(required=True, max_length=100, unique=True)
    phoneNumber = StringField(required=True, unique=True, min_length=11, max_length=11)
    

    def __str__(self):
        return str(self.email)