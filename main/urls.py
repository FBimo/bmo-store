from django.urls import path
from main.views import create_product_flutter, show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import increase_card, decrease_card, remove_card
from main.views import get_product_json, create_ajax
from main.views import remove_product_ajax
from main.views import modify_quantity_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase-card/<int:id>', increase_card, name='increase_card'),
    path('decrease-card/<int:id>', decrease_card, name='decrease_card'),
    path('remove-card/<int:id>', remove_card, name='remove_card'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('remove-product-ajax/<int:id>', remove_product_ajax, name='remove_product_ajax'),
    path('modify-qty-ajax/<int:id>/<str:symbol>', modify_quantity_ajax, name='modify_quantity_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    ]