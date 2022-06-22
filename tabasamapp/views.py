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

def update_account(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_account', user.username)
    else:
        form = UpdateAccountForm(instance=request.user.account)
    return render(request, 'tabasamapp/editaccount.html', {'form': form})

def useracc_statement(request,id):
    user_f=User.objects.get(id=id)
    statements=Transaction.objects.filter(maker=user_f)
    savings=[]
    withdrawals=[]
    for st in statements:
        if st.type=='deposit':
            saving=st.amount
            savings.append(saving)
        elif st.type=='withdrawal':
            withdrawal=st.amount
            withdrawals.append(withdrawal)

         
    
    total_savings=sum(savings)
    total_widhdrawals=sum(withdrawals)
    account_standings=sum(savings)-sum(withdrawals)

    return render(request,'tabasamapp/statement.html',{'transactions':statements,'standings':account_standings,'savings':total_savings,'withdrawals':total_widhdrawals})
