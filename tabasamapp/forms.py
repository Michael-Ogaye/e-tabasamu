
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import UserAccount,Transaction,AccountStatement,Facility



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class FacilityForm(forms.ModelForm):
    class Meta:
        model=Facility
        fields='__all__'


class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=['type','amount','facility','maker','statement']


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model=UserAccount
        fields=['name','phone_no','account_picture','info']


