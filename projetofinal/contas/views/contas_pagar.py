from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from ..models import ContasPagar
from ..forms.contaspagar_form import ContasPagarForm

@csrf_exempt
@require_http_methods(["GET"])
def home(request):
	return render(request, 'contas/home.html')

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	data = {}
	data['listaContas'] = ContasPagar.objects.all()

	return render(request, 'contas/contasPagarRead.html', data)

def cadastrar(request):
    data = {}
    form = ContasPagarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_pagamento')

    data['operacao'] = 'Cadastro de Contas a Pagar'
    data['form'] = form
    return render(request, 'contas/contasPagarCreateUpdate.html', data)

# def detalhar(request, id_pessoa):
# 	pessoa = Pessoa.objects.get(id=id_pessoa)
# 	return HttpResponse(f"Detalhou {pessoa.nome} (id={pessoa.id})")

# def excluir(request, id_pessoa):
# 	try:
# 		pessoa = Pessoa.objects.get(id=id_pessoa)
# 		pessoa.delete()		
# 		return HttpResponse(f"Excluiu {pessoa.nome} (id={pessoa.id})")
# 	except ObjectDoesNotExist:
# 		return HttpResponse("Pessoa não encontrada")

