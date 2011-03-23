# -*- coding: utf-8 -*-
#
# Curso de Python
# ---------------
# Demonstrações de Aula
#
__author__ = "Sérgio Almeida Dias"
__date__ = "2011-02-20"
__copyright__ = "Copyright 2011, Sérgio Almeida Dias"

def foo(param):
    param += 2
    return param

def foo2(x, y, z = 0):
    return x+y+z

def foo3(a=1,b=2,c=3):
    return foo2(a,b,c)
    
#--- exemplos de chamada ---
print foo3(b=3, a=foo2(4,foo(1)))
print foo2(*[12,4,6])
print foo3(**{'a':2,'b':10})

#--- exemplo de escopo de variáveis
print
print 'Escopo de variaveis'
xkx = '123'
def f1(a):
    xkx = a
    print 'em f1 xkx=',xkx

def f2(a):
    global xkx
    xkx = a
    print 'em f2 xkx=',xkx

f1(10)
print '      depois xkx=',xkx
f2(20)
print '      depois xkx=',xkx

class MinhaClasse(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def foo(self,x):
        return x*self.a
    
class MinhaOutra(object):
    def foo2(self,x):
        return self.a + x
    
class MinhaSegunda(MinhaClasse):
    def foo(self,x):
        return x*self.b # Note que self.b não existe

class MinhaComposta(MinhaClasse, MinhaOutra):
    pass
    
print
print 'Classes'
a = MinhaClasse(10,20)
b = MinhaSegunda(100,200)
c = MinhaComposta(8,9)
d = MinhaOutra()

print a.foo(10)
print b.foo(3)
print c.foo(2)
print c.foo2(10)
try:
    print d.foo2(20)
except AttributeError,e:
    print e
    