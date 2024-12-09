def selection_sort(jogadores):
    n = len(jogadores)
    for i in range(n):
        menor_indice = i
        for j in range(i + 1, n):
            if jogadores[j]['pontuacao'] < jogadores[menor_indice]['pontuacao']:
                menor_indice = j

        jogadores[i], jogadores[menor_indice] = jogadores[menor_indice], jogadores[i]


jogadores = [
    {"nome": "Alice", "pontuacao": 50},
    {"nome": "Bob", "pontuacao": 20},
    {"nome": "Charlie", "pontuacao": 40},
]

selection_sort(jogadores)
print(jogadores)
