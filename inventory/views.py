from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import CarMake
from .models import CarModel
from .models import Stock
from .models import JapanStock
from .models import Receipts
from .models import CarExpenses
from .models import LeasedStock

from .forms import CarMakeForm
from .forms import UpdateCarMakeForm
from .forms import CarModelForm
from .forms import UpdateCarModelForm
from .forms import StockForm
from .forms import UpdateStockForm
from .forms import JapanStockForm
from .forms import UpdateJapanStockForm
from .forms import ReceiptForm
from .forms import UpdateReceiptForm
from .forms import CarExpensesForm
from .forms import UpdateCarExpensesForm
from .forms import LeasedStockForm
from .forms import UpdateLeasedStockForm

# Create your views here.
    #view all makes available
def carmake_list(request):
    template= 'inventory/carmake/carmake.html'
    carlists = CarMake.objects.all().order_by('-id')
    page=Paginator(carlists,7)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    return render(request,template , context)

    #create a new make
@login_required(login_url='auth_app:login')
def create_carmake(request):
    template='inventory/carmake/add-carmake.html'
    if request.method == 'POST':
        form=CarMakeForm(request.POST)
        if form.is_valid():            
            form.save()

            messages.success(request, f'Car Model added successfully')
            return redirect('inventory:carmake')
    else:
            form=CarMakeForm()
    context={
            'form':form
        }
    return render(request, template,context)


    # update car make details
