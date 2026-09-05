import os
import sys

larg_tela = 1000

alt_tela = 750

# Função para não precisar colocar todo o caminho da imagem/som/fonte
# Apenas o caminho dentro de assets
def caminho_asset(caminho):
    if getattr(sys, "frozen", False):
        pasta_base = sys._MEIPASS
    else:
        pasta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(pasta_base, "assets", caminho)