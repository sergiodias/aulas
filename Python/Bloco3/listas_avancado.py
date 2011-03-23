# -*- coding: utf-8 -*-
#
# Curso de Python
# ---------------
# Demonstrações de Aula
#
__author__ = "Sérgio Almeida Dias"
__date__ = "2011-02-28"
__copyright__ = "Copyright 2011, Sérgio Almeida Dias"


nomes = ['carlos','alfredo','fernanda','luciana', 'carla']
idades = [30,31,33,29]

class Pessoa(object):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return 'nome:%s; idade:%s;' %(self.nome,self.idade)
        
def f(x,y):
    return Pessoa(x,y)

r = map(f,nomes,idades)
for x in r:
    print x
print r

