from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275380',
        'name': 'Cahya Bagus Gautama Gozales ',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)