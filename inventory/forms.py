from django import forms

from .models import CarMake
from .models import CarModel
from .models import Stock
from .models import JapanStock
from .models import Receipts
from .models import CarExpenses
from .models import LeasedStock

class CarMakeForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    class Meta:
        model=CarMake
        fields=('__all__')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class UpdateCarMakeForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 2}),required=True)
    class Meta:
        model=CarMake
        fields=('__all__')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class CarModelForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    class Meta:
        model = CarModel
        fields = ['make','name']
        widgets = {
            'make': forms.Select(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class UpdateCarModelForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    class Meta:
        model = CarModel
        fields = ['make','name']
        widgets = {
            'make': forms.Select(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class StockForm(forms.ModelForm):
    color=forms.CharField(label='Color',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    year =forms.CharField(label='Make Year',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    chassisno=forms.CharField(label='Chassis No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    arrivaldate=forms.DateTimeField(label='Arrival Date',widget=DateInput)
    class Meta:
        model=Stock
        fields=('__all__')
        name=widgets = {
            'name': forms.Select(attrs={'class': 'form-control','rows': 1}),
            'status': forms.Select(attrs={'class': 'form-control','rows': 1}),
            }


class UpdateStockForm(forms.ModelForm):
    color=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    year =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    chassisno=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    arrivaldate=forms.DateTimeField(label='Arrival Date',widget=DateInput)
    class Meta:
        model=Stock
        fields=('__all__')
        widgets = {
            'name':  forms.Select(attrs={'class': 'form-control','rows': 1}),
            'status': forms.Select(attrs={'class': 'form-control','rows': 1}),
        }


class JapanStockForm(forms.ModelForm):
    chassisno=forms.CharField(label='Chassis No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    cif=forms.CharField(label='CIF(USD)',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    exchangerate=forms.CharField(label='Exchange Rate',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True) 
    paymentdate=forms.DateTimeField(label='Payment Date',widget=DateInput)
    class Meta:
        model=JapanStock
        fields=('name','chassisno','cif','exchangerate','paymentdate')
        widgets = {
            'name':  forms.Select(attrs={'class': 'form-control','rows': 1}),
        }

class UpdateJapanStockForm(forms.ModelForm):
    chassisno=forms.CharField(label='Chassis No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    cif=forms.CharField(label='CIF(USD)',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    exchangerate=forms.CharField(label='Exchange Rate',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    paymentdate=forms.DateTimeField(label='Payment Date',widget=DateInput)
    class Meta:
        model=JapanStock
        fields=('name','chassisno','cif','exchangerate','paymentdate')
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control','rows': 1}),
        }
    
class ReceiptForm(forms.ModelForm):
    invoiceno=forms.CharField(label='Invoice No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    invoiceamt=forms.CharField(label='Invoice Amount(USD)',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    amtpaid=forms.CharField(label='Amount Paid',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    datepaid=forms.DateTimeField(label='Payment Date',widget=DateInput)
    class Meta:
        model=Receipts
        fields=('__all__')

class UpdateReceiptForm(forms.ModelForm):
    invoiceno=forms.CharField(label='Invoice No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    invoiceamt=forms.CharField(label='Invoice Amount(USD)',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    amtpaid=forms.CharField(label='Amount Paid',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    datepaid=forms.DateTimeField(label='Payment Date',widget=DateInput)
    class Meta:
        model=Receipts
        fields=('__all__')

class CarExpensesForm(forms.ModelForm):
    unitcost=forms.IntegerField(label='Unit Cost(Kshs)',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    tax=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    portcharges=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    transportcharges=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    miscellaneous=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    class Meta:
        model = CarExpenses
        fields=('name','unitcost','tax','portcharges','transportcharges','miscellaneous')
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control','rows': 1}),
        }

class UpdateCarExpensesForm(forms.ModelForm):
    chassisno=forms.CharField(label='Chassis No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    unitcost=forms.IntegerField(label='Unit Cost(Kshs)',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    tax=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    portcharges=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    transportcharges=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    miscellaneous=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    class Meta:
        model = CarExpenses
        fields=('name','chassisno','unitcost','tax','portcharges','transportcharges','miscellaneous')
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control','rows': 1}),
        }

class LeasedStockForm(forms.ModelForm):
    person=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    contact=forms.IntegerField(label='Phone No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    showroom=forms.CharField(label='Show Room',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    leasedate=forms.DateTimeField(label='Lease Date',widget=DateInput)
    class Meta:
        model = LeasedStock
        fields=('person','contact','showroom','cardetails','leasedate')
        widgets = {'cardetails': forms.Select(attrs={'class': 'form-control','rows': 1})},

class UpdateLeasedStockForm(forms.ModelForm):
    person=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    contact=forms.IntegerField(label='Phone No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    showroom=forms.CharField(label='Show Room',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    leasedate=forms.DateTimeField(label='Lease Date',widget=DateInput)
    class Meta:
        model = LeasedStock
        fields=('person','contact','showroom','cardetails','leasedate')
        widgets = {'cardetails': forms.Select(attrs={'class': 'form-control','rows': 1})},