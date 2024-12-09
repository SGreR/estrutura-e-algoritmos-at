class Pilha:
	def __init__(self):
		self.itens = []

	def is_empty(self):
		return len(self.itens) == 0

	def push(self, item):
		self.itens.append(item)

	def pop(self):
		if not self.is_empty():
			return self.itens.pop()
		else:
			return "A pilha está vazia"

	def peek(self):
		if not self.is_empty():
			return self.itens[-1]
		else:
			return "A pilha está vazia"

	def size(self):
		return len(self.itens)

	def display(self):
		print("Pilha:", self.itens)

	def copy(self):
		nova_pilha = Pilha()
		nova_pilha.itens = self.itens[:]
		return nova_pilha
