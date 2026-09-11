import numpy as np
import time
import matplotlib.pyplot as plt

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
tempos_matriz = []
tempos_recursivo = []

print("--- Medicao do tempo para Fibonacci Recursivo ---")
for i in range(QTD_ENTRADAS):
    n = n_inicial + i * AUMENTO
    inicio = time.perf_counter()
    resultado = fib_rec(n)
    fim = time.perf_counter()
    tempo = (fim - inicio) * 1000 #converte para milisegundos
    
    tempos_recursivo.append(tempo) 
    print(f"Fibonacci({n}) = {resultado}, Tempo: {tempo:.6f} milisegundos")

print(" ")
print("--- Medicao do tempo para Fibonacci com Matriz ---")
for i in range(QTD_ENTRADAS):
    n = n_inicial + i * AUMENTO
    inicio = time.perf_counter()
    resultado = fib_matrix(n)
    fim = time.perf_counter()
    tempo = (fim - inicio) * 1000 #converte para milisegundos
    tempos_matriz.append(tempo)
    print(f"Fibonacci({n}) = {resultado}, Tempo: {tempo:.6f} milisegundos")


#--- DESENHANDO GRÁFICOS ---
plt.figure(figsize=(10, 6))

# Valores do eixo x
valores_n = np.arange(n_inicial, n_inicial + QTD_ENTRADAS * AUMENTO, AUMENTO)
valores_n_seguro = np.clip(valores_n, 1e-9, None)  #Evita o zero no log

# Plotando os dados reais obtidos nos testes

plt.plot(valores_n, tempos_matriz, 'b-o', label='Fibonacci com Matriz (Tempo Real)', linewidth=2)
plt.plot(valores_n, tempos_recursivo, 'r-o', label='Fibonacci Recursivo (Tempo Real)', linewidth=2)


# GRÁFICO 1 - Tempo de execução × tamanho da entrada n --------------------------------

#Complexidades teóricas - Multiplicamos por constantes pequenas para fins de escala no mesmo eixo gráfico

complexidade_log = np.log2(valores_n_seguro) * 0.0001 
complexidade_exp = 2**valores_n * 0.00001

# Plotando as curvas teóricas de Notação Big-O

plt.plot(valores_n, complexidade_log, 'b--', label='Teórico: $O(\\log n)$', alpha=0.7)
plt.plot(valores_n, complexidade_exp, 'r--', label='Teórico: $O(2^n)$', alpha=0.7)
plt.title('Comparação entre Análise teórica e empírica')
plt.xlabel('Tamanho da Entrada (n) - Escala log Y')
plt.ylabel('Tempo de Execução (ms)')

# GRÁFICO 2 --------------------------------

#CALCULO DO NUMERO DE OPERAÇÕES 
'''
custo_matriz_log = np.log2(valores_n_seguro) # Custo teórico para Fibonacci com matriz
custo_recursivo_exp = 2.0**valores_n   # Custo teórico para Fibonacci recursivo
plt.plot(valores_n, custo_matriz_log, 'b-o', label='Fibonacci com Matriz (Tempo Real)', linewidth=2)
plt.plot(valores_n, custo_recursivo_exp, 'r-o', label='Fibonacci Recursivo (Tempo Real)', linewidth=2)
plt.xlabel('Tamanho da Entrada (n)')
plt.ylabel('Custo de crescimento teórico (número de operações)')
'''


# Configurações cruciais de escala e legendas
plt.yscale('log') # Escala Logarítmica para juntar O(log n) e O(2^n) perfeitamente
plt.title('Comparação entre Fibonnaci recursivo e com matriz')
plt.grid(True, which="both", linestyle='--', alpha=0.5)
plt.legend(loc='upper left')

# Exibe na janela 
plt.show()
