from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import CompanyExpenses
from .models import PersonalExpenses

from .forms import OfficeExpenseForm
from .forms import UpdateOfficeExpenseForm
from .forms import PersonalExpenseForm
from .forms import UpdatePersonalExpenseForm

# Create your views here.
# office expenses view
def officeexpenses_list(request):
    template= 'matel/expenses/office.html'
    officelists = CompanyExpenses.objects.all().order_by('-id')
    page=Paginator(officelists,7)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    return render(request,template , context)

#add a new office expense
@login_required(login_url='auth_app:login')
def add_officeexpense(request):
    template='matel/expenses/addofficeexpense.html'
    if request.method == 'POST':
        form=OfficeExpenseForm(request.POST)
        if form.is_valid():            
            form.save()

            messages.success(request, f'Expenses posted successfully')
            return redirect('matel:officeexpenseslist')
    else:
            form=OfficeExpenseForm()
    context={
            'form':form
        }
    return render(request, template,context)

# search office expense by month
def search_officeexpense(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:
            searched_details = CompanyExpenses.objects.filter(Q(month__icontains=searched))
    
    return render(request, 'matel/expenses/searchoffice.html', {'searched_details': searched_details})
# update office expenses details
@login_required(login_url='auth_app:login')
def update_officeexpense(request,id):
    expenseslist=get_object_or_404(CompanyExpenses, id=id)
    if request.method == 'POST':
        form=UpdateOfficeExpenseForm(request.POST, instance=expenseslist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Expense updated successfully')
            return redirect('matel:officeexpenseslist')
    else:
        form=UpdateOfficeExpenseForm(instance=expenseslist)
    context={
        'form':form,
        }
    template='matel/expenses/updateofficeexpense.html'
    return render(request,template,context)

# house expenses view
def personalexpenses_list(request):
    template= 'matel/expenses/personalexpenses.html'
    personallists = PersonalExpenses.objects.all().order_by('-id')
    page=Paginator(personallists,7)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    return render(request,template , context)

#add a personal expense
@login_required(login_url='auth_app:login')
def add_personalexpense(request):
    template='matel/expenses/addpersonalexpense.html'
    if request.method == 'POST':
        form=PersonalExpenseForm(request.POST)
        if form.is_valid():            
            form.save()

            messages.success(request, f'Expenses posted successfully')
            return redirect('matel:personalexpenseslist')
    else:
            form=PersonalExpenseForm()
    context={
            'form':form
        }
    return render(request, template,context)

# update office expenses details
@login_required(login_url='auth_app:login')
def update_personalexpense(request,id):
    expenseslist=get_object_or_404(PersonalExpenses, id=id)
    if request.method == 'POST':
        form=UpdatePersonalExpenseForm(request.POST, instance=expenseslist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Expense updated successfully')
            return redirect('matel:officeexpenseslist')
    else:
        form=UpdatePersonalExpenseForm(instance=expenseslist)
    context={
        'form':form,
        }
    template='matel/expenses/updatepersonalexpense.html'
    return render(request,template,context)

# search personal expense by month
def search_personalexpense(request):
    if request.method == 'GET':
        searched = request.GET.get('searched')
        if searched:
            searched_details = PersonalExpenses.objects.filter(Q(month__icontains=searched))
    
    return render(request, 'matel/expenses/personalsearch.html', {'searched_details': searched_details})
