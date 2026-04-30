import argparse
import random
import time
from typing import List, Any

def encontrar_maior_padrao(arr: List[Any]) -> List[Any]:
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    max_length = 0
    best_end_index = 0
    
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Garante match e previne sobreposição validando a distância (j - i)
            if arr[i - 1] == arr[j - 1] and (j - i) > dp[i - 1][j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                
                # O > (estrito) garante que em caso de empate mantemos a 1ª ocorrência
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    best_end_index = i - 1 
            else:
                dp[i][j] = 0
                
    if max_length > 0:
        start_index = best_end_index - max_length + 1
        return arr[start_index : best_end_index + 1]
    
    return []

def run_demo():
    exemplo = [6, 2, 6, 8, 22, 0, 9, 5, 8, 22, 0, 9, 8, 1, 2, 4, 5, 6, 7]
    print("Executando demo...")
    print(f"Input:  {exemplo}")
    
    start_time = time.perf_counter()
    resultado = encontrar_maior_padrao(exemplo)
    end_time = time.perf_counter()
    
    exec_time_ms = (end_time - start_time) * 1000
    print(f"Output: {resultado}")
    print(f"Tempo de execução: {exec_time_ms:.4f} ms")

def run_random(size: int):
    # Gera array com pool reduzida (1 a 5) para forçar repetições
    arr = [random.randint(1, 5) for _ in range(size)]
    print(f"Array aleatório (size={size}):\n{arr}")
    
    start_time = time.perf_counter()
    res = encontrar_maior_padrao(arr)
    end_time = time.perf_counter()
    
    exec_time_ms = (end_time - start_time) * 1000
    print(f"Padrão: {res if res else 'Nenhum'}")
    print(f"Tempo de execução: {exec_time_ms:.4f} ms")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Desafio A - Padrão Repetido")
    parser.add_argument('--demo', action='store_true', help="Corre o array de exemplo")
    parser.add_argument('--random', type=int, metavar='N', help="Gera array aleatorio de tamanho N")
    
    args = parser.parse_args()
    
    if args.demo:
        run_demo()
    elif args.random:
        run_random(args.random)
    else:
        parser.print_help()