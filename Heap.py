import math
import random
import time
import heapq as fila_prioridade

def ordenacao_raiz_quadrada_heap(vetor):
    """
    Ordena o vetor usando a técnica de ordenação por raiz quadrada com heap.
    """
    tamanho_vetor = len(vetor)
    tamanho_parte = int(math.sqrt(tamanho_vetor))

    # Dividir o vetor em partes
    partes = [vetor[i:i+tamanho_parte] for i in range(0, tamanho_vetor, tamanho_parte)]

    # Transformar cada parte em um Max Heap
    for i in range(len(partes)):
        fila_prioridade._heapify_max(partes[i])

    vetor_ordenado = []
    while any(partes):
        # Encontrar o maior elemento de cada parte
        maiores_elementos = [parte[0] for parte in partes if parte]

        # Pegar o maior elemento entre e1 . . . ek e inseri-lo no vetor solução
        maior = max(maiores_elementos)
        vetor_ordenado.append(maior)

        print(partes)
        # Descartar o maior elemento da parte correspondente
        for parte in partes:
            if parte and parte[0] == maior:
                fila_prioridade._heappop_max(parte)
                break

    return vetor_ordenado[::-1]

# Gerar vetor de tamanho n com números aleatórios
tamanho_vetor = random.randint(10000, 99999)
numeros = [random.randint(0, 2147483647) for _ in range(tamanho_vetor)]

# Medir o tempo de execução
inicio = time.time()
numeros_ordenados = ordenacao_raiz_quadrada_heap(numeros)
fim = time.time()

print("Vetor original:", numeros)
print("Vetor ordenado:", numeros_ordenados)
print("Tempo de execução:", fim - inicio, "segundos")
