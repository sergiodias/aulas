# -*- coding: utf-8 -*-
from horas.models import Projeto, Atividade, Lancamento
from django.contrib import admin

class ProjetoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nome', 'descricao']}),
        (u'Informações administrativas', {'fields': ['uri', 'data_inicio','data_termino','ativo']}),
    ]
    list_display = ('nome', 'descricao','ativo')

admin.site.register(Projeto, ProjetoAdmin)

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao','bugzilla_obrigatorio')

admin.site.register(Atividade, AtividadeAdmin)

admin.site.register(Lancamento)
