from django.test import TestCase, Client
from main.models import Item

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    #another test
    def setUp(self):
        Item.objects.create(name="sunspot", amount=1, price=5000, description='Gain atk power with unspent energy', atk_power=50)
        Item.objects.create(name="hawkeye", amount=1, price=5000, description='Gain 3 atk power if you play card here next turn', atk_power=45)
    
    def test_get_desc(self):
        sunspot = Item.objects.get(name="sunspot")
        hawkeye = Item.objects.get(name="hawkeye")
        self.assertEqual(sunspot.get_desc(), "Gain atk power with unspent energy")
        self.assertEqual(hawkeye.get_desc(), "Gain 3 atk power if you play card here next turn")