# -*- coding: utf-8 -*-
#
# Curso de Python
# ---------------
# Demonstrações de Aula
#
__author__ = "Sérgio Almeida Dias"
__date__ = "2011-02-20"
__copyright__ = "Copyright 2011, Sérgio Almeida Dias"

#
## Motra como é a tipagem
#
print 'Demonstracao basica de tipagem dinamica'
print """a = 1
b = '2'
c = 3
d = '4'
"""

a = 1
b = '2'
c = 3
d = '4'

try:
    print 'a+c', a+c   #ok
    print 'b+d', b+d
    c = '3' # ok, c agora tem um string
    print 'b+c (novo c)', b+c
    print 'a+int(b)', a+int(b)
    print 'a+b',a+b   # erro

except TypeError, e:
    print '***'
    print e

#
## Constantes como objetos
#
print 
print "Todos os tipos são objetos (inclusive constantes)"

csv = '34,"banana",23,14'
lista = csv.split(',')
print lista

lista = '14.2,15,16.1'.split(',')
print lista

print ','.join(['1','2','5','9'])
x = ' ama '.join(['joao','maria','rosana','pedro'])
print x
print x.split(' ama ')