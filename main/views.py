from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'my_app': 'Bmo Store',
        'name': 'FBmo',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)