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
## Demonstração de código dinamicamente alterado
#

def par_ou_impar():
    """
    Função para perguntar para o usuário se ele quer um número par ou impar.
    
    Retorna 0 ou 1 (para par e ímpar)
    """
    while True:
        resp = raw_input('Par ou impar (digite 0 ou 1): ')
        if resp not in ['0', '1']:
            print '0 ou 1'
            continue
        return int(resp)

num = par_ou_impar()
print
print 'resposta:',
if num:
    def numero():
        return 5
else:
    def numero():
        return 2
    
print numero()
