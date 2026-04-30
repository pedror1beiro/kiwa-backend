# Exercicio 1 - Maior Padrão Repetido

Solução para identificar o maior padrão com repetição (sem sobreposição) num array.

## A Solução
Para evitar abordagens ineficientes de *brute force* (O(n³)), implementei o algoritmo usando **Programação Dinâmica**. A lógica garante através de uma matriz que os índices dos padrões encontrados não se cruzam. 
* **Complexidade de Tempo:** O(n²)

## Como correr

A aplicação funciona via linha de comandos (CLI).

**Correr os testes unitários (exemplos do PDF + edge cases):**
```bash
python teste.py

Gerar um array aleatório e testar o algoritmo (Ex: 50 elementos):

python main.py --random 50

Correr a demonstração base do PDF:

python main.py --demo