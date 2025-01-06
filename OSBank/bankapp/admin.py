from django.contrib import admin
from .models import Bankupload, AmountAdded, GetLoan, AmountTransfer, DebitPayment, CreditPayment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class BankuploadInline(admin.StackedInline):
    model = Bankupload
    can_delete = False
    verbose_name_plural = 'Bankuploads'

class CustomizedBankUserAdmin(UserAdmin):
    inlines = (BankuploadInline, )


admin.site.unregister(User)
admin.site.register(User, CustomizedBankUserAdmin)



class BankuploadsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'name', 'acc_no', 'email', 'date_of_birth', 'amount', 'bank_type', 'loan')
    list_filter = ('name', 'acc_no', 'email', 'amount', 'loan')
    search_fields = ['name', 'acc_no', 'email', 'date_of_birth', 'amount', 'bank_type', 'loan']


admin.site.register(Bankupload, BankuploadsAdmin)


class AmountAddedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'amount_added')

admin.site.register(AmountAdded, AmountAddedAdmin)


class GetLoanAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'loan_amount')

admin.site.register(GetLoan, GetLoanAdmin)


class AmountTransferAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'account_number', 'amount_added')

admin.site.register(AmountTransfer, AmountTransferAdmin)



class DebitPaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'bill_payments', 'debitpay_amount')

admin.site.register(DebitPayment, DebitPaymentAdmin)



class CreditPaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'bill_payments', 'creditpay_amount')

admin.site.register(CreditPayment, CreditPaymentAdmin)





