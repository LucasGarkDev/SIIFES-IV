# codigo_lab1_escalabilidade.py
import time
from datetime import datetime
import threading
import random

log_de_transacoes = []
lock = threading.Lock()

def processar_transacao(evento):
    global log_de_transacoes
    agora = datetime.now().strftime("%H:%M:%S")

    with lock:  # Evita conflito entre threads
        print(f"\n[{agora}] NOVO EVENTO: Cliente {evento['cliente']} | Valor: R${evento['valor']}")

        if evento['valor'] > 1000:
            evento['valor'] *= 0.85
            print(f" [AUTOMAÇÃO]: Regra aplicada. Novo valor: R${evento['valor']:.2f}")

        compras_anteriores = [
            t for t in log_de_transacoes
            if t['cliente'] == evento['cliente']
        ]

        if len(compras_anteriores) >= 2:
            print(f" [ALERTA CEP]: Cliente {evento['cliente']} com múltiplas transações.")

        log_de_transacoes.append(evento)


def gerar_transacao(cliente_id):
    evento = {
        'cliente': f'Cliente_{cliente_id}',
        'valor': random.randint(100, 3000)
    }
    processar_transacao(evento)


threads = []

# Simula 20 clientes simultâneos (poderia ser 10000)
for i in range(20):
    t = threading.Thread(target=gerar_transacao, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()