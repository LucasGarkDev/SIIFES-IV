from dados import salvar_dados

def adicionar_conhecimento(base):
    print("\n--- NOVO CONHECIMENTO ---")

    titulo = input("Título: ")
    conteudo = input("Conteúdo: ")

    novo_id = max([item['id'] for item in base], default=0) + 1

    novo_item = {
        "id": novo_id,
        "titulo": titulo,
        "conteudo": conteudo,
        "acessos": 0
    }

    base.append(novo_item)
    salvar_dados(base)

    print("Conhecimento adicionado com sucesso!")