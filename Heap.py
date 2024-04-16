import math
import time
import random


def makeheap(heap):
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, n, i)


def heapify(heap, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] > heap[largest]:
        largest = left

    if right < n and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, n, largest)


def insertheap(heap, value):
    heap.append(value)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] < heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break


def removeheap(heap):
    if not heap:
        return None
    root = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    heapify(heap, len(heap), 0)
    return root


def sqrt_sort_quadratico(vetor):
    n = len(vetor)
    k = math.floor(math.sqrt(n))
    vetor_ordenado = []

    # Dividir o vetor em partes e criar um heap para cada parte
    partes = [vetor[i:i+k] for i in range(0, n, k)]
    for parte in partes:
        
        makeheap(parte)

    while any(partes):
        # Encontrar o maior elemento de cada parte e comparar com o heap
        maior_global = [-1]
        makeheap(maior_global)
        indice_global = None
        #print(partes)
        for i, parte in enumerate(partes):
            if parte:
                if parte[0] > maior_global[0]:
                    maior_global = [parte[0]]
                    indice_global = i
                    

        if indice_global is not None:
            vetor_ordenado.insert(0, removeheap(partes[indice_global]))

    return vetor_ordenado


def main():

    n = random.randint(100, 100)

    vetor = [random.randint(1, 100) for _ in range(n)]

    #print("Vetor original:", vetor)
    start_time = time.time()
    tempos_execucao = []
    for _ in range(3):
        vetor_ordenado_quadratico = sqrt_sort_quadratico(vetor.copy())
        tempo_execucao = time.time() - start_time
        tempos_execucao.append(tempo_execucao)

    media_tempo = sum(tempos_execucao) / len(tempos_execucao)
    print("Média do tempo de execução:", media_tempo)
    #print("Vetor ordenado (método quadrático):", vetor_ordenado_quadratico)


if __name__ == "__main__":
    main()
