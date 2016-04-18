#!/usr/bin/env python

"""
Esse é um exemplo de um
comentário multilinha
"""

balance = 200 # saldo de 200 reais
quantity = 50 # quero sacar 50

# verifica se existe dinheiro suficiente
if balance >= quantity:
    balance = balance - quantity
    print('Saldo atual: %d' % balance)
else:
    print('Saldo insuficiente!')

"Fim do arquivo"