@login_required(login_url='auth_app:login')
def update_carmake(request,id):
    carlist=get_object_or_404(CarMake, id=id)
    if request.method == 'POST':
        form=UpdateCarMakeForm(request.POST, instance=carlist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Car Make updated successfully')
            return redirect('inventory:carmake')
    else:
        form=UpdateCarMakeForm(instance=carlist)
    context={
        'form':form,
        }
    template='inventory/carmake/updatecarmake.html'
    return render(request,template,context)

#delete a  car make
@login_required(login_url='auth_app:login')
def delete_carmake(request,id):
    id = int(id)
    try:
        carmake_list=CarMake.objects.get(id=id)
    except:
        messages.error(request, f'The car make was deleted successfully')
        return redirect('inventory:carmake')
    carmake_list.delete()
    return redirect('inventory:carmake') 

# view the different models available
def carmodel_list(request):
    template= 'inventory/carmodel/carmodel.html'
    carmodels = CarModel.objects.all()
    page=Paginator(carmodels,7)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    return render(request,template , context)

# create a new model
@login_required(login_url='auth_app:login')
def addcarmodel(request):
    template='inventory/carmodel/addcarmodel.html'
    if request.method == 'POST':
        form=CarModelForm(request.POST)
        if form.is_valid():            
            form.save()
           
            messages.success(request, f'Car Model added successfully')
            return redirect('inventory:carmodel')
    else:
            form=CarModelForm()
    context={
        'form':form,
    }
    return render(request,template,context)



   # update car model details
@login_required(login_url='auth_app:login')
def update_carmodel(request,id):
    carmodels=get_object_or_404(CarModel, id=id)
    if request.method == 'POST':
        form=UpdateCarModelForm(request.POST, instance=carmodels)
        if form.is_valid():
            form.save()
            messages.success(request, f'Car Model updated successfully')
            return redirect('inventory:carmodel')
    else:
        form=UpdateCarModelForm(instance=carmodels)
    context={
        'form':form,
        }
    template='inventory/carmodel/updatecarmodel.html'
    return render(request,template,context)

#delete a  car model
@login_required(login_url='auth_app:login')
def delete_carmodel(request,id):
    id = int(id)
    try:
        carmodels=CarModel.objects.get(id=id)
    except:
        messages.error(request, f'The car make was deleted successfully')
        return redirect('inventory:carmodel')
    carmodels.delete()
    return redirect('inventory:carmodel') 

def stocklist(request):
    template='inventory/stock/localstock/stock.html'
    stocklist=Stock.objects.all().order_by('-id')
    page=Paginator(stocklist,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
    }
    return render(request,template,context)

@login_required(login_url='auth_app:login')
def add_stock(request):
    template='inventory/stock/localstock/addstock.html'
    if request.method == 'POST':
        form=StockForm(request.POST)
        if form.is_valid():            
            form.save()
            
            messages.success(request, f'Stock details added successfully')
            return redirect('inventory:stock')
    else:
            form=StockForm()
    context={
        'form':form,
    }
    return render(request,template,context)

# search a car to the stock inventory
@login_required(login_url='users:login')
def stock_searchbar(request):
    if request.method == 'GET':
        searched=request.GET.get('searched')
        if searched:
            multiple_searched=Q(Q(chassisno__icontains=searched) |Q(status__icontains=searched))
            searcheddetails=Stock.objects.filter(multiple_searched)
            return render(request, 'inventory/stock/localstock/localsearch.html',{'searcheddetails':searcheddetails})
        else:
            return render(request, 'inventory/stock/localstock/localsearch.html',{})

   # update stock details
@login_required(login_url='auth_app:login')
def update_stock(request,id):
    stocklist=get_object_or_404(Stock, id=id)
    if request.method == 'POST':
        form=UpdateStockForm(request.POST, instance=stocklist)
        if form.is_valid():
            form.save()

            return redirect('inventory:stock')
    else:
        form=UpdateStockForm(instance=stocklist)
    context={
        'form':form,
        }
    template='inventory/stock/localstock/updatestock.html'
    return render(request,template,context)

# japan stock details
def japanstock(request):
    template='inventory/stock/japanstock/japan.html'
    stocklist=JapanStock.objects.all().order_by('-id')
    page=Paginator(stocklist,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
    }
    return render(request,template,context)

@login_required(login_url='auth_app:login')
def add_japanstock(request):
    template='inventory/stock/japanstock/addjapanstock.html'
    if request.method == 'POST':
        form=JapanStockForm(request.POST)
        if form.is_valid():            
            form.save()
            
            messages.success(request, f'Details added successfully')
            return redirect('inventory:japanstock')
    else:
            form=JapanStockForm()
    context={
        'form':form,
    }
    return render(request,template,context)

# update stock
@login_required(login_url='auth_app:login')
def update_japanstock(request,id):
    stocklist=get_object_or_404(JapanStock, id=id)
    if request.method == 'POST':
        form=UpdateJapanStockForm(request.POST, instance=stocklist)
        if form.is_valid():
            form.save()

            return redirect('inventory:japanstock')
    else:
        form=UpdateJapanStockForm(instance=stocklist)
    context={
        'form':form,
        }
    template='inventory/stock/japanstock/updatejapanstock.html'
    return render(request,template,context)

# search a car in the japan stock inventory   
@login_required(login_url='users:login')
def japanstock_searchbar(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:
            searched_details = JapanStock.objects.filter(Q(name__name__icontains=searched) | Q(chassisno__icontains=searched))
            return render(request, 'inventory/stock/japanstock/japansearch.html', {'searcheddetails': searched_details})
        else:
            return render(request, 'inventory/stock/japanstock/japansearch.html', {})

# Receipts details
def receiptsdetails(request):
    template='inventory/stock/accounts/receipt.html'
    receiptlist=Receipts.objects.all().order_by('-id')
    page=Paginator(receiptlist,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    if request.method == 'POST':
        form=ReceiptForm(request.POST)
        if form.is_valid():            
            form.save()
            
            messages.success(request, f'Receipt details added successfully')
            return redirect('inventory:receiptsdetails')
    else:
            form=ReceiptForm()
    context={
        'page':page,
        'form':form,
    }
    return render(request,template,context)

# update stock
@login_required(login_url='auth_app:login')
def update_receipts(request,id):

    receiptlist=get_object_or_404(Receipts, id=id)
    if request.method == 'POST':
        form=UpdateReceiptForm(request.POST, instance=receiptlist)
        if form.is_valid():
            form.save()

            return redirect('inventory:receiptsdetails')
    else:
        form=UpdateReceiptForm(instance=receiptlist)
    context={
        'form':form,
        }
    template='inventory/stock/accounts/receipt.html'
    return render(request,template,context)

# searching by invoice no      
def search_by_invoice(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:
            searched_details = Receipts.objects.filter(Q(invoiceno__icontains=searched) | Q(amtpaid__icontains=searched))
    
    return render(request, 'inventory/stock/accounts/searchreceipt.html', {'searched_details': searched_details})

# car expenses details
def carexpenses_list(request):
    template= 'inventory/stock/accounts/carexpenses.html'
    carexpenseslists = CarExpenses.objects.all().order_by('-id')
    page=Paginator(carexpenseslists,7)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    return render(request,template , context)

@login_required(login_url='auth_app:login')
def addexpense(request):
    template='inventory/stock/accounts/addexpense.html'
    if request.method == 'POST':
        form=CarExpensesForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, f'Car expenses details added successfully')
            return redirect('inventory:carexpenses_list')
    else:
            form=CarExpensesForm()
    context={
            'form':form
        }
    return render(request, template,context)

@login_required(login_url='auth_app:login')
def update_carexpenses(request,id):
    carexpenses_list=get_object_or_404(CarExpenses, id=id)
    if request.method == 'POST':
        form=UpdateCarExpensesForm(request.POST, instance=carexpenses_list)
        if form.is_valid():
            form.save()
            messages.success(request, f'Car expenses details updated successfully')
            return redirect('inventory:carexpenses_list')
    else:
        form=UpdateCarExpensesForm(instance=carexpenses_list)
    context={
        'form':form,
        }
    template='inventory/stock/accounts/updateexpense.html'
    return render(request,template,context)

# searching through the car expenses      
def search_carexpenses(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:
            searched_details = CarExpenses.objects.filter(Q(chassisno__icontains=searched) )
    
    return render(request, 'inventory/stock/accounts/carexpensesearch.html', {'searched_details': searched_details})

    #view all leased cars available
def leasedstock_list(request):
    template= 'inventory/stock/leasedstock/leasedstock.html'
    leasedlists = LeasedStock.objects.all().order_by('-id')
    page=Paginator(leasedlists,7)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    return render(request,template , context)

    #create a new make
@login_required(login_url='auth_app:login')
def add_leasedcars(request):
    template='inventory/stock/leasedstock/addleasedstock.html'
    if request.method == 'POST':
        form=LeasedStockForm(request.POST)
        if form.is_valid():            
            form.save()

            messages.success(request, f'Car Details added successfully')
            return redirect('inventory:leasedstock')
    else:
            form=LeasedStockForm()
    context={
            'form':form
        }
    return render(request, template,context)


    # update car leased details
@login_required(login_url='auth_app:login')
def update_leasedcars(request,id):
    leasedlist=get_object_or_404(LeasedStock, id=id)
    if request.method == 'POST':
        form=UpdateLeasedStockForm(request.POST, instance=leasedlist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Car details updated successfully')
            return redirect('inventory:leasedstock')
    else:
        form=UpdateLeasedStockForm(instance=leasedlist)
    context={
        'form':form,
        }
    template='inventory/stock/leasedstock/updateleasedstock.html'
    return render(request,template,context)

# search a car to the leased stock inventory
@login_required(login_url='users:login')
def leasedcars_searchbar(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:
            # Perform case-insensitive search on multiple fields
            searched_details = LeasedStock.objects.filter(
                Q(person__icontains=searched) |
                Q(contact__icontains=searched) |
                Q(showroom__icontains=searched)
            )
            return render(request, 'inventory/stock/leasedstock/search.html', {'searcheddetails': searched_details})
        else:
            return render(request, 'inventory/stock/leasedstock/search.html', {})

        
