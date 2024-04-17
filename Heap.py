import math
import time
import random
import heapq  # Importando a biblioteca para trabalhar com heaps

def sqrt_sort_max_heap(vetor):
    """
    Args:
        vetor (list): O vetor a ser ordenado.

    Returns:
        list: O vetor ordenado.
    """

    n = len(vetor)
    k = math.floor(math.sqrt(n))
    partes = []
    vetor_ordenado = []
    max_heaps = []

    # Dividir o vetor em partes e criar um max heap para cada parte
    for i in range(0, n, k):
        fim_parte = min(i + k, n)
        parte = vetor[i:fim_parte]
        heapq._heapify_max(parte)  # Transforma a parte em um max heap
        partes.append(parte)
        max_heaps.append(parte[0])  # Adiciona o maior elemento da max heap à lista de max heaps
        #print(partes)
    heapq._heapify_max(max_heaps)  # Transforma a lista de max heaps em um max heap

    while max_heaps:
       
        maior_heap = heapq._heappop_max(max_heaps)  # Pega o maior elemento entre as max heaps
        for parte in partes:
            if parte and parte[0] == maior_heap:
                heapq._heappop_max(parte)  # Remove o maior elemento da max heap correspondente
                if parte:
                    heapq.heappush(max_heaps, parte[0])  # Re-heapify após a remoção
                    heapq._heapify_max(max_heaps)  # Transforma a lista de volta em um max heap
                break
        vetor_ordenado.append(maior_heap)  # Adiciona o maior elemento ao vetor ordenado

    return vetor_ordenado[::-1]  # Inverte o vetor para obter a ordenação correta

def main():
    """
    Função principal para demonstração do algoritmo de ordenação por max heap.
    """
    n = random.randint(1000000, 1000000)
    vetor = [random.randint(1, 100) for _ in range(n)]

    #print("Vetor original:", vetor)

    tempos_execucao = []
    for _ in range(1):
        start_time = time.time()
        vetor_ordenado_max_heap = sqrt_sort_max_heap(vetor)
        tempo_execucao = time.time() - start_time
        tempos_execucao.append(tempo_execucao)

    media_tempo = sum(tempos_execucao) / len(tempos_execucao)

    print("Média do tempo de execução:", media_tempo)
    #print("Vetor ordenado (método max heap):", vetor_ordenado_max_heap)

if __name__ == "__main__":
    main()
