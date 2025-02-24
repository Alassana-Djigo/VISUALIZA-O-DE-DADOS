from random import randint

class Die():

	"""Representa um unico dado"""
	def __init__(self,num_sides=6):
		"""Dados comuns de 6 lados"""
		self.num_sides = num_sides

	def roll(self):
		"""Devolve um valor aleatorio entre 1 e num_sides"""
		return randint(1,self.num_sides)
