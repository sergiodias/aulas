# -*- coding: utf-8 -*-
#
# Curso de Python
# ---------------
# Demonstrações de Aula
#
__author__ = "Sérgio Almeida Dias"
__date__ = "2011-02-20"
__copyright__ = "Copyright 2011, Sérgio Almeida Dias"

lista = [1,7,3,9,5]
texto = 'python'

print 'lista=', lista
print 'texto=', texto

print "'c' in texto:", 'c' in texto
print "'k' not in texto", 'k' not in texto
print '3 in lista', 3 in lista

print

print 'texto: ',
for x in texto:
    print x,
print

print 'lista (reverse):',
lista.reverse()
for x in lista:
    print x,
print

print 'lista (sort):',
lista.sort()
for x in lista:
    print x,
print

print 'lista[4]=',lista[4]
try:
    print 'lista[5]=',lista[5]
except IndexError,e:
    print e
    
print 'lista[2:3]=',lista[2:3]
lista.append(12)
lista.append('a')
print 'lista: ', lista
del(lista [2])
print 'lista: ', lista

print
print 'Outras estruturas'
tupla = (1,2,4)
print 'tupla:',tupla

dicionario = {1:'um','dois': 2,(1,2):'um e dois'}
#dicionario = dict()
#dicionario[1] = 'um'
#dicionario['dois'] = 2
#dicionario[(1,2)] = 'um  e dois'
#dicionario[(2,3)] = [2,3]

print 'dicionario:', dicionario
print
print 'dicionario[1]=', dicionario[1]
print 'dicionario[(1,2)]=', dicionario[(1,2)]
print 'dicionario.get(99)', dicionario.get(99)
print 'dicionario.get(99)', dicionario.get(99,'noventa e nove')
try:
    print 'dicionario[99]', dicionario[99]
except KeyError,e:
    print 'KeyError'

for x in dicionario.keys():
    print x
