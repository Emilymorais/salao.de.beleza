from django.shortcuts import render, redirect
from salaoapp.forms import UsersForm
from salaoapp.models import Usuario
# Create your views here.

def home(request):
	tabela = Usuario.objects.all()
	return render(request,'home.html',{'usuario':tabela})

def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html',data)

def docad(request):
	form = UsersForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('cadastro')

def docad(request):
	form = UsersForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('cadastro')