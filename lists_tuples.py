#!/usr/bin/python

shopping_list = ['Maçã', 'Arroz', 'Feijão', 'Carne']
print(shopping_list)
print(shopping_list[0])
print('Quantos itens na minha lista? R: %d' % len(shopping_list))

# Esqueci o leite E o leite condensado!
shopping_list.append('Leite')
shopping_list.append('Leite condensado')
print(shopping_list)

# Ok, preciso de colocar em lista alfabética
# (não sei porquê)
shopping_list.sort()

print(shopping_list)

# Ok, mas qual a quantidade?
item_qnty = (2, 0.5, 1, 2, 3, 0.8)
# não consigo alterar o valor de uma tupla
# item_qnts[0] = 1
item_qnty = list(zip(shopping_list, item_qnty))

print(item_qnty)

