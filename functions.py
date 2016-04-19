#!/usr/bin/python

legal_drinking_age = {
	'Brazil': 18,
	'USA': 21
}

def even(n):
	return (n % 2) == 0

def can_drink(age, country):
	return age >= legal_drinking_age[country]

print(even(3))
print(even(6))
print(can_drink(18, 'Brazil'))
print(can_drink(18, 'USA'))
