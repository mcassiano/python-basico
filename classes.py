#!/usr/bin/python

class Student:

	def __init__(self, idty, name, dept = 'CS'):
		self.idty = idty
		self.dept = dept
		self.name = name

	def study(self):
		print('Procrastina...')
		print('Procrastina...')
		print('TEM PROVA AMANHÃ 😱😱😱')
		print('Vê vídeo de gatinhos... 🙀')
		print('6 da manhã: ok vou estudar')

	def think(self):
		print('http://google.com')
		print('como fazer <qualquer coisa> pesquisar')
		print('hm, faz sentido')

me = Student(111, "Matheus")
print(me.name)
print(me.idty)
print()
me.study()
print()
me.think()
