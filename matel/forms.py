from django import forms

from .models import CompanyExpenses
from .models import PersonalExpenses


#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class OfficeExpenseForm(forms.ModelForm):
    month=forms.CharField(label='Month',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    officerent =forms.CharField(label='Office Rent',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    salary=forms.CharField(label='Salary',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    officeinternet=forms.CharField(label='Office Internet',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    electricity=forms.CharField(label='Electricity',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    miscellaneouscosts=forms.CharField(label='Miscellaneous Costs',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    paymentdate=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=CompanyExpenses
        fields=('month','officerent','salary','officeinternet','electricity','miscellaneouscosts','paymentdate')

class UpdateOfficeExpenseForm(forms.ModelForm):
    month=forms.CharField(label='Month',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    officerent =forms.CharField(label='Office Rent',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    salary=forms.CharField(label='Salary',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    officeinternet=forms.CharField(label='Office Internet',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    electricity=forms.CharField(label='Electricity',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    miscellaneouscosts=forms.CharField(label='Miscellaneous Costs',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    paymentdate=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=CompanyExpenses
        fields=('month','officerent','salary','officeinternet','electricity','miscellaneouscosts','paymentdate')

class PersonalExpenseForm(forms.ModelForm):
    month=forms.CharField(label='Month',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    houserent =forms.CharField(label='House Rent',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    homeinternet=forms.CharField(label='Home Internet',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    monthlyfuel=forms.CharField(label='Monthly Fuel',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    carmaintenance=forms.CharField(label='Car Maintenance',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    date=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=PersonalExpenses
        fields=('month','houserent','homeinternet','monthlyfuel','carmaintenance','date')

class UpdatePersonalExpenseForm(forms.ModelForm):
    month=forms.CharField(label='Month',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    houserent =forms.CharField(label='House Rent',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    homeinternet=forms.CharField(label='Home Internet',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    monthlyfuel=forms.CharField(label='Monthly Fuel',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    carmaintenance=forms.CharField(label='Car Maintenance',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    date=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=PersonalExpenses
        fields=('month','houserent','homeinternet','monthlyfuel','carmaintenance','date')