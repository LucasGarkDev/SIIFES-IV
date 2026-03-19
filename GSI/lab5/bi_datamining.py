# ============================================================
# LABORATÓRIO 5 - BI e Data Mining
# ============================================================

import pandas as pd

print("\n====================================")
print("PARTE 0 - CARGA DE DADOS")
print("====================================")

# Interoperabilidade Técnica ocorre aqui:
# Leitura do arquivo CSV padronizado
df = pd.read_csv("vendas_200_registros.csv")

print("\nEstrutura da Base:")
print(df.head())

print("\nTotal de Registros:", len(df))