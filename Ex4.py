def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    iteracoes = 0
    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio, iteracoes
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, iteracoes

def busca_linear(lista, alvo):
    iteracoes = 0
    for i, valor in enumerate(lista):
        iteracoes += 1
        if valor == alvo:
            return i, iteracoes
    return -1, iteracoes

lista = list(range(1, 100001))
lista_isbn = [1, 5, 10, 100, 1000, 5000, 10000, 25000, 50000, 75000, 100000]
for isbn in lista_isbn:
    pos_bin, it_bin = busca_binaria(lista, isbn)
    pos_lin, it_lin = busca_linear(lista, isbn)
    print("Busca binária - ISBN:", isbn, "Posição:", pos_bin, "Iterações:", it_bin)
    print("Busca linear - ISBN:", isbn, "Posição:", pos_lin, "Iterações:", it_lin)
