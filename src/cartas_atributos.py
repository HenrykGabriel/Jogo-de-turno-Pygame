import pygame
from config import caminho_asset

class Carta_atributo:
    def __init__(self, raridade, caminho, atributo, quant_aumento):

        self.raridade = raridade

        self.img = pygame.image.load(caminho_asset(caminho))

        self.imagem = pygame.transform.scale(self.img, (200, 280))

        self.atributo = atributo

        self.quant_aumento = quant_aumento 

    def aplicar(self, jogador):

        if self.atributo == "vida_maxima":
            jogador.vida_maxima += self.quant_aumento

        elif self.atributo == "dano":
            jogador.dano += self.quant_aumento

        elif self.atributo == "esquiva":
            jogador.esquiva += self.quant_aumento

        elif self.atributo == "chance_critico":
            jogador.chance_critico += self.quant_aumento

        elif self.atributo == "critico":
            jogador.critico += self.quant_aumento

        elif self.atributo == "escudo_maximo":
            jogador.escudo_maximo += self.quant_aumento

# cartas bronze

bronze_dano = Carta_atributo("Bronze", "cartas_atributos/bronze_dano.png", "dano", 1)
bronze_vida = Carta_atributo("Bronze", "cartas_atributos/bronze_vida.png", "vida_maxima", 3)
bronze_chance = Carta_atributo("Bronze", "cartas_atributos/bronze_chance.png", "chance_critico", 1)
bronze_escudo = Carta_atributo("Bronze", "cartas_atributos/bronze_escudo.png", "escudo_maximo", 2)
bronze_critico = Carta_atributo("Bronze", "cartas_atributos/bronze_critico.png", "critico", 0.25)
bronze_esquiva = Carta_atributo("Bronze", "cartas_atributos/bronze_esquiva.png", "esquiva", 2)

cartas_bronze = [bronze_dano, bronze_vida, bronze_chance, bronze_escudo, bronze_critico, bronze_esquiva]

# cartas prata

prata_dano = Carta_atributo("Prata", "cartas_atributos/prata_dano.png", "dano", 2)
prata_vida = Carta_atributo("Prata", "cartas_atributos/prata_vida.png", "vida_maxima", 5)
prata_chance = Carta_atributo("Prata", "cartas_atributos/prata_chance.png", "chance_critico", 3)
prata_escudo = Carta_atributo("Prata", "cartas_atributos/prata_escudo.png", "escudo_maximo", 3)
prata_critico = Carta_atributo("Prata", "cartas_atributos/prata_critico.png", "critico", 0.5)
prata_esquiva = Carta_atributo("Prata", "cartas_atributos/prata_esquiva.png", "esquiva", 4)

cartas_prata = [prata_dano, prata_vida, prata_chance, prata_escudo, prata_critico, prata_esquiva]

# cartas ouro

ouro_dano = Carta_atributo("Ouro", "cartas_atributos/ouro_dano.png", "dano", 4)
ouro_vida = Carta_atributo("Ouro", "cartas_atributos/ouro_vida.png", "vida_maxima", 8)
ouro_chance = Carta_atributo("Ouro", "cartas_atributos/ouro_chance.png", "chance_critico", 5)
ouro_escudo = Carta_atributo("Ouro", "cartas_atributos/ouro_escudo.png", "escudo_maximo", 5)
ouro_critico = Carta_atributo("Ouro", "cartas_atributos/ouro_critico.png", "critico", 1)
ouro_esquiva = Carta_atributo("Ouro", "cartas_atributos/ouro_esquiva.png", "esquiva", 7)

cartas_ouro = [ouro_dano, ouro_vida, ouro_chance, ouro_escudo, ouro_critico, ouro_esquiva]