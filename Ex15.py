from BinaryTree import BinaryTree

tree = BinaryTree()

notas = [85, 70, 95, 60, 75, 90, 100]
for nota in notas:
    tree.add(nota)

min_node = tree._get_min(tree.root)
max_node = tree._get_max(tree.root)

print("Nota mínima:", min_node.value)
print("Nota máxima:", max_node.value)