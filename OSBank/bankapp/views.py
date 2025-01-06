from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, SignupForm, AmountAddedForm, GetLoanForm, AmountTransferForm, DebitForm, CreditForm, EditForm
from .models import Bankupload, AmountAdded, GetLoan, AmountTransfer, DebitPayment, CreditPayment
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import authenticated_user  
from babel.numbers import format_currency


def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')



# Register - register_1(signup) & register_2(register details)

@authenticated_user

def register_signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_2')
        else:
            form = SignupForm()
    return render(request, 'register_1.html', {'form': form})

@authenticated_user

def register_details(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = RegisterForm()
            print('Users with Bankupload details already registered cannot register this form')
    return render(request, 'register_2.html', {'form': form})



# Login

@authenticated_user

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = user_name, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Logout

def logout_user(request):
    logout(request)
    return redirect('home')



@login_required(login_url = 'login')

def amount_added(request):
    if request.method == 'POST':
        user = request.user
        # print(user)
        form = AmountAddedForm(request.POST)
        if form.is_valid():
            formuser = form.cleaned_data.get('user')
            # print(formuser)
            if formuser == user:
                form.save()
                ac_n1 = Bankupload.objects.get(user=user)
                # print(ac_n1)
                amt1 = int(form.data.get('amount_added'))
                # print(amt1)
                amt2 = int(ac_n1.amount)
                # print(amt2)
                add_amt = amt1+amt2
                # print(add_amt)
                ac_n1.amount = add_amt
                ac_n1.save()
                return redirect('home')
            else:
                print('Invalid Username')
    else:
        form = AmountAddedForm()
    return render(request, 'AmountAdded.html', {'form': form})




@login_required(login_url = 'login')

def amount_transfer(request, pk):
    if request.method == 'POST':
        user = request.user
        # print(user)
        form = AmountTransferForm(request.POST)
        if form.is_valid():
            formuser = form.cleaned_data.get('user')
            if formuser == user:
                ac_n1 = Bankupload.objects.get(user=user)
                # print(ac_n1)
                ac_n2 = ac_n1.pk
                # print(ac_n2)
                ac_n3a = form.cleaned_data.get('account_number')
                # print(ac_n3a)
                ac_n3b = ac_n3a.pk
                # print(ac_n3b)
                if ac_n2 == ac_n3b:
                    print('Cannot add amount only can transfer amount')
                else:
                    amt2 = int(form.cleaned_data.get('amount_added'))
                    # print(amt2)
                    sub_amt1 = int(ac_n1.amount)
                    # print(sub_amt1)
                    if sub_amt1 >= amt2:
                        sub_amt_total = sub_amt1-amt2
                        # print(sub_amt_total)
                        ac_n1.amount = sub_amt_total
                        ac_n1.save()
                        ac_n4 = Bankupload.objects.get(pk=ac_n3b)
                        # print(ac_n4)
                        add_amt2 = int(ac_n4.amount)
                        # print(add_amt2)
                        add_amt_total2 = add_amt2+amt2
                        # print(add_amt_total2)
                        ac_n4.amount = add_amt_total2
                        ac_n4.save()
                        form.save()
                        return redirect('home')
                    else:
                        print('Your bank balance is insufficient')
            else:
                print('Invalid Username')
    else:
        form = AmountTransferForm()
    return render(request, 'AmountTransfer.html', {'form': form})



@login_required(login_url = 'login')

def debit_pay(request):
    if request.method == 'POST':
        user = request.user
        # print(user)
        form_d = DebitForm(request.POST)
        if form_d.is_valid():
            formuser = form_d.cleaned_data.get('user')
            if formuser == user:
                ac_n1 = Bankupload.objects.get(user=user)
                # print(ac_n1)
                ac_n2 = form_d.cleaned_data.get('bill_payments')
                # print(ac_n2)
                ac_n3 = "Loan Re-Payment"
                # print(ac_n3)
                if ac_n2 == ac_n3: 
                    d_amt1 = int(form_d.cleaned_data.get('debitpay_amount'))
                    d_loan = int(ac_n1.loan)
                    d_amt2 = int(ac_n1.amount)
                    if d_loan >= d_amt1 and d_amt2 >= d_amt1:
                        d_loan_total = d_loan-d_amt1
                        d_amt_total = d_amt2-d_amt1
                        ac_n1.loan = d_loan_total
                        ac_n1.amount = d_amt_total
                        ac_n1.save()
                        form_d.save()
                        return redirect('home')
                    else:
                        print('Your loan/Amount is less than the entered amount')
                else:
                    d_amt3 = int(form_d.cleaned_data.get('debitpay_amount'))
                    d_amt4 = int(ac_n1.amount)
                    if d_amt4 >= d_amt3:
                        d_amt_total = d_amt4-d_amt3
                        ac_n1.amount = d_amt_total
                        # print(ac_n1.amount)
                        ac_n1.save()
                        form_d.save()
                        return redirect('home')
                    else:
                        print('Your bank balance is insufficient')
            else:
                print('Invalid Username')
    else:
        form_d = DebitForm()
    return render(request, 'debit.html', {'form_d': form_d})



@login_required(login_url = 'login')

def credit_pay(request):
    if request.method == 'POST':
        user = request.user
        # print(user)
        form_c = CreditForm(request.POST)
        if form_c.is_valid():
            formuser = form_c.cleaned_data.get('user')
            if formuser == user:
                form_c.save()
                ac_n1 = Bankupload.objects.get(user=user)
                # print(ac_n1)
                c_amt1 = int(form_c.data.get('creditpay_amount'))
                c_amt2 = int(ac_n1.loan)
                # print(c_amt2)
                c_amt_total = c_amt1+c_amt2
                ac_n1.loan = c_amt_total
                # print(ac_n1.loan)
                ac_n1.save()
                return redirect('home')
            else:
                print('Invalid username')
    else:
        form_c = CreditForm()
    return render(request, 'credit.html', {'form_c': form_c})



@login_required(login_url = 'login')

def trans_details(request):
    user = request.user
    detail0 = Bankupload.objects.all().filter(user=user)
    detail1a = AmountAdded.objects.all().filter(user=user)
    detail1b = GetLoan.objects.all().filter(user=user)
    detail1c = AmountTransfer.objects.all().filter(user=user)
    detail2 = DebitPayment.objects.all().filter(user=user)
    detail3 = CreditPayment.objects.all().filter(user=user)
    context = {'detail0': detail0, 'detail1a': detail1a, 'detail1b': detail1b, 'detail1c': detail1c, 'detail2': detail2, 'detail3': detail3,}
    return render(request, 'trans_details.html', context)



@login_required(login_url = 'login')

def get_loan(request):
    if request.method == 'POST':
        user = request.user
        # print(user)
        form = GetLoanForm(request.POST)
        if form.is_valid():
            formuser = form.cleaned_data.get('user')
            # print(formuser)
            if formuser == user:
                form.save()
                ac_n1 = Bankupload.objects.get(user=user)
                # print(ac_n1)
                loan_amt = int(form.data.get('loan_amount'))
                amt = int(ac_n1.amount)
                loan = int(ac_n1.loan)
                Total_amt = loan_amt+amt
                # print(Total_amt)
                Total_loan = loan_amt+loan
                # print(Total_loan)
                ac_n1.amount = Total_amt
                ac_n1.loan = Total_loan
                ac_n1.save()
                return redirect('home')
            else:
                print('Invalid Username')
    else:
        form = GetLoanForm()
    return render(request, 'Getloan.html', {'form': form})



@login_required(login_url = 'login')

def edit_account(request):
    user = request.user
    account = Bankupload.objects.all().get(user=user)
    editForm = EditForm(instance = account)
    if request.method == 'POST':
        editForm = EditForm(request.POST, instance = account)
        if editForm.is_valid():
            editForm.save()
            return redirect('home')
    context = {'editForm': editForm}
    return render(request, 'EditAccount.html', context)




@login_required(login_url = 'login')

def loan_emi(request):
    user = request.user
    loanUser = Bankupload.objects.all().get(user=user)
    # print(loanUser)
    loanAmount = loanUser.loan
    # print(loanAmount)

    ROI = 8
    Year = 2
    ROI_in_months = ROI/12/100
    Tenure_in_months = Year*12

    loanEMI = (loanAmount*(ROI_in_months)*((1+ROI_in_months)**(Tenure_in_months)))/(((1+ROI_in_months)**(Tenure_in_months))-1)
    Total_Amount_Paid = loanEMI*Tenure_in_months

    loanEMIapprox = int(round(loanEMI, 0))
    T_A_P_approx = int(round(Total_Amount_Paid, 0))

    Total_Interest = T_A_P_approx-loanAmount

    EMI = format_currency(loanEMIapprox, 'INR', locale='en_IN').replace('.00','').replace('₹','₹ ')
    Total_Amount = format_currency(T_A_P_approx, 'INR', locale='en_IN').replace('.00','').replace('₹','₹ ')
    Total_In = format_currency(Total_Interest, 'INR', locale='en_IN').replace('.00','').replace('₹','₹ ')
    loan_A = format_currency(loanAmount, 'INR', locale='en_IN').replace('.00','').replace('₹','₹ ')

    context = {'User': loanUser, 'ROI': ROI, 'Year': Year, 'loanEMI': EMI, 'loan_Amount': loan_A, 'Total_Interest': Total_In, 'Total_Amount': Total_Amount}
    return render(request, 'LoanDetails.html', context)