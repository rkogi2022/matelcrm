from django.db import models
from django.utils import timezone
from inventory.models import Stock

# Create your models here.
class Prospects(models.Model):
    name=models.CharField(max_length=150)
    phoneno=models.PositiveIntegerField(default=None)
    idno=models.PositiveIntegerField(default=None)
    krapin=models.CharField(max_length=150)
    pobox= models.CharField(max_length=150, default='NONE')

    def __str__(self):
        return f"{self.name}"
    

class Business(models.Model):
    transmissiontype=[
        ('AUTOMATIC ', 'Automatic'),
        ('MANUAL ', 'Manual'),
    ]
    fueltype=[
        ('PETROL ', 'Petrol'),
        ('DIESEL ', 'Diesel'),
    ]
    name=models.ForeignKey(Prospects,null=True, on_delete=models.CASCADE)
    cardetails=models.ForeignKey(Stock,null=True, on_delete=models.CASCADE)
    regno= models.CharField(max_length=150)
    engine= models.CharField(max_length=150,default='1190CC')
    fuel= models.CharField(max_length=20,choices=fueltype, default='Petrol')
    transmission= models.CharField(max_length=20,choices=transmissiontype, default='Automatic')
    quantity= models.PositiveIntegerField(default=1)
    invamt=models.PositiveIntegerField(default=0)
    ttlamt=models.PositiveIntegerField(default=0)

     # function to calculate the total amount
    def save(self, *args, **kwargs):
        self.ttlamt=(int(self.quantity) * int(self.invamt))
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name}-{self.invamt}"
    
class Receipt(models.Model):
    mode=[
        ('MPESA ', 'Mpesa'),
        ('CASH ', 'Cash'),
        ('CHEQUE', 'Cheque'),
        ('BANK-TRANSACTION','Bank Payment'),
    ]

    invamount = models.ForeignKey(Business, on_delete=models.CASCADE)
    amt_paid=models.PositiveIntegerField(default=0)
    payment_mode=models.CharField(max_length=20,choices=mode, default='Mpesa')
    paymentdate=models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.invamount.name}- {self.invamount.invamt}- {self.amt_paid}"