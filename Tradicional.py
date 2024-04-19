import math
import random
import time

def ordenacao_raiz_quadrada(vetor):
    """
    Ordena o vetor usando a técnica de ordenação por raiz quadrada.
    """
    tamanho_vetor = len(vetor)
    tamanho_parte = int(math.sqrt(tamanho_vetor))

    # Dividir o vetor em partes
    partes = [vetor[i:i+tamanho_parte] for i in range(0, tamanho_vetor, tamanho_parte)]

    # Ordenar cada parte
    for i in range(len(partes)):
        partes[i] = sorted(partes[i])

    vetor_ordenado = []
    while any(partes):
        # Encontrar o maior elemento de cada parte
        maiores_elementos = [parte[-1] for parte in partes if parte]

        # Pegar o maior elemento entre e1 . . . ek e inseri-lo no vetor solução
        maior = max(maiores_elementos)
        vetor_ordenado.append(maior)
        print(partes)
        # Descartar o maior elemento da parte correspondente
        for parte in partes:
            if parte and parte[-1] == maior:
                parte.pop()
                break
        
    return vetor_ordenado[::-1]

# Gerar vetor de tamanho n com números aleatórios
tamanho_vetor = random.randint(10000, 99999)
numeros = [random.randint(0, 2147483647) for _ in range(tamanho_vetor)]

# Medir o tempo de execução
inicio = time.time()
numeros_ordenados = ordenacao_raiz_quadrada(numeros)
fim = time.time()

print("Vetor original:", numeros)
print("Vetor ordenado:", numeros_ordenados)
print("Tempo de execução:", fim - inicio, "segundos")
