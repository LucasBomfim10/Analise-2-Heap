import math
import time
import random



def sqrt_sort_quadratico(vetor):
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
    maior_global = -1
    indice_global = [0, 0]

    # Dividir o vetor em partes
    for i in range(0, n, k):
        fim_parte = min(i + k, n)
        if i + k >= n:  
            fim_parte = n
        partes.append(vetor[i:fim_parte])
        sorted(partes[-1])  # ordena as partes
        


    #print(partes)
    while any(partes):
        # Encontrar o maior elemento de cada parte e comparar com o maior global
        maior_global = float('-inf')  # Inicializar o maior global
        for i, parte in enumerate(partes):
            if parte:  # Verificar se a parte não está vazia
                maior_parte = parte[-1]  # Pega o maior elemento da parte atual
                if maior_parte > maior_global:
                    maior_global = maior_parte
                    # Atualiza o índice global
                    indice_global = [i, len(parte) - 1]

        if partes[indice_global[0]]:  # Verificar se a parte não está vazia
            vetor_ordenado.insert(
                0, partes[indice_global[0]].pop(indice_global[1]))
        #print(partes)
        #print(vetor_ordenado)

    return vetor_ordenado


def main():
    """
    Função principal para demonstração do algoritmo de ordenação por seleção de raiz quadrada.
    """
    n = random.randint(1000, 1000)

    vetor = [random.randint(1, 100) for _ in range(n)]

    #print("Vetor original:", vetor)


    tempos_execucao = []
    for _ in range(1):
      start_time = time.time()
      vetor_ordenado_quadratico = sqrt_sort_quadratico(vetor)
      tempo_execucao = time.time() - start_time
      tempos_execucao.append(tempo_execucao)

    media_tempo = sum(tempos_execucao) / len(tempos_execucao)

    print("Média do tempo de execução:", media_tempo)
    #print("Vetor ordenado (método quadrático):", vetor_ordenado_quadratico)


if __name__ == "__main__":

    main()
