from django import forms
from django.forms import ModelForm
from main.models import Card

class ProductForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ("name", "amount", "price", "power", "energy_cost", "description")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'power': forms.TextInput(attrs={'class': 'form-control'}),
            'energy_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

        }