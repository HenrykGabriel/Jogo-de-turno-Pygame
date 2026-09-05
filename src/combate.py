import pygame
from config import larg_tela, alt_tela, caminho_asset
from fontes import Fontes

class Combate:
    def __init__(self, jogador, inimigos):
        self.jogador = jogador

        self.inimigos = inimigos

        self.fontes = Fontes()
        self.titulo = self.fontes.titulo
        self.texto_maior = self.fontes.texto_maior
        self.texto_normal = self.fontes.texto_normal
        self.texto_pequeno = self.fontes.texto_pequeno
        self.texto_normal_bold = self.fontes.texto_normal_bold
        self.texto_pequeno_bold = self.fontes.texto_pequeno_bold

        self.turno = "jogador"

        self.inimigo_selecionado = None

        self.larg_painel = larg_tela
        
        self.alt_painel = alt_tela // 3

        self.larg_cenario = larg_tela

        self.alt_cenario = alt_tela - self.alt_painel

        # CENARIO 1 - CAMPO ABERTO
        self.img_campo_aberto = pygame.image.load(caminho_asset("cenarios/Campo aberto.png")).convert_alpha()

        self.campo_aberto = pygame.transform.scale(self.img_campo_aberto, (self.larg_cenario, self.alt_cenario))

        self.cenario_rect = self.campo_aberto.get_rect()

        #  PAINEIS ------------------------------------------------------
        self.img_painel = pygame.image.load(caminho_asset("cenarios/painel.png")).convert_alpha()
        self.painel = pygame.transform.scale(self.img_painel, (self.larg_painel, self.alt_painel))
        self.painel_rect = self.painel.get_rect(bottom=alt_tela)

        self.img_painel_menor = pygame.image.load(caminho_asset("cenarios/painel_menor.png")).convert_alpha()
        self.painel_menor = pygame.transform.scale(self.img_painel_menor, ((self.larg_painel//3)-40, self.alt_painel - 120))

        self.painel_menor_rect = self.painel_menor.get_rect()
        self.painel_menor_rect.topright = self.cenario_rect.topright

        self.img_barra_vida = pygame.image.load(caminho_asset("cenarios/barra_vida.png")).convert_alpha()
        self.barra_vida = pygame.transform.scale(self.img_barra_vida, (190, 50))
        self.barra_vida_rect = self.barra_vida.get_rect()
        self.barra_vida_rect.y = self.alt_cenario // 2 + 95

        # -------------------------------------
        
        self.jogador.rect = self.jogador.imagem.get_rect()

        self.jogador.rect.center = (
            self.cenario_rect.centerx - 240,
            self.cenario_rect.centery + 10
        )

        self.posicionar_inimigos()

        # ATRIBUTOS
        self.jogador_classe = self.texto_normal_bold.render(f"Classe: {self.jogador.classe}", True, (255, 251, 0))
        self.jogador_classe_rect = self.jogador_classe.get_rect(
                    midleft=(
                            self.painel_rect.left + 130,
                            self.painel_rect.top + 40
                        ))
        
        self.jogador_vida = self.texto_normal.render(f"Vida: {self.jogador.vida_maxima}", True, (255, 251, 0))
        self.jogador_vida_rect = self.jogador_vida.get_rect(
                    midleft=(
                            self.painel_rect.left + 60,
                            self.painel_rect.top + 80
                        ))

        self.jogador_dano = self.texto_normal.render(f"Dano: {self.jogador.dano}", True, (255, 251, 0))
        self.jogador_dano_rect = self.jogador_dano.get_rect(
                    midleft=(
                            self.painel_rect.left + 220,
                            self.painel_rect.top + 80
                        ))

        self.jogador_esquiva = self.texto_normal.render(f"Esquiva: {self.jogador.esquiva}", True, (255, 251, 0))
        self.jogador_esquiva_rect = self.jogador_esquiva.get_rect(
                    midleft=(
                            self.painel_rect.left + 60,
                            self.painel_rect.top + 130
                        ))

        self.jogador_chance_critico = self.texto_normal.render(f"Chance de crítico: {self.jogador.chance_critico}%", True, (255, 251, 0))
        self.jogador_chance_critico_rect = self.jogador_chance_critico.get_rect(
                    midleft=(
                            self.painel_rect.left + 220,
                            self.painel_rect.top + 130
                        ))

        self.jogador_critico = self.texto_normal.render(f"Crítico: {self.jogador.critico}X", True, (255, 251, 0))
        self.jogador_critico_rect = self.jogador_critico.get_rect(
                    midleft=(
                            self.painel_rect.left + 60,
                            self.painel_rect.top + 180
                        ))

        self.jogador_escudo = self.texto_normal.render(f"Escudo: {self.jogador.escudo}", True, (255, 251, 0))
        self.jogador_escudo_rect = self.jogador_escudo.get_rect(
                    midleft=(
                            self.painel_rect.left + 220,
                            self.painel_rect.top + 180
                        ))
        # CARTAS ---------------------------------------
        self.larg_cartas = 160
        self.alt_cartas = self.alt_painel - 40
        self.img_carta_ataque = pygame.image.load(caminho_asset("cartas/carta_ataque.png")).convert_alpha()
        self.carta_ataque = pygame.transform.scale(self.img_carta_ataque, (self.larg_cartas, self.alt_cartas))
        self.carta_ataque_rect = self.carta_ataque.get_rect(
                    midleft=(
                            self.painel_rect.centerx + 80,
                            self.painel_rect.centery
                        ))

        self.img_carta_defesa = pygame.image.load(caminho_asset("cartas/carta_defesa.png")).convert_alpha()
        self.carta_defesa = pygame.transform.scale(self.img_carta_defesa, (self.larg_cartas, self.alt_cartas))
        self.carta_defesa_rect = self.carta_defesa.get_rect(
                    midleft=(
                            self.painel_rect.centerx + 80 + self.larg_cartas + 40,
                            self.painel_rect.centery
                        ))

        self.personagem_acao = None

        self.resultado = None

        self.tempo_resultado = pygame.time.get_ticks()

        self.acao = None

        self.indice_inimigo = 0

        self.escolher_carta = self.texto_maior.render("Escolha uma carta", True, (255, 251, 0))
        self.escolher_carta_rect = self.escolher_carta.get_rect(
                    midtop=(
                            self.cenario_rect.centerx - 30,
                            self.cenario_rect.top + 40
                        ))

        self.escolher_oponente = self.texto_maior.render("Escolha um oponente", True, (255, 251, 0))
        self.escolher_oponente_rect = self.escolher_oponente.get_rect(
                    midtop=(
                            self.cenario_rect.centerx - 40,
                            self.cenario_rect.top + 40
                        ))


    def comecar(self, janela, eventos, cenario_atual):

        self.draw(janela, cenario_atual)

        if self.turno == "jogador":

            if self.acao is None:
                self.acao = self.clicou_carta(eventos)

            if self.acao == "atacar":

                self.inimigo_selecionado = self.clicou_inimigo(eventos)

                if self.inimigo_selecionado is not None:

                    self.resultado = self.jogador.atacar(
                        self.inimigo_selecionado
                    )

                    self.personagem_acao = self.inimigo_selecionado

                    self.tempo_resultado = pygame.time.get_ticks()
                    self.tempo_turno = pygame.time.get_ticks()

                    if self.inimigo_selecionado.vida <= 0:
                        self.inimigos.remove(self.inimigo_selecionado)

                    self.acao = None

                    if len(self.inimigos) > 0:
                        self.turno = "inimigos"

                    else:
                        pass

        if self.turno == "inimigos":

            if pygame.time.get_ticks() - self.tempo_turno >= 1500:

                if self.indice_inimigo < len(self.inimigos):
                    inimigo = self.inimigos[self.indice_inimigo]

                    self.resultado = inimigo.atacar(self.jogador)
                    self.personagem_acao = self.jogador
                    self.tempo_resultado = pygame.time.get_ticks()

                    self.tempo_turno = pygame.time.get_ticks()
                    self.indice_inimigo += 1

                if self.indice_inimigo >= len(self.inimigos):

                    self.indice_inimigo = 0
                    self.turno = "jogador"

    def draw(self, janela, cenario_atual):

        if self.inimigos:
            inimigo = self.inimigos[0]
            self.draw_atributos_inimigo(janela, inimigo)

        if cenario_atual == "Campo aberto":
            janela.blit(self.campo_aberto, (0, 0))

        janela.blit(self.painel, (0, self.alt_cenario))

        self.jogador.draw(janela)
        self.draw_barra_vida(janela, self.jogador, (14, 222, 17))

        for inimigo in self.inimigos:

            inimigo.draw(janela)
            self.draw_barra_vida(janela, inimigo, (224, 11, 11))

        self.draw_atributos(janela)

        self.draw_cartas(janela)

        self.draw_atributos_inimigo(janela, inimigo)

        self.mostrar_resultado(janela, self.personagem_acao)

        if self.acao == None and self.turno == "jogador":

            janela.blit(self.escolher_carta, self.escolher_carta_rect)

        if self.turno == "jogador" and self.acao == "atacar":

            janela.blit(self.escolher_oponente, self.escolher_oponente_rect)

    def posicionar_inimigos(self):

        x = self.cenario_rect.centerx + 330
        y = self.cenario_rect.centery + 10

        for inimigo in self.inimigos:

            inimigo.rect.center = (x, y)

            x -= inimigo.rect.width + 40

    def draw_atributos(self, janela):

        janela.blit(self.jogador_classe, self.jogador_classe_rect)

        janela.blit(self.jogador_vida, self.jogador_vida_rect)

        janela.blit(self.jogador_dano, self.jogador_dano_rect)

        janela.blit(self.jogador_esquiva, self.jogador_esquiva_rect)

        janela.blit(self.jogador_chance_critico, self.jogador_chance_critico_rect)

        janela.blit(self.jogador_critico, self.jogador_critico_rect)

        janela.blit(self.jogador_escudo, self.jogador_escudo_rect)

    def draw_cartas(self, janela):

        janela.blit(self.carta_ataque, self.carta_ataque_rect)

        janela.blit(self.carta_defesa, self.carta_defesa_rect)

    def draw_atributos_inimigo(self, janela, inimigo):

        janela.blit(self.painel_menor, self.painel_menor_rect)

        inimigo_nome = self.texto_pequeno_bold.render(f"Nome: {inimigo.nome}", True, (255, 251, 0))
        inimigo_nome_rect = inimigo_nome.get_rect(
                    midleft=(
                            self.painel_menor_rect.left + 40,
                            self.painel_menor_rect.top + 20
                        ))
        
        inimigo_vida = self.texto_pequeno.render(f"Vida: {inimigo.vida_maxima}", True, (255, 251, 0))
        inimigo_vida_rect = inimigo_vida.get_rect(
                    midleft=(
                            self.painel_menor_rect.left + 10,
                            self.painel_menor_rect.top + 50
                        ))

        inimigo_dano = self.texto_pequeno.render(f"Dano: {inimigo.dano}", True, (255, 251, 0))
        inimigo_dano_rect = inimigo_dano.get_rect(
                    midleft=(
                            self.painel_menor_rect.left + 95,
                            self.painel_menor_rect.top + 50
                        ))

        inimigo_esquiva = self.texto_pequeno.render(f"Esquiva: {inimigo.esquiva}", True, (255, 251, 0))
        inimigo_esquiva_rect = inimigo_esquiva.get_rect(
                    midleft=(
                            self.painel_menor_rect.left + 10,
                            self.painel_menor_rect.top + 80
                        ))

        inimigo_chance_critico = self.texto_pequeno.render(f"Chance de crítico: {inimigo.chance_critico}%", True, (255, 251, 0))
        inimigo_chance_critico_rect = inimigo_chance_critico.get_rect(
                    midleft=(
                            self.painel_menor_rect.left + 95,
                            self.painel_menor_rect.top + 80
                        ))

        inimigo_critico = self.texto_pequeno.render(f"Crítico: {inimigo.critico}X", True, (255, 251, 0))
        inimigo_critico_rect = inimigo_critico.get_rect(
                    midleft=(
                            self.painel_menor_rect.left + 10,
                            self.painel_menor_rect.top + 110
                        ))

        janela.blit(inimigo_nome, inimigo_nome_rect)
        janela.blit(inimigo_vida, inimigo_vida_rect)
        janela.blit(inimigo_dano, inimigo_dano_rect)
        janela.blit(inimigo_esquiva, inimigo_esquiva_rect)
        janela.blit(inimigo_chance_critico, inimigo_chance_critico_rect)
        janela.blit(inimigo_critico, inimigo_critico_rect)

    def draw_barra_vida(self, janela, personagem, cor):

        self.barra_vida_rect = self.barra_vida.get_rect(
            midtop=(
                personagem.rect.centerx,
                self.barra_vida_rect.y
            )
        )

        area_vida = pygame.Rect(
            self.barra_vida_rect.left + 10,
            self.barra_vida_rect.top + 8,
            170,
            35
        )

        porcentagem = personagem.vida / personagem.vida_maxima

        largura_vida = area_vida.width * porcentagem

        vida_rect = pygame.Rect(
            area_vida.left,
            area_vida.top,
            largura_vida,
            area_vida.height
        )

        vida_vida_maxima = self.texto_normal_bold.render(f"{personagem.vida}/{personagem.vida_maxima}", True, (255, 255, 255))
        vida_vida_maxima_rect = vida_vida_maxima.get_rect(
                midleft=(
                        self.barra_vida_rect.left + 30,
                        self.barra_vida_rect.centery
                    ))

        janela.blit(self.barra_vida, self.barra_vida_rect)

        pygame.draw.rect(janela, cor, vida_rect, 0, 5)

        janela.blit(vida_vida_maxima, vida_vida_maxima_rect)

    def clicou_carta(self, eventos):

        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:

                    if self.carta_ataque_rect.collidepoint(evento.pos):
                        return "atacar"

                    elif self.carta_defesa_rect.collidepoint(evento.pos):
                        return "defender"

        return None    

    def clicou_inimigo(self, eventos):
    
            for evento in eventos:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        for inimigo in self.inimigos:
                            if inimigo.rect.collidepoint(evento.pos):
                                return inimigo
            
            return None 
                                        # é o personagem em que aconteceu a ação, ex: o jogador atacou
                                        # e o inimigo se esquivou, o inimigo é personagem
    def mostrar_resultado(self, janela, personagem):
        if self.resultado is None:
            return

        tempo_atual = pygame.time.get_ticks()

        if tempo_atual - self.tempo_resultado < 1500:

            texto = self.texto_maior.render(
                str(self.resultado),
                True,
                (207, 6, 6)
            )

            rect = texto.get_rect(
                center=(personagem.rect.centerx,
                        personagem.rect.top - 30)
            )

            janela.blit(texto, rect)

        else:
            self.resultado = None