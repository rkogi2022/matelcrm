from django import forms

from .models import Prospects
from inventory.models import Stock
from .models import Business
from .models import Receipt

#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class ProspectsForm(forms.ModelForm):
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    phoneno =forms.CharField(label='Phone No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    idno=forms.CharField(label='ID/Passport No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    krapin=forms.CharField(label='KRA PIN',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    pobox=forms.CharField(label='P.O Box',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    class Meta:
        model=Prospects
        fields=('name','phoneno','idno','krapin', 'pobox')

class UpdateProspectForm(forms.ModelForm):
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    phoneno =forms.CharField(label='Phone No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    idno=forms.CharField(label='ID/Passport No',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    krapin=forms.CharField(label='KRA PIN',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    pobox=forms.CharField(label='P.O Box',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    class Meta:
        model=Prospects
        fields=('name','phoneno','idno','krapin','pobox')

# add business details
class BusinessForm(forms.ModelForm):
    regno = forms.CharField(label='Registration No', widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}), required=True)
    engine = forms.CharField(label='Engine Capacity', widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}), required=True)
    invamt = forms.CharField(label='Invoice Amount', widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}), required=True)
    cardetails = forms.ModelChoiceField(queryset=Stock.objects.filter(status__icontains='available'))

    class Meta:
        model = Business
        fields = ['name','fuel','transmission','regno','engine','invamt','cardetails']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'fuel': forms.Select(attrs={'class': 'form-control'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
        }

#update business details
class UpdateBusinessForm(forms.ModelForm):
    regno = forms.CharField(label='Registration No', widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}), required=True)
    engine = forms.CharField(label='Engine Capacity', widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}), required=True)
    invamt = forms.CharField(label='Invoice Amount', widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}), required=True)
    cardetails = forms.ModelChoiceField(queryset=Stock.objects.filter(status__icontains='available'))

    class Meta:
        model = Business
        fields = ['name','fuel','transmission','regno','engine','invamt','cardetails']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'fuel': forms.Select(attrs={'class': 'form-control'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
        }

#Receipts details
class ReceiptForm(forms.ModelForm):
    amt_paid=forms.CharField(label='Amount Paid',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    paymentdate=forms.DateTimeField(label='Payment Date',widget=DateInput)
    class Meta:
        model=Receipt
        fields=('__all__')
        invamount=widgets = { forms.Select(attrs={'class': 'form-control','rows': 1})},
        payment_mode={ forms.Select(attrs={'class': 'form-control','rows': 1})}

#Update receipts details
class UpdateReceiptForm(forms.ModelForm):
    amt_paid=forms.CharField(label='Amount Paid',widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),required=True)
    paymentdate=forms.DateTimeField(label='Payment Date',widget=DateInput)
    class Meta:
        model=Receipt
        fields=('__all__')
        invamount=widgets = { forms.Select(attrs={'class': 'form-control','rows': 1})},
        payment_mode={ forms.Select(attrs={'class': 'form-control','rows': 1})}