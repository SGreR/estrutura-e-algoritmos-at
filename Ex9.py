import timeit
from Hashtable import HashTable

usuarios = HashTable()

usuarios_data = [
    ("joaosilva", {"nome": "João Silva", "idade": 30}),
    ("mariacruz", {"nome": "Maria Cruz", "idade": 25}),
    ("pedrosantos", {"nome": "Pedro Santos", "idade": 40}),
    ("anabeatriz", {"nome": "Ana Beatriz", "idade": 22}),
    ("lucaspires", {"nome": "Lucas Pires", "idade": 35}),
    ("fernandasoares", {"nome": "Fernanda Soares", "idade": 28}),
    ("carlosoliveira", {"nome": "Carlos Oliveira", "idade": 33}),
    ("sofiamendes", {"nome": "Sofia Mendes", "idade": 26}),
    ("eduardocosta", {"nome": "Eduardo Costa", "idade": 31}),
    ("juliagomes", {"nome": "Júlia Gomes", "idade": 29}),
]

for chave, valor in usuarios_data:
    usuarios.inserir(chave, valor)

def busca_linear(lista, chave):
    for usuario in lista:
        if usuario[0] == chave:
            return usuario[1]
    return None

def teste_hash():
    return usuarios.buscar("juliagomes")

def teste_linear():
    return busca_linear(usuarios_data, "juliagomes")

tempo_hash = timeit.timeit(teste_hash, number=10000)
tempo_linear = timeit.timeit(teste_linear, number=10000)

print(f"Tempo da busca na hashtable: {tempo_hash:.8f} segundos (para 10.000 execuções)")
print(f"Tempo da busca linear: {tempo_linear:.8f} segundos (para 10.000 execuções)")
