from django.test import TestCase, Client
from main.models import Card

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
        Card.objects.create(name="Gundala", amount=35, price=15000, power=3, energy_cost=4, description='Summon lightning to gain +3 power and destroy all card nearby')
        Card.objects.create(name="Godam", amount=35, price=16000, power=5, energy_cost=3, description='Invincible (cannot be destroyed, weakened, etc) until round 6')
    
    def test_get_desc(self):
        gundala = Card.objects.get(name="Gundala")
        godam = Card.objects.get(name="Godam")
        self.assertEqual(gundala.get_desc(), "Summon lightning to gain +3 power and destroy all card nearby")
        self.assertEqual(godam.get_desc(), "Invincible (cannot be destroyed, weakened, etc) until round 6")