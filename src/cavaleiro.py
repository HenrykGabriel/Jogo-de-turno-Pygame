from config import caminho_asset


class Cavaleiro:

    def __init__(self):

        self.classe = "Cavaleiro"

        self.caminho_imagem = caminho_asset("cavaleiro/Cavaleiro.png")

        self.vida_maxima = 60

        self.vida = self.vida_maxima

        self.dano = 7

        self.chance_critico = 80

        self.critico = 1.5

        self.esquiva = 100

        self.escudo = 5

        self.larg_frame = 220

        self.alt_frame = 220
        
        self.qtd_frames = 9