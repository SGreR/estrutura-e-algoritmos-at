import time
import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

for tamanho in [1000, 10000]:
    lista = random.sample(range(100000), tamanho)
    inicio = time.time()
    bubble_sort(lista)
    fim = time.time()
    print(f"Tamanho: {tamanho}, Tempo: {fim - inicio:.2f}s")
