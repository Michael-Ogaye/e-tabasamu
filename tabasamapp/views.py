from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import FacilityForm,UpdateAccountForm,TransactionForm,SignupForm
from .models import Facility,Transaction,AccountStatement,UserAccount

# Create your views here.
def index(request):
    return render(request, 'base.html')

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

