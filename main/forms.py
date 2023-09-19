from django.forms import ModelForm
from main.models import Card

class ProductForm(ModelForm):
    class Meta:
        model = Card
        fields = ["name", "amount", "price", "power", "energy_cost", "description"]