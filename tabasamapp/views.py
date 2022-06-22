from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import FacilityForm,UpdateAccountForm,TransactionForm,SignupForm
from .models import Facility,Transaction,AccountStatement,UserAccount
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'tabasamapp/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES)
        if form.is_valid():
            
            facility=form.save()
            return redirect('index')
    else:
        form = FacilityForm()
    return render(request, 'tabasamapp/add_facility.html', {'form': form})


def make_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction=form.save()
            return redirect('index')
    else:
        form = TransactionForm()
    return render(request, 'tabasamapp/transaction.html', {'form': form})


def User_account(request,pk):
    user=User.objects.get(pk=pk)

    return render(request, 'tabasamapp/useraccount.html',{'user':user})