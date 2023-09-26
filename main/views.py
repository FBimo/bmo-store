import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import Card
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


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
        'last_login': request.COOKIES['last_login']
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
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
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


#def increase_card(request):
