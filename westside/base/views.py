from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def preschool(request):
    return render(request, 'base/preschool.html')

def elementary(request):

    nav_status = {
        'preschool': 'inactive',
        'elementary': 'active',
        'pricing': 'inactive',
        'church': 'inactive',
    }

    context = {
        'nav_status': nav_status,
        'body_class': 'body_secondary'
    }

    return render(request, 'base/elementary.html', context)

def pricing(request):
    return render(request, 'base/pricing.html')

def church(request):
    return render(request, 'base/church.html')
