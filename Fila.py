class Fila:
	def __init__(self):
		self.itens = []

	def is_empty(self):
		return len(self.itens) == 0

	def enqueue(self, item):
		self.itens.append(item)

	def dequeue(self):
		if self.is_empty():
			print("Erro: A fila está vazia")
			return None
		return self.itens.pop(0)

	def peek(self):
		if self.is_empty():
			print("Erro: A fila está vazia")
			return None
		return self.itens[0]

	def size(self):
		return len(self.itens)

	def display(self):
		if self.is_empty():
			print("A fila está vazia")
		else:
			print("Fila:", end=" ")
			for item in self.itens:
				print(item, end=" ")
				print()

	def copy(self):
		nova_fila = Fila()
		nova_fila.itens = self.itens[:]
		return nova_fila