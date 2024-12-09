from BinaryTree import BinaryTree

tree = BinaryTree()
for nota in [85, 70, 95, 60, 75, 90, 100]:
    tree.add(nota)

print("Buscar 70:", tree.search(70))
