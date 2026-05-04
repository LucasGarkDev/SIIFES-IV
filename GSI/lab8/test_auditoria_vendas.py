"""Testes do Laboratorio 8 - Auditoria de Sistemas."""

from __future__ import annotations

import unittest
from pathlib import Path

import pandas as pd

from auditoria_vendas import (
    ARQUIVO_CSV,
    carregar_base,
    identificar_duplicidades,
    identificar_falhas_negativos,
    identificar_falhas_nulos,
    identificar_valores_invalidos,
    montar_resumo_principal,
)


class AuditoriaVendasTestCase(unittest.TestCase):
    """Valida as regras centrais do script de auditoria."""

    def test_contagens_da_base_real(self) -> None:
        df = carregar_base(ARQUIVO_CSV)

        self.assertEqual(len(df), 300)
        self.assertEqual(len(identificar_falhas_nulos(df)), 68)
        self.assertEqual(len(identificar_falhas_negativos(df)), 49)
        self.assertEqual(len(identificar_duplicidades(df)), 0)
        self.assertEqual(len(identificar_valores_invalidos(df)), 99)

    def test_duplicidades_em_base_controlada(self) -> None:
        df = pd.DataFrame(
            [
                {"id_transacao": 1, "cliente": "Ana", "valor": "10", "metodo_pagamento": "Pix"},
                {"id_transacao": 1, "cliente": "Bruno", "valor": "20", "metodo_pagamento": "Cartao"},
                {"id_transacao": 2, "cliente": "Carla", "valor": "-5", "metodo_pagamento": "Boleto"},
            ]
        )
        df["valor_numerico"] = pd.to_numeric(df["valor"], errors="coerce")

        duplicados = identificar_duplicidades(df)
        negativos = identificar_falhas_negativos(df)

        self.assertEqual(duplicados["id_transacao"].tolist(), [1, 1])
        self.assertEqual(negativos["id_transacao"].tolist(), [2])

    def test_resumo_principal_tem_categorias_esperadas(self) -> None:
        df = carregar_base(Path(ARQUIVO_CSV))
        resumo = montar_resumo_principal(df)

        self.assertEqual(resumo["categoria"].tolist(), ["Nulos", "Negativos", "Duplicados"])
        self.assertEqual(resumo["quantidade"].tolist(), [68, 49, 0])


if __name__ == "__main__":
    unittest.main()
