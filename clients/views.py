from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import  Sum
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.templatetags.static import static
from xhtml2pdf import pisa

from .models import Prospects
from .models import Business
from .models import Receipt

from .forms import ProspectsForm
from .forms import UpdateProspectForm
from .forms import BusinessForm
from .forms import UpdateBusinessForm
from .forms import ReceiptForm
from .forms import UpdateReceiptForm
# Create your views here.
# office expenses view
def prospects_list(request):
    template= 'clients/prospects.html'
    prospectlists = Prospects.objects.all().order_by('-id')
    page=Paginator(prospectlists,7)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    return render(request,template , context)

#add a new client
@login_required(login_url='auth_app:login')
def add_prospect(request):
    template='clients/addprospect.html'
    if request.method == 'POST':
        form=ProspectsForm(request.POST)
        if form.is_valid():            
            form.save()

            messages.success(request, f'Client details added successfully')
            return redirect('clients:prospectslist')
    else:
            form=ProspectsForm()
    context={
            'form':form
        }
    return render(request, template,context)

# update prospects details
@login_required(login_url='auth_app:login')
def update_prospect(request,id):
    prospectlist=get_object_or_404(Prospects, id=id)
    if request.method == 'POST':
        form=UpdateProspectForm(request.POST, instance=prospectlist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Details updated successfully')
            return redirect('clients:prospectslist')
    else:
        form=UpdateProspectForm(instance=prospectlist)
    context={
        'form':form,
        }
    template='clients/updateprospect.html'
    return render(request,template,context)

#business details view
def business_list(request):
    template= 'clients/business/businessdetails.html'
    businesslists = Business.objects.all().order_by('-id')
    page=Paginator(businesslists,7)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    return render(request,template , context)

#add a new business lead
@login_required(login_url='auth_app:login')
def add_business(request):
    template='clients/business/addbusiness.html'
    if request.method == 'POST':
        form=BusinessForm(request.POST)
        if form.is_valid():            
            form.save()

            messages.success(request, f'Business details added successfully')
            return redirect('clients:businesslist')
    else:
            form=BusinessForm()
    context={
            'form':form,
        }
    return render(request, template,context)

# update business details
@login_required(login_url='auth_app:login')
def update_business(request,id):
    businesslist=get_object_or_404(Business, id=id)
    if request.method == 'POST':
        form=UpdateBusinessForm(request.POST, instance=businesslist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Details updated successfully')
            return redirect('clients:businesslist')
    else:
        form=UpdateBusinessForm(instance=businesslist)

    context={
        'form':form,
        }
    template='clients/business/updatebusiness.html'
    return render(request,template,context)

def proforma(request, id):
    template_path='clients/pdfs/proforma.html'
    image_path = 'assets/images/letterhead.jpg' 
    image = 'assets/images/bottom.jpg' 
  
    clientdetails = Business.objects.filter(id=id)  # Retrieve queryset

    context={
        'clientdetails':clientdetails,
        'image_path': image_path,
        "image":image,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Proforma_Invoice.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def finalinvoice(request, id):
    template_path='clients/pdfs/invoice.html'
    image_path = 'assets/images/letterhead.jpg' 
    image = 'assets/images/bottom.jpg' 
    
  
    clientdetails = Business.objects.filter(id=id)  # Retrieve queryset
    report_data = []
    for client in clientdetails:
        total_invoice_amount = client.invamt
        total_paid = Receipt.objects.filter(invamount=client).aggregate(Sum('amt_paid'))['amt_paid__sum']
        total_paid = total_paid or 0  # If no payments, set total_paid to 0
        balance = total_invoice_amount - total_paid

        report_data.append({
            'client': client.name,
            'total_invoice_amount': total_invoice_amount,
            'total_paid': total_paid,
            'balance': balance,
        })

    context={
        'clientdetails':clientdetails,
        'report_data':report_data,
        'image_path': image_path,
        "image":image,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Final_Invoice.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def salesagreement(request, id):
    template_path='clients/pdfs/sales.html'
    image_path = 'assets/images/letterhead.jpg' 
    image = 'assets/images/sign.jpg' 
  
    clientdetails = Business.objects.filter(id=id)  # Retrieve queryset

    context={
        'clientdetails':clientdetails,
        'image_path': image_path,
        'image': image,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Sales_Agreement.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


#Receipts details view
def receipts_list(request):
    template= 'clients/receipts/receiptsdetails.html'
    receiptlists = Receipt.objects.all().order_by('-id')
    page=Paginator(receiptlists,7)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    return render(request,template , context)

#add receipt details
@login_required(login_url='auth_app:login')
def add_receipt(request):
    template='clients/receipts/addreceipt.html'
    if request.method == 'POST':
        form=ReceiptForm(request.POST)
        if form.is_valid():            
            form.save()

            messages.success(request, f'Receipt details added successfully')
            return redirect('clients:receiptslist')
    else:
            form=ReceiptForm()
    context={
            'form':form,
        }
    return render(request, template,context)

# update business details
@login_required(login_url='auth_app:login')
def update_receipt(request,id):
    receiptlist=get_object_or_404(Receipt, id=id)
    if request.method == 'POST':
        form=UpdateReceiptForm(request.POST, instance=receiptlist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Details updated successfully')
            return redirect('clients:receiptslist')
    else:
        form=UpdateReceiptForm(instance=receiptlist)

    context={
        'form':form,
        }
    template='clients/receipts/updatereceipt.html'
    return render(request,template,context)

# transactional reports view
def transactional_report(request):
    template='clients/receipts/transactionalreports.html'
    clients = Business.objects.filter(receipt__isnull=False).distinct()
    report_data = []

    for client in clients:
        total_invoice_amount = client.invamt
        total_paid = Receipt.objects.filter(invamount=client).aggregate(Sum('amt_paid'))['amt_paid__sum']
        total_paid = total_paid or 0  # If no payments, set total_paid to 0
        balance = total_invoice_amount - total_paid

        report_data.append({
            'client': client.name,
            'total_invoice_amount': total_invoice_amount,
            'total_paid': total_paid,
            'balance': balance,
        })
    
    page = Paginator(report_data, 8).get_page(request.GET.get('page'))

    context = {
        'page': page,
    }
    return render(request, template, context)