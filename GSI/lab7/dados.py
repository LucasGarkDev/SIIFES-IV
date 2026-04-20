import json
import os

ARQUIVO_DADOS = "base_conhecimento.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return [
            {"id": 1, "titulo": "Acesso VPN", "conteudo": "Usar Cisco AnyConnect...", "acessos": 120},
            {"id": 2, "titulo": "Backup SQL", "conteudo": "Scripts às 02h...", "acessos": 45},
            {"id": 3, "titulo": "Lentidão ERP", "conteudo": "Pausar Backup_Sync.", "acessos": 89}
        ]
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def salvar_dados(base):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(base, f, indent=4, ensure_ascii=False)