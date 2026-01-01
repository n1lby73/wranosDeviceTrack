from django.db import models

# Create your models here.
class vendorModel(models.Model):

    address = models.TextField()
    email = models.EmailField(unique=True)
    # vendorName = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    businessName = models.CharField(max_length=100)
    verifiedEmail = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    verifiedAddress = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)
    RCNumber = models.CharField(max_length=7, min_length=7, unique=True)
    phoneNumber = models.CharField(max_length=11, min_length=11, unique=True)


    def __str__(self):
        return str(self.RCNumber)
    # def getVendorBusinessName(self):
    #     return str(self.BusinessName)