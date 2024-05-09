from django.db import models
from django.db.models import UniqueConstraint, Q
from django.utils import timezone

# Create your models here.
class CompanyExpenses(models.Model):
    month=models.CharField(max_length=50)
    officerent=models.PositiveIntegerField(default=0)
    salary=models.PositiveIntegerField(default=0)
    officeinternet=models.PositiveIntegerField(default=0)
    miscellaneouscosts=models.PositiveIntegerField(default=0)
    electricity=models.PositiveIntegerField(default=0)
    paymentdate=models.DateField(default=timezone.now)
    totalcost=models.PositiveIntegerField(default='0')

    # function to calculate the total amount
    def save(self, *args, **kwargs):
        self.totalcost=(int(self.officerent) + int(self.salary) + int(self.officeinternet) + int(self.miscellaneouscosts) + int(self.electricity))
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.month
    

class PersonalExpenses(models.Model):
    month=models.CharField(max_length=50)
    houserent=models.PositiveIntegerField(default=0)
    homeinternet=models.PositiveIntegerField(default=0)
    monthlyfuel=models.PositiveIntegerField(default=0)
    carmaintenance=models.PositiveIntegerField(default=0)
    date=models.DateField(default=timezone.now)
    totalcost=models.PositiveIntegerField(default='0')

    # function to calculate the total amount
    def save(self, *args, **kwargs):
        self.totalcost=(int(self.houserent) +  int(self.homeinternet) + int(self.monthlyfuel) + int(self.carmaintenance))
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.month