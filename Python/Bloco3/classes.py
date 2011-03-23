#-*- coding: UTF-8 -*-

class Movel(object):
    def __init__(self):
        print '*Contrutor de Movel'
    def limpeza(self):
        return u'Não faz nada'

# Atributos de Classe e Atributos de objeto (instância)
class Cadeira(Movel):
    revestimento = 'madeira'
    pernas = 4
    almofada = 'nao'
    def __init__(self):
        Movel.__init__(self)
        print '**Contrutor de Cadeira'

    def limpeza(self):
        return u'Pano com água'

banco = Cadeira()
cadeira = Cadeira()

print 'Cadeira.pernas:', Cadeira.pernas
print 'banco.pernas:', banco.pernas
print 'cadeira.pernas:', cadeira.pernas
print 'Movel.pernas:', hasattr(Movel, 'pernas') and Movel.pernas

# agora 'pernas' é uma variável da instância 'banco'
print
print "banco.pernas = 3"
banco.pernas = 3
print 'Cadeira.pernas:', Cadeira.pernas
print 'banco.pernas:', banco.pernas
print 'cadeira.pernas:', cadeira.pernas

# Modificando objeto no objeto
print
print "cadeira.revestimento = 'tecido'"
cadeira.revestimento = 'tecido'
print 'Cadeira tem revestimento', hasattr(Cadeira, 'revestimento') and Cadeira.revestimento
print 'banco tem revestimento', hasattr(banco, 'revestimento') and banco.revestimento
print 'cadeira tem revestimento', hasattr(cadeira, 'revestimento') and cadeira.revestimento

# modificando uma classe
print
print 'Atribuindo revestimento em Cadeira'
Cadeira.revestimento = 'Pintura'
print 'Cadeira tem revestimento', hasattr(Cadeira, 'revestimento') and Cadeira.revestimento
print 'banco tem revestimento', hasattr(banco, 'revestimento') and banco.revestimento
print 'cadeira tem revestimento', hasattr(cadeira, 'revestimento') and cadeira.revestimento


class Estofado(Movel):
    almofada = 'sim'
    def __init__(self):
        print '**Contrutor de Estofado'
    def limpeza(self):
        return u'Aspirador'

class Poltrona(Cadeira, Estofado):
    revestimento = 'couro'
    def __init__(self):
        print '***Contrutor de Poltrona'

print
print u'--- Múltipla herança ---'
p = Poltrona()
print u'Limpeza: ', p.limpeza()
print u'Almofada:', p.almofada

class Poltroninha(Estofado, Cadeira):
    revestimento = 'tecido'
    def __init__(self):
        print '***Contrutor de Poltroninha'

print
print u'--- Múltipla herança (2) ---'
p = Poltroninha()
print u'Limpeza: ', p.limpeza()
print u'Almofada:', p.almofada
