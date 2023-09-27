from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    name = models.CharField('Card Name', max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    power = models.IntegerField()
    energy_cost = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def get_desc(self):
       return self.description
    

    def set_amount(self, param):
        if param == "inc":
            self.amount += 1
        else:
            self.amount -= 1


    