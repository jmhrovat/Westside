from django.shortcuts import render

# Create your views here.

def index(request):

    nav_status = {
        'preschool': 'inactive',
        'elementary': 'inactive',
        'pricing': 'inactive',
        'church': 'inactive',
        'contact': 'inactive'
    }

    context = {
        'nav_status': nav_status
    }

    return render(request, 'base/index.html', context)

def contact(request):

    nav_status = {
        'preschool': 'inactive',
        'elementary': 'inactive',
        'pricing': 'inactive',
        'church': 'inactive',
        'contact': 'active'
    }

    context = {
        'nav_status': nav_status
    }

    return render(request, 'base/contact.html', context)

def preschool(request):

    nav_status = {
        'preschool': 'active',
        'elementary': 'inactive',
        'pricing': 'inactive',
        'church': 'inactive',
    }

    context = {
        'nav_status': nav_status,
        'body_class': 'body_secondary'
    }

    return render(request, 'base/preschool.html', context)

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

    nav_status = {
        'preschool': 'inactive',
        'elementary': 'inactive',
        'pricing': 'active',
        'church': 'inactive',
    }

    context = {
        'nav_status': nav_status,
        'body_class': 'body_secondary'
    }
    return render(request, 'base/pricing.html', context)

def church(request):
    nav_status = {
        'preschool': 'inactive',
        'elementary': 'inactive',
        'pricing': 'inactive',
        'church': 'active',
    }

    context = {
        'nav_status': nav_status,
        'body_class': 'body_secondary'
    }

    return render(request, 'base/church.html', context)
