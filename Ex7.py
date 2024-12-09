from Hashtable import HashTable

def verificar_duplicatas(lista):
    tabela_hash = HashTable()
    for elemento in lista:
        if tabela_hash.buscar(elemento) is not None:
            return True
        tabela_hash.inserir(elemento, True)
    return False

lista = [1, 2, 3, 4, 5, 1]
print(verificar_duplicatas(lista))

lista = [10, 20, 30, 40, 50]
print(verificar_duplicatas(lista))
