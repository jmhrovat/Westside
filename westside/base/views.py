from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def preschool(request):
    return render(request, 'preschool/index.html')

def elementary(request):
    return render(request, 'base/elementary.html')

def pricing(request):
    return render(request, 'base/pricing.html')
