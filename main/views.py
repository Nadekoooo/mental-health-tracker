from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306241676',
        'name': 'Christian Yudistira Hermawan',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)