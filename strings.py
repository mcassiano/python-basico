#!/usr/bin/python

first_name = 'Fulano' # nome
last_name = 'de Tal' # sobrenome

print(first_name)
print(last_name[0:2])
print(last_name[:2])
print(last_name[3:])

print(first_name + ' ' + last_name)
print(first_name, last_name)
print('%s, %s' % (last_name, first_name))
print('%s, %s' % (last_name.upper(), first_name)) # lower

# string com múltiplas linhas
print("""TEXTO COM MAIS DE UMA
LINHA E QUEM NINGUÉM VAI LER

OOPS""")
