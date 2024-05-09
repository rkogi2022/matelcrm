# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from inventory.models import Stock, JapanStock, LeasedStock
# import mesagess
from django.contrib import messages
# import forms
from .forms import CreateUserForm

# Create your views here.

# register a new user
def registerpage(request):
    if request.user.is_authenticated:
        return redirect()
    else:
        form=CreateUserForm()
        
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('authapp:login')

        context={'form':form}
        return render(request, 'authapp/register.html',context)

# login
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('authapp:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user =authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect ('authapp:home')
            else:
                messages.info(request, 'Username OR Password is Incorrect')
                
        context={}
        return render(request,'authapp/login.html',context)

# logout
def logoutUser(request):
    logout(request)
    return redirect('authapp:login')


def home(request):
     # Query the Stock model to count the number of available cars
    local_count = Stock.objects.filter(status__contains='AVAILABLE').count()
    japan_count = JapanStock.objects.all().count()
    leased_count = LeasedStock.objects.all().count()
    
    # Pass the count to the template context
    context = {
        'local_count': local_count,
        'japan_count': japan_count,
        'leased_count': leased_count,
        }
    template="authapp/index.html"
    return render(request,template,context)




