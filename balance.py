#!/usr/bin/env python

balance = 200 # saldo de 200 reais
quantity = 50 # quero sacar 50

# verifica se existe dinheiro suficiente
if balance >= quantity:
balance = balance - quantity
else:
print('Saldo insuficiente!')
