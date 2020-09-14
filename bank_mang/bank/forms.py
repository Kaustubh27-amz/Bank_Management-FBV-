from django import forms
from .models import Account

class AccountProfileForm(forms.ModelForm):
    class Meta():
        model=Account
        fields='__all__'
class Amount(forms.Form):
    value=forms.IntegerField()
