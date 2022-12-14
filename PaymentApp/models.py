''' /PaymentApp/models.py '''

from django.db import models
from SignupApp.models import TMSUser

class TMSPayment(models.Model):
    payment_id=models.CharField(max_length=6,primary_key=True)
    tmsuser = models.ForeignKey(TMSUser, on_delete=models.CASCADE, null=True)
    amount=models.PositiveIntegerField(default=None, null=True)
    mode=models.CharField(default=None, null=True,max_length=25)


