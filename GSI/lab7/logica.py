def buscar_conhecimento(base, termo):
    termo = termo.lower()
    return [
        item for item in base
        if termo in item['titulo'].lower()
        or termo in item['conteudo'].lower()
    ]