from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField('Card Name', max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    power = models.IntegerField()
    energy_cost = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_desc(self):
       return self.description

    