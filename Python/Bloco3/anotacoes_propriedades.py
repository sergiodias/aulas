#!/usr/bin/python
#-*- coding: UTF-8 -*-

class dec_c(object):
    """Demonstra como implementar uma classe de decoração
    """

    def __init__(self, f):
        print 'dec_c.__init__'
        self.func = f

    def __call__(self, *argv, **kwarg):
        print 'pre-dec_c'
        self.func(*argv, **kwarg)
        
def dec_f(func):
    """Demonstra como implementar uma função de decoração
    """

    def my_func(*argv, **kwarg):
        print 'pre-dec_f'
        func(*argv, **kwarg)
        print 'pos-dec_f'
    # Caso especial: mudo o nome da função para ninguém cair do cavalo
    my_func.__name__ = func.__name__
    return my_func

@dec_f
def foo(x,y = 10):
    print 'foo(%s, %s)' % (x,y)

@dec_f
def foo2():
    print 'foo2()'

@dec_c
def foo3(x,y = 10):
    print 'foo3(%s, %s)' % (x,y)

print 'Testes com decorações'
foo(1,2)
print '--'
foo(22)
print '--'
print 'foo.__name__',foo.__name__
print '--'
foo2()
print '--'
foo3(11,33)
foo3(5,7)
print '--'
print type(foo3)
try:
    print 'foo3.__name__:',foo3.__name__
except AttributeError, e:
    print '   ***** ',e,'*****'

class Velocimetro(object):
    CONVERTE = 1.609344
    def __init__(self, metrico=True):
        """Se metrico is not True, assume milhas"""
        self._v = 0
        self._metrico = metrico

    @property
    def metrico(self):
        return self._metrico
    
    def get_v(self):
        return self._v
    
    def set_v(self, novo):
        if not self.metrico:
            self._v = novo * self.CONVERTE
        else:
            self._v = novo
    
    velocidade = property(fget=get_v, fset=set_v, doc='Eu sou a propriedade velocidade')

print
print 'Testes de Propriedades'
print
v = Velocimetro()
v.velocidade = 100
print v.velocidade
print 'metrico:',v.metrico
print
v = Velocimetro(False)
v.velocidade = 55
print v.velocidade
print 'metrico:',v.metrico


