# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils.translation import ugettext as _

STATUS_LANCAMENTO = ((u'A',_(u'Aberto')), (u'C',_(u'Conferido')), (u'L',_(u'Lançado'))
                     )

class Projeto(models.Model):
    nome =  models.CharField(max_length=40)
    descricao =  models.CharField(_(u'descrição'),max_length=200)
    uri =  models.CharField(max_length=200)
    data_inicio =  models.DateField(_(u'data de início'))
    data_termino = models.DateField(_(u'data de término'), null = True, blank = True)
    ativo = models.BooleanField()
    def __unicode__(self):
        return self.nome

class Atividade(models.Model):
    nome = models.CharField(max_length=20)
    descricao =  models.CharField(_(u'descrição'),max_length=200)
    bugzilla_obrigatorio = models.BooleanField(_(u'obrigatório bugzilla'))
    def __unicode__(self):
        return self.nome

class Lancamento(models.Model):
    ABERTO = 'A'
    CONFERIDO = 'C'
    LANCADO = 'L'
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, verbose_name=_(u'usuário'))
    projeto = models.ForeignKey(Projeto)
    atividade = models.ForeignKey(Atividade)
    descricao =  models.CharField(_(u'descrição'),max_length=200)
    data = models.DateField(default=date.today())
    hora_inicial = models.TimeField(default=datetime.now().time())
    minutos = models.IntegerField(default=0)
    status = models.CharField(_(u'situação'),max_length=1,choices=STATUS_LANCAMENTO, default='A')
    bugzilla = models.IntegerField(_(u'número do bug'),blank = True, default = 0)
    class Meta:
        verbose_name_plural = _(u'lançamentos')
        verbose_name = _(u'lançamento')
    def __unicode__(self):
        return '%s %s %s' % (self.usuario,self.data,self.hora_inicial)

class LancamentoForm(ModelForm):
    class Meta:
        model = Lancamento
        exclude = ('usuario','status')
