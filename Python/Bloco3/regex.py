#-*- coding: UTF-8 -*-
import re

entrada = '''The quick brown fox jumps over the lazy dog'''

r = re.findall('(?<!\S)\S{3}(?!\S)',entrada, flags=re.IGNORECASE)
print '-- findall --'
print r

entrada = '''Sergio,38,SP'''


r = re.sub('^(\w+)\,(\d+)\,(\w+)','xxx\0\1\2\3\4\5\6',entrada)
print
print 'find:',re.findall('^(\w+)\,(\d+)\,(\w+)',entrada)
print '--- in ---'
print entrada
print '--- out ---'
print r
