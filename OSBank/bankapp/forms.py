from .models import Bankupload, AmountAdded, GetLoan, AmountTransfer, DebitPayment, CreditPayment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


bank_type_choices = (
    ('default', 'select'),
    ('saving account', 'saving account'), 
    ('current account', 'current account')
)


class RegisterForm(forms.ModelForm):

    name = forms.CharField(
        widget = forms.TextInput(attrs = {'class': 'form-control'}), 
        required = True
    )

    acc_no = forms.CharField(
        widget = forms.TextInput(attrs = {'class': 'form-control'}), 
        required = True
    )

    email = forms.EmailField(
        widget = forms.EmailInput(attrs = {'class': 'form-control'}), 
        required = True
    )

    date_of_birth = forms.DateField(
        widget = forms.DateInput(attrs = {'class': 'form-control', 'type': 'date'}), 
        required = True
    )

    amount = forms.FloatField(
        widget = forms.TextInput(attrs = {'class': 'form-control'}),
        required = True
    )

    bank_type = forms.CharField( 
        widget = forms.Select(attrs = {'class': 'form-select dropdown border-dark', 'data-toggle': 'dropdown'}, choices = bank_type_choices),
        required = True
    )

    agree = forms.BooleanField(
        disabled = False,
        error_messages = {'required': 'Please check the box'},
        widget = forms.CheckboxInput(attrs = {'class': 'checkbox'}),
        required = True
    )

    class Meta:
        model = Bankupload
        fields = ['user', 'name', 'acc_no', 'email', 'date_of_birth', 'amount', 'bank_type']




class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class AmountAddedForm(forms.ModelForm):

    amount_added = forms.FloatField(
        widget = forms.TextInput(attrs = {'class': 'form-control'}),
        required = True
    )

    class Meta:
        model = AmountAdded
        fields = ['user', 'amount_added']


class GetLoanForm(forms.ModelForm):

    loan_amount = forms.FloatField(
        widget = forms.TextInput(attrs = {'class': 'form-control'}),
        required = True
    )

    class Meta:
        model = GetLoan
        fields = ['user', 'loan_amount']


class AmountTransferForm(forms.ModelForm):

    amount_added = forms.FloatField(
        widget = forms.TextInput(attrs = {'class': 'form-control'}),
        required = True
    )

    class Meta:
        model = AmountTransfer
        fields = ['user', 'account_number', 'amount_added']


class DebitForm(forms.ModelForm):

    debitpay_amount = forms.FloatField(
        widget = forms.TextInput(attrs = {'class': 'form-control'}),
        required = True
    )

    class Meta:
        model = DebitPayment
        fields = ['user', 'bill_payments', 'debitpay_amount']


class CreditForm(forms.ModelForm):

    creditpay_amount = forms.FloatField(
        widget = forms.TextInput(attrs = {'class': 'form-control'}),
        required = True
    )

    class Meta:
        model = CreditPayment
        fields = ['user', 'bill_payments', 'creditpay_amount']


class EditForm(forms.ModelForm):

    class Meta:
        model = Bankupload
        fields = ['name', 'acc_no', 'email', 'date_of_birth', 'bank_type']


 
       