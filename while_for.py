#!/usr/bin/python

age = 15

# é um while normal porém com sintaxe diferente
while age < 18:
	print('Não pode beber ainda. 🙄')
	age += 1

if age >= 18:
	print('Partiu Rosa!!! 😱')

# com o for é a mesma ideia, mas...
# precisamos usar range()

print('Zero a cinco:')

for i in range(0, 5):
	print(i)

print('Primeiros dez ímpares:')
for i in range(1, 10, 2):
	print(i)

print('Primeiros dez pares:')
for i in range(0, 10, 2):
	print(i)

# fors e whiles também funcionam
# com estruturas de dados

campi = ['Coração Eucarístico', 'São Gabriel', 'Barreiro', 'Contagem'] # ...
campi_copy = campi[:]

while campi_copy:
	print(campi_copy[0])
	del(campi_copy[0])
	#print(campi_copy.pop())

for campus in campi:
	print(campus)
