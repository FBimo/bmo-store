import datetime
import json
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import Card
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    cards = Card.objects.filter(user=request.user)

    total_cards = 0
    for card in cards:
        total_cards += 1

    context = {
        'my_app': 'Marpellus Cenep',
        'name': request.user.username,
        'class': 'PBP C',
        'cards': cards,
        'total_cards': total_cards,
        # 'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        cards = form.save(commit=False)
        cards.user = request.user
        cards.save()
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


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
            
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def increase_card(request, id):
    card = Card.objects.filter(user=request.user, pk=id).first()
    if card.amount > 0:
        card.amount += 1
    card.save()

    return HttpResponseRedirect(reverse('main:show_main'))


def decrease_card(request, id):
    card = Card.objects.filter(user=request.user, pk=id).first()
    if card.amount > 0:
        card.amount -= 1
    card.save()

    return HttpResponseRedirect(reverse('main:show_main'))


def remove_card(request, id):
    card = Card.objects.filter(user=request.user, pk=id).get(pk = id)
    if card.amount > 0:
        card.delete()
    
    return HttpResponseRedirect(reverse('main:show_main'))

def get_product_json(request):
    cards = Card.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', cards))

@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        power = request.POST.get("power")
        energy_cost = request.POST.get("energy_cost")
        description = request.POST.get("description")
        user = request.user

        new_product = Card(name=name, amount=amount, price=price, power=power, energy_cost=energy_cost, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def remove_product_ajax(request, id):
    try:
        product = Card.objects.get(pk=id)
        product.delete()
        return JsonResponse({'message': 'Product removed successfully'})
    except Card.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=404)

@csrf_exempt
def modify_quantity_ajax(request, id, symbol):
    try:
        product = Card.objects.get(pk=id)
        if symbol == "-" and product.amount > 0:
            product.amount -= 1
            product.save()
            return JsonResponse({'message': 'Decreament success'})
        
        elif symbol == "+" and product.amount > 0:
            product.amount += 1
            product.save()
            return JsonResponse({'message': 'Increament success'})
        
        else:
            raise Card.DoesNotExist
        
    except Card.DoesNotExist:
        return JsonResponse({'message': 'Card not found'}, status=404)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Card.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            power = int(data["power"]),
            energy_cost = int(data["energy_cost"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    


