from django.contrib import admin
from django.urls import path
from .views import Home, About, register_signup, register_details, amount_added, get_loan, amount_transfer, login_user, logout_user, debit_pay, credit_pay, trans_details, loan_emi, edit_account
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', Home, name = "home"),
    path('home', Home, name = "home"),
    path('about', About, name = "about"),
    path('register_1', register_signup, name="register_1"),
    path('register_2', register_details, name = "register_2"),
    path('Amount_Added', amount_added, name = "Amount_Added"),
    path('Get_Loan', get_loan, name = "Get_Loan"),
    path('Amount_transfer/<str:pk>', amount_transfer, name = "Amount_transfer"),
    path('login', login_user, name = "login"),
    path('logout', logout_user, name = "logout"),
    path('debit_pay', debit_pay, name = "debit_pay"),
    path('credit_pay', credit_pay, name = "credit_pay"),
    path('transaction_details', trans_details, name = "trans_details"),
    path('loan_EMI', loan_emi, name = "loan_EMI"),
    path('Edit_Account', edit_account, name = "Edit_Account"),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


