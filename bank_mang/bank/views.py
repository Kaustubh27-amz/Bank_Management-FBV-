from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AccountProfileForm, Amount
from .models import Account

# Create your views here.
def index(request):
    return render(request,'bank/index.html')

def about(request):
    return render(request,'bank/about.html')

@login_required
def users_list(request):
    if request.user.is_superuser:
        accounts=Account.objects.all()
    else:
        accounts=Account.objects.filter(user=request.user)
    return render(request,'bank/account_list.html',{'object_list':accounts})

@login_required
def users_detail(request,pk):
    account=get_object_or_404(Account,pk=pk)
    return render(request,'bank/account_detail.html',{'object':account})

@login_required
def users_create(request):
    form=AccountProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('account_list')
    return render(request,'bank/account_form.html',{'form':form})

@login_required
def users_update(request,pk):
    if request.user.is_superuser:
        obj=get_object_or_404(Account,pk=pk)
    else:
        obj=get_object_or_404(Account,pk=pk,user=request.user)

    form=AccountProfileForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('account_list')

    return render(request,'bank/account_form.html',{'form':form})

@login_required
def users_delete(request,pk):
    if request.user.is_superuser:
        obj=get_object_or_404(Account,pk=pk)
    else:
        obj=get_object_or_404(Account,pk=pk,user=request.user)

    if request.method == 'POST':
        obj.delete()
        return redirect('account_list')

    return render(request,'bank/account_delete.html',{'obj':obj})

@login_required
def deposit(request,pk):
    if request.user.is_superuser:
        obj=get_object_or_404(Account,pk=pk)
    else:
        obj=get_object_or_404(Account,pk=pk,user=request.user)

    form=Amount()
    if request.method == 'POST':
        form=Amount(request.POST)
        if form.is_valid():
            a=form.cleaned_data['value']
            b=a+obj.balance
            obj.balance=b
            obj.save()
            return redirect('account_list')
    return render(request,'bank/deposit.html',{'form':form})

@login_required
def withdraw(request,pk):
    if request.user.is_superuser:
        obj=get_object_or_404(Account,pk=pk)
    else:
        obj=get_object_or_404(Account,pk=pk,user=request.user)

    form=Amount()
    if request.method == 'POST':
        form=Amount(request.POST)
        if form.is_valid():
            a=form.cleaned_data['value']
            if a <= obj.balance:
                b=obj.balance-a
                obj.balance=b
                obj.save()

            return redirect('account_list')
    return render(request,'bank/withdraw.html',{'form':form})
