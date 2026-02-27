# codigo_lab1_escalabilidade.py
import time
import multiprocessing
from datetime import datetime
import random
from concurrent.futures import ThreadPoolExecutor
import threading

NUM_CLIENTES = 4
LATENCIA = 0.1  # Alterar para 2 para o segundo teste
# LATENCIA = 2
# LATENCIA = 4

log_de_transacoes = []
lock = threading.Lock()

def processar_transacao(evento):
    global log_de_transacoes
    
    # Simula latência externa (rede/banco/API)
    time.sleep(LATENCIA)

    with lock:
        if evento['valor'] > 1000:
            evento['valor'] *= 0.85

        compras_anteriores = [
            t for t in log_de_transacoes
            if t['cliente'] == evento['cliente']
        ]

        log_de_transacoes.append(evento)


def gerar_transacao(cliente_id):
    evento = {
        'cliente': f'Cliente_{cliente_id}',
        'valor': random.randint(100, 3000)
    }
    processar_transacao(evento)


if __name__ == "__main__":

    inicio = time.time()

    # Pool de threads (não cria 10k threads reais)
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(gerar_transacao, range(NUM_CLIENTES))

    fim = time.time()

    tempo_total = fim - inicio
    throughput = NUM_CLIENTES / tempo_total

    print("\n--- TESTE DE ESCALABILIDADE ---")
    print(f"Clientes processados: {NUM_CLIENTES}")
    print(f"Latência simulada: {LATENCIA} segundos")
    print(f"Tempo total: {tempo_total:.4f} segundos")
    print(f"Throughput: {throughput:.2f} transações/segundo")