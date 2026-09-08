import numpy as np
import time

def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

    
def fib_matrix(n):
    if n == 0:
        return 0
    else:
        m = np.array([[1, 1], [1, 0]]) 
        m_pot = np.linalg.matrix_power(m, n - 1)

        return m_pot[0][0]

#testes e medição do tempo
QTD_ENTRADAS = 10
AUMENTO = 5
n_inicial = 0

print("--- Medicao do tempo para Fibonacci Recursivo ---")
for i in range(QTD_ENTRADAS):
    n = n_inicial + i * AUMENTO
    inicio = time.time()
    resultado = fib_rec(n)
    fim = time.time()
    print(f"Fibonacci({n}) = {resultado}, Tempo: {fim - inicio:.6f} segundos")

print(" ")
print("--- Medicao do tempo para Fibonacci com Matriz ---")
for i in range(QTD_ENTRADAS):
    n = n_inicial + i * AUMENTO
    inicio = time.time()
    resultado = fib_matrix(n)
    fim = time.time()
    print(f"Fibonacci({n}) = {resultado}, Tempo: {fim - inicio:.6f} segundos")