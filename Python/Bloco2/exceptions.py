# -*- coding: utf-8 -*-
#
# Curso de Python
# ---------------
# Demonstrações de Aula
#
__author__ = "Sérgio Almeida Dias"
__date__ = "2011-02-20"
__copyright__ = "Copyright 2011, Sérgio Almeida Dias"

lista = [1,2,3]

print
print 'Excecao no bloco'

try:
    print 'lista[5]=',lista[5]
except IndexError,e:
    print '  *** Erro ***'
    print ' ',e
else:
    'Não houve erro'
finally:
    print 'Por aqui eu passo sempre'

print
print 'Agora sem erro'

try:
    print 'lista[2]=',lista[2]
except IndexError,e:
    print '*** Erro ***'
    print e
else:
    print '  Nao houve erro'
finally:
    print '  Por aqui eu passo sempre'

# Classe própria de exceção
#
print
print 'Exemplos com raise e classe propria de excecao'

class MinhaExcecao(Exception):
    """Minha Classe de exceção"""
    pass


try:
    try:
        # Nesse caso eu vou tratar o erro e seguir em frente
        a = lista[99]
    except IndexError, e:
        print e

    try:
        # Nesse eu trato o erro e lanço outra exceção
        
        a = 0
        b = 10
        c = b/a
    except ZeroDivisionError, e:
        print e
        m = MinhaExcecao(e)
        raise m
    print 'Continuando o bloco'     # Nunca passa aqui, por causa do raise

except MinhaExcecao, e:
    print 'MinhaExcecao'
    print e
