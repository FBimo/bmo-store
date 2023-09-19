from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import Card
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    cards = Card.objects.all()

    total_cards = 0
    for card in cards:
        total_cards += 1

    context = {
        'my_app': 'Marpellus Cenep',
        'name': 'FBmo',
        'class': 'PBP C',
        'cards': cards,
        'total_cards': total_cards
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)


def show_xml(request):
    data = Card.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Card.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Card.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Card.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

