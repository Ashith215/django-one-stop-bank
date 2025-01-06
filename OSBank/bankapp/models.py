from django.db import models
from django.contrib.auth.models import User

bank_type_choices = (
    ('saving account', 'saving account'), 
    ('current account', 'current account')
)


class Bankupload(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length = 100)
    acc_no = models.CharField(max_length = 10, primary_key=True)
    email = models.EmailField(max_length = 254, null=True, blank=True)
    date_of_birth = models.DateField()
    amount = models.FloatField()
    bank_type = models.CharField(max_length = 15, choices = bank_type_choices)
    loan = models.FloatField(default = 0, null = True, blank = True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class AmountAdded(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    amount_added = models.FloatField(default = 0, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class GetLoan(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    loan_amount = models.FloatField(default = 0, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class AmountTransfer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    account_number = models.ForeignKey(Bankupload, on_delete = models.CASCADE, null=True)
    amount_added = models.FloatField(default = 0, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


debit_bill_payments_choices = (
    ('mobile recharge', 'mobile recharge'),
    ('DTH/Cable TV', 'DTH/Cable TV'),
    ('Electricity', 'Electricity'),
    ('Subs fee', 'Subs fee'),
    ('Water', 'Water'),
    ('Loan Re-Payment', 'Loan Re-Payment')
)

class DebitPayment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    bill_payments = models.CharField(max_length = 15, choices = debit_bill_payments_choices)
    debitpay_amount = models.FloatField(default = 0, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)



credit_bill_payments_choices = (
    ('mobile recharge', 'mobile recharge'),
    ('DTH/Cable TV', 'DTH/Cable TV'),
    ('Electricity', 'Electricity'),
    ('Subs fee', 'Subs fee'),
    ('Water', 'Water')
)

class CreditPayment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    bill_payments = models.CharField(max_length = 15, choices = credit_bill_payments_choices)
    creditpay_amount = models.FloatField(default = 0, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)



