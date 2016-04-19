#!/usr/bin/python

# lista de compras do usuário
shopping_list_dict = {
    'fruits': ['Maçã', 'Melancia', 'Banana'],
    'veggies': ['Alface', 'Brócolis', 'Espinafre'], # ...
}

print(shopping_list_dict)
print(shopping_list_dict['fruits'])

# tá, mas strings gastam espaço
# e não legal repetir sempre

# dicionário com códigos e produtos do supermercado
products = {
    111: 'Maçã',
    200: 'Banana',
    310: 'Melancia', #...
}

# dicionário com preços dos produtos
prices = {
    111: 0.5,
    200: 1.0,
    310: 6.0, #...
}

# carrinho de compras do supermercado
shopping_cart = [(111, 5), (200, 12), (310, 1)]


def mult(x):
	return prices[x[0]]*x[1]

total = list(map(mult, shopping_cart))
print(total)
total = sum(total)
print(total)

# é possível fazer com labda, e com for
# simples e compreensão de listas