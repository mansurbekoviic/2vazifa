from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def kurtua(request):
    return render(request, 'myapp/kurtua.html')

def carvajal(request):
    return render(request, 'myapp/carvajal.html')

def militao(request):
    return render(request, 'myapp/militao.html')

def ramos(request):
    return render(request, 'myapp/ramos.html')

def bellingham(request):
    return render(request, 'myapp/bellingham.html')

def camavinga(request):
    return render(request, 'myapp/camavinga.html')

def vinicius(request):
    return render(request, 'myapp/vinicius.html')

def valverde(request):
    return render(request, 'myapp/valverde.html')

def mbappe(request):
    return render(request, 'myapp/mbappe.html')

def modric(request):
    return render(request, 'myapp/modric.html')
