from dataclasses import fields
from django import forms
from .models import PaymentModel

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = ('name', 'amount')