#!/usr/bin/python

class NotImplementedYet(Exception):
	def __init__(self):
		super(NotImplementedYet, self).__init__()

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

	def do_homework(self):
		raise NotImplementedYet

me = Student(111, "Matheus")
print(me.name)
print(me.idty)
print()
me.study()
print()
me.think()
print()

try:
	me.do_homework()
except:
	print('Ainda não aprendi a matéria...')
