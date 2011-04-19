#-*- coding: UTF-8 -*-

class Animal(object):
    def __init__(self):
        self.pernas = 4
        

tom = Animal()
# Copia por referência
bob = tom
bob.patas = 3
print 'Patas do tom',tom.patas
print 'Patas do bob',bob.patas 

import copy
rock = copy.copy(bob)
rock.patas = 4
print 'Patas do bob',bob.patas 
print 'Patas do Rock',rock.patas

lista = [1,2,3,4,5]
copia = lista
clone = list(lista)
copia.append(99)
print 'Lista original:',lista
print 'Copia da Lista:',copia
print 'Clone da Lista:',clone
    