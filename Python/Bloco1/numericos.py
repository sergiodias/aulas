# -*- coding: utf-8 -*-
#
# Curso de Python
# ---------------
# Demonstra��es de Aula
#
__author__ = "S�rgio Almeida Dias"
__date__ = "2011-02-20"
__copyright__ = "Copyright 2011, S�rgio Almeida Dias"

#
## Tipos num�ricos
#
a = 2
b = 2.5
c = 3.0
d = 2L
e = 7.0
f = '3'
# o resultado � sempre promovido para o tipo maior
print
print 'Tipos numericos'
print 'a=%s, b=%s, c=%s, d (L)=%s, e=%s, f=%s' % (a, b, c, d, e, f)
print
print 'a * b=',a*b
print 'c ** a=',c**a
print 'a ** c=',a**c
print 'a * d=',a*d
print 'e / a=',e/a
print 'e // a=',e//a
print 'e % a=',e%a

print 'a and b=', a and b
print 'a or b=',a or b
print 'e > f',e > f
print 'e < f',e < f