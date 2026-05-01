# Desafio Backend

Solução para os exercícios de algoritmia e programação concorrente.

---

## Exercício 1 — Maior Padrão Repetido

Identificar o maior padrão com pelo menos uma repetição (sem sobreposição) num array de inteiros.

### A Solução

Para evitar abordagens ineficientes de *brute force* (O(n³)), implementei o algoritmo usando **Programação Dinâmica**. A matriz `dp[i][j]` guarda o comprimento do padrão comum que termina nas posições `i` e `j`. A condição `(j - i) > dp[i-1][j-1]` garante que os dois padrões nunca partilham as mesmas posições.

- **Complexidade de Tempo:** O(n²)
- **Complexidade de Espaço:** O(n²)

### Como correr

```bash
# Testes unitários (exemplos do PDF + edge cases)
python exercicio1/teste.py

# Demonstração com o exemplo base do PDF
python exercicio1/main.py --demo

# Array aleatório de tamanho N (ex: 50 elementos)
python exercicio1/main.py --random 50
```

---

## Exercício 2 — Produtor-Consumidor com ficheiro CSV

Programa concorrente que lê um ficheiro de eventos de controlo de acessos, processa as linhas em paralelo e exporta os registos ordenados por data para JSON.

### A Solução

Implementado com o modelo **produtor-consumidor** usando `threading` e `queue.Queue` para comunicação entre threads.

- O **produtor** lê uma linha do ficheiro a cada intervalo aleatório entre 100ms e 500ms, linha a linha sem carregar o ficheiro todo para memória
- O **consumidor** recebe cada linha, simula um tempo de processamento entre 100ms e 200ms, extrai `timestamp`, `values` e `comment`, e acumula os registos
- No final, os registos são ordenados por timestamp (ascendente) e exportados para `output.json`
- A comunicação usa um **sentinel pattern** (`DONE = object()`) para sinalizar ao consumidor que o produtor terminou

### Como correr

```bash
# Correr o programa (gera output.json na pasta exercicio2/)
python exercicio2/main.py

# Testes unitários
python exercicio2/teste.py
```

### Formato do input

- `timestamp` — sempre o primeiro campo (`YYYY-MM-DD-HH-MM`)
- `values` — campos numéricos a seguir ao timestamp (opcional)
- `comment` — string no final da linha (opcional)

### Formato do output

```json
[
  {
    "timestamp": "2026-04-01-08-05",
    "values": [0.3, 1.2, -0.5],
    "comment": "O António abriu a porta"
  }
]
```