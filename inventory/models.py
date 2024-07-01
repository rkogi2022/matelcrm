from django.db import models
from django.db.models import UniqueConstraint, Q
from django.utils import timezone

# Create your models here.
class CarMake(models.Model):
    name=models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name


    
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    class Meta:
        unique_together = ['make', 'name',]

    def __str__(self):
        return f"{self.make.name}  {self.name}"

status=[
        ('AVAILABLE ','AVAILABLE'),
        ('SOLD','SOLD'),
]
class Stock(models.Model):
    name = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    color=models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=None)
    chassisno=models.CharField(max_length=50)
    arrivaldate=models.DateField(default=timezone.now)
    status=models.CharField(max_length=20,choices=status, default='AVAILABLE')

    def __str__(self):
        return f" {self.name} - {self.chassisno} - {self.year} - {self.color}"
    
class JapanStock(models.Model):
    name = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    chassisno=models.CharField(max_length=50)
    cif = models.PositiveIntegerField(default=0)
    exchangerate = models.PositiveIntegerField(default=1)
    paymentdate=models.DateField(default=timezone.now)
    totalcost=models.PositiveIntegerField(default=0)

        # function to calculate the total amount
    def save(self, *args, **kwargs):
        self.totalcost=(int(self.cif) * int(self.exchangerate))
        return super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name} - {self.chassisno}"


class Receipts(models.Model):
    invoiceno=models.CharField(max_length=30)
    invoiceamt=models.IntegerField(default=0)
    amtpaid=models.IntegerField(default=0)
    datepaid=models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.invoiceno}"
    
class CarExpenses(models.Model):
    totalcost=models.PositiveIntegerField(default='0')
    name = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    chassisno=models.CharField(max_length=50, default='0001')
    unitcost = models.PositiveIntegerField(default='0')
    tax=models.PositiveIntegerField(default='0')
    portcharges=models.PositiveIntegerField(default='0')
    transportcharges=models.PositiveIntegerField(default='0')
    miscellaneous=models.PositiveIntegerField(default='0')

    # function to calculate the total amount
    def save(self, *args, **kwargs):
        self.totalcost=(int(self.unitcost) + int(self.tax) + int(self.portcharges) + int(self.transportcharges) + int(self.miscellaneous))
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.totalcost}"
    
class LeasedStock(models.Model):
    person=models.CharField(max_length=100)
    contact=models.PositiveIntegerField(default=None)
    showroom=models.CharField(max_length=150)
    cardetails=models.ForeignKey(Stock, on_delete=models.CASCADE)
    leasedate=models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.person} - {self.cardetails}"