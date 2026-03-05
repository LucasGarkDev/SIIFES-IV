# lab3/legacy_systems.py
# Sistema A: Ilha de Dados de RH
funcionario_rh = {
    "id_func": 101,
    "nome_completo": "Eduardo Amaral",
    "salario_base": 5000.00
}
# Sistema B: Ilha de Dados Financeira (Espera 'cod' e 'valor')
def processar_pagamento(dados_pagamento):
    # Simula um sistema que falha se os nomes das chaves estiverem errados
    try:
        print(f"Processando ID {dados_pagamento['cod']}: Valor R$ {dados_pagamento['valor']}")
    except KeyError as e:
        print(f"ERRO DE INTEROPERABILIDADE: Chave não encontrada {e}")
# Tentativa de integração direta (VAI FALHAR)
processar_pagamento(funcionario_rh)