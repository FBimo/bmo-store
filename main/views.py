from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'my_app': 'Marpellus Cenep',
        'name': 'FBmo',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)