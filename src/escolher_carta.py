import pygame
import random

from config import alt_tela, larg_tela, caminho_asset

from cartas_atributos import cartas_bronze, cartas_prata, cartas_ouro


class TelaEscolherCarta:

    def __init__(self, fontes):

        self.titulo = fontes.titulo
        self.texto_medio = fontes.texto_medio
        self.texto_normal = fontes.texto_normal
        self.texto_pequeno = fontes.texto_pequeno

        # CENÁRIOS
        self.larg_cenario = larg_tela
        self.alt_cenario = alt_tela

        self.img_campo_aberto = pygame.image.load(
            caminho_asset("cenarios/Campo aberto.png")
        ).convert_alpha()

        self.campo_aberto = pygame.transform.scale(
            self.img_campo_aberto,
            (self.larg_cenario, self.alt_cenario)
        )

        self.img_deserto = pygame.image.load(
            caminho_asset("cenarios/Deserto.png")
        ).convert_alpha()

        self.deserto = pygame.transform.scale(
            self.img_deserto,
            (self.larg_cenario, self.alt_cenario)
        )

        self.img_vulcao = pygame.image.load(
            caminho_asset("cenarios/Zona vulcânica.png")
        ).convert_alpha()

        self.zona_vulcanica = pygame.transform.scale(
            self.img_vulcao,
            (self.larg_cenario, self.alt_cenario)
        )

        self.fundo = None

        # EFEITO ESCURO
        self.efeito_escuro = pygame.Surface(
            (larg_tela, alt_tela)
        )
        self.efeito_escuro.fill((0, 0, 0))
        self.efeito_escuro.set_alpha(230)

        self.cartas = []

        self.sorteou = False

        self.distancia_cartas = 250

        self.titulo = self.titulo.render("Escolha sua carta!", True, (255, 251, 0))
        self.titulo_rect = self.titulo.get_rect(
            center=(
                self.campo_aberto.get_rect().centerx,
                self.campo_aberto.get_rect().centery - 300)
                )

    def sortear_cartas(self):

        self.cartas = []

        bronze = cartas_bronze.copy()
        prata = cartas_prata.copy()
        ouro = cartas_ouro.copy()

        listas = [
            bronze,
            prata,
            ouro
        ]

        pesos = [
            50,
            35,
            15
        ]

        for i in range(3):

            lista_escolhida = random.choices(
                listas,
                weights=pesos,
                k=1
            )[0]

            carta = random.choice(lista_escolhida)

            lista_escolhida.remove(carta)

            self.cartas.append(carta)

        # POSIÇÃO DAS CARTAS

        self.cartas[1].rect = self.cartas[1].imagem.get_rect(
            center=(
                larg_tela // 2,
                alt_tela // 2
            )
        )

        self.cartas[0].rect = self.cartas[0].imagem.get_rect(
            center=(
                larg_tela // 2 - self.distancia_cartas,
                alt_tela // 2
            )
        )

        self.cartas[2].rect = self.cartas[2].imagem.get_rect(
            center=(
                larg_tela // 2 + self.distancia_cartas,
                alt_tela // 2
            )
        )

    def rodar(self, janela, eventos, cenario, jogador):

        # Escolhe o cenário
        if cenario == "Campo aberto":
            self.fundo = self.campo_aberto

        elif cenario == "Deserto":
            self.fundo = self.deserto

        elif cenario == "Zona vulcânica":
            self.fundo = self.zona_vulcanica

        # Sorteia apenas uma vez
        if not self.sorteou:
            self.sortear_cartas()
            self.sorteou = True

        resultado = self.update(eventos, jogador)

        self.draw(janela)

        return resultado

    def update(self, eventos, jogador):

        for evento in eventos:

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if evento.button == 1:

                    for carta in self.cartas:

                        if carta.rect.collidepoint(evento.pos):

                            carta.aplicar(jogador)

                            self.sorteou = False

                            return "escolheu carta"

        return None

    def draw(self, janela):

        janela.blit(self.fundo, (0, 0))

        janela.blit(self.efeito_escuro, (0, 0))

        janela.blit(self.titulo, self.titulo_rect)

        for carta in self.cartas:

            janela.blit(carta.imagem, carta.rect)