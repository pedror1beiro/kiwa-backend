import threading
import queue
import time
import random
import json
from datetime import datetime

fila = queue.Queue()
registos = []
registos_lock = threading.Lock()

# Sentinel para sinalizar ao consumidor que o produtor terminou
DONE = object()


def parse_linha(linha: str) -> dict:
    linha = linha.strip()
    if not (linha.startswith('[') and linha.endswith(']')):
        return None

    campos = [c.strip() for c in linha[1:-1].split(',')]
    if not campos:
        return None

    timestamp = campos[0]
    values = []
    comment_parts = []
    encontrou_texto = False

    # Percorre os campos após o timestamp:
    # tenta converter para float — se falhar, é início do comentário
    for campo in campos[1:]:
        if encontrou_texto:
            comment_parts.append(campo)
            continue
        try:
            values.append(float(campo))
        except ValueError:
            encontrou_texto = True
            comment_parts.append(campo)

    return {
        "timestamp": timestamp,
        "values": values if values else None,
        "comment": ', '.join(comment_parts) if comment_parts else None
    }


def normalizar_timestamp(ts: str) -> datetime:
    # Normaliza campos sem zero à esquerda antes de fazer parse
    partes = [p.zfill(2) for p in ts.split('-')]
    partes[0] = partes[0].zfill(4)
    return datetime.strptime('-'.join(partes), '%Y-%m-%d-%H-%M')


def produtor(caminho: str):
    with open(caminho, 'r', encoding='utf-8') as f:
        linhas = [l.strip() for l in f if l.strip()]

    for linha in linhas:
        time.sleep(random.uniform(0.1, 0.5))
        print(f"[produtor] {linha[:70]}")
        fila.put(linha)

    fila.put(DONE)


def consumidor():
    while True:
        linha = fila.get()
        if linha is DONE:
            break

        time.sleep(random.uniform(0.1, 0.2))
        registo = parse_linha(linha)

        if registo:
            with registos_lock:
                registos.append(registo)
            print(f"[consumidor] {registo['timestamp']}")

        fila.task_done()


def exportar(caminho: str):
    ordenados = sorted(registos, key=lambda r: normalizar_timestamp(r['timestamp']))
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(ordenados, f, ensure_ascii=False, indent=2)
    print(f"\nexportado {len(ordenados)} registos -> {caminho}")


if __name__ == "__main__":
    input_path = "input.txt"
    output_path = "output.json"

    t_prod = threading.Thread(target=produtor, args=(input_path,))
    t_cons = threading.Thread(target=consumidor)

    t_prod.start()
    t_cons.start()

    t_prod.join()
    t_cons.join()

    exportar(output_path)