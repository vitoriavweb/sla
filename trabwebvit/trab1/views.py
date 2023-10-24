from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'trab1/index.html')

def index1(request):
	return render(request, 'trab1/index1.html')

listas = ['norte', 'nordeste', 'centro-oeste', 'sudeste', 'sul']
def index(request):
	return render(request, 'trab1/index.html',{
		'listas': listas
	})