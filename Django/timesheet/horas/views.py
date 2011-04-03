# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from models import Lancamento, Atividade, Projeto, LancamentoForm
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

#from django.conf import settings

def lista(request):
    return HttpResponse("Lista horas")

def detalhe(request, lanc_id):
    return HttpResponse(u"Detalhe do lançamento %s" % lanc_id)

@login_required
def lanca(request, lanc_id = None):
    if lanc_id:
        lanc = get_object_or_404(Lancamento,pk=lanc_id)
    else:
        try:
            lanc = Lancamento.objects.get(status="A",usuario=request.user)
        except Lancamento.DoesNotExist:
            lanc = None
    return _atualiza_lancamento(request, request.user, lanc)

def _atualiza_lancamento(request, usuario, lanc):
    if request.method == "POST":
        lf = LancamentoForm(request.POST, instance=lanc)
        lanc = lf.save(commit=False)
        if not hasattr(lanc, 'usuario') or lanc.usuario is None:
            lanc.usuario = usuario
        if lanc.minutos == 0:
            lanc.status = Lancamento.ABERTO
        else:
            lanc.status = Lancamento.LANCADO
        lanc.save()
        return HttpResponseRedirect(reverse('horas.views.lanca'))
    else:
        lf = LancamentoForm(instance=lanc)
        return render_to_response('lanca.html', {'formulario':lf})
