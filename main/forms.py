from django import forms
from django.forms import ModelForm
from main.models import Card
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    amount = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    power = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    energy_cost = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Card
        fields = ("name", "amount", "price", "power", "energy_cost", "description")

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'amount': forms.TextInput(attrs={'class': 'form-control'}),
        #     'price': forms.TextInput(attrs={'class': 'form-control'}),
        #     'power': forms.TextInput(attrs={'class': 'form-control'}),
        #     'energy_cost': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        # }

class RegisterForm(UserCreationForm): 
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta: 
        model = User 
        fields = ['username', 'email', 'password1', 'password2',]
    
    def custom_error_display(self):
        error_string = ""
        for field, errors in self.errors.items():
            error_string += errors
        return error_string