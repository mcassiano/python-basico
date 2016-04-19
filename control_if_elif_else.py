#!/usr/bin/python

"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
ou "Valor Inválido!", conforme o caso.
"""

time_period = input('Insira código: ')

if time_period == 'M':
	print('Bom dia!')
elif time_period == 'V':
	print('Boa tarde!')
elif time_period == 'N':
	print('Boa noite!')
else:
	print('Valor inválido')