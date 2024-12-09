from BinaryTree import BinaryTree

tree = BinaryTree()

produtos = [45, 25, 65, 20, 30, 60, 70]
for produto in produtos:
    tree.add(produto)

print("Árvore em ordem antes da remoção:", tree.inorder())

tree.remove(20)
print("Árvore em ordem após remover 20 (nó folha):", tree.inorder())

tree.remove(25)
print("Árvore em ordem após remover 25 (nó com um filho):", tree.inorder())

tree.remove(45)
print("Árvore em ordem após remover 45 (nó com dois filhos):", tree.inorder())
