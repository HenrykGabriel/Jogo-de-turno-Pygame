import pygame
from config import larg_tela, alt_tela, caminho_asset
from fontes import Fontes

class Combate:
    def __init__(self, jogador, inimigos):
        self.jogador = jogador

        self.inimigos = inimigos

        # FONTES --------------------------------------------

        self.fontes = Fontes()
        self.titulo = self.fontes.titulo
        self.texto_maior = self.fontes.texto_maior
        self.texto_normal = self.fontes.texto_normal
        self.texto_pequeno = self.fontes.texto_pequeno
        self.texto_normal_bold = self.fontes.texto_normal_bold
        self.texto_pequeno_bold = self.fontes.texto_pequeno_bold
        self.texto_medio = self.fontes.texto_medio
        # ---------------------------------------------------

        self.turno = "jogador"

        self.inimigo_selecionado = None

        self.larg_painel = larg_tela
        
        self.alt_painel = alt_tela // 3

        self.larg_cenario = larg_tela

        self.alt_cenario = alt_tela - self.alt_painel

        # CENARIO 1 - CAMPO ABERTO -------------------------------------
        self.img_campo_aberto = pygame.image.load(caminho_asset("cenarios/Campo aberto.png")).convert_alpha()

        self.campo_aberto = pygame.transform.scale(self.img_campo_aberto, (self.larg_cenario, self.alt_cenario))

        # CENARIO 2 - DESERTO -------------------------------------

        self.img_deserto = pygame.image.load(caminho_asset("cenarios/Deserto.png")).convert_alpha()
        
        self.deserto = pygame.transform.scale(self.img_deserto, (self.larg_cenario, self.alt_cenario))

        self.img_vulcao = pygame.image.load(caminho_asset("cenarios/Zona vulcânica.png")).convert_alpha()
        
        self.zona_vulcanica = pygame.transform.scale(self.img_vulcao,(self.larg_cenario, self.alt_cenario))
                
        self.deserto = pygame.transform.scale(self.img_deserto, (self.larg_cenario, self.alt_cenario))

        self.cenario_rect = self.campo_aberto.get_rect()

        #  PAINEIS ------------------------------------------------------
        self.img_painel = pygame.image.load(caminho_asset("cenarios/painel.png")).convert_alpha()
        self.painel = pygame.transform.scale(self.img_painel, (self.larg_painel, self.alt_painel))
        self.painel_rect = self.painel.get_rect(bottom=alt_tela)

        self.img_painel_menor = pygame.image.load(caminho_asset("cenarios/painel_menor.png")).convert_alpha()
        self.painel_menor = pygame.transform.scale(self.img_painel_menor, (self.larg_painel//2+150, 400))

        self.painel_menor_rect = self.painel_menor.get_rect(
            center=(
                self.cenario_rect.centerx,
                self.cenario_rect.centery
            )
        )

        # EFEITO ESCURO ------------------------------------------------------

        self.efeito_escuro = pygame.Surface((larg_tela, alt_tela))
        self.efeito_escuro.fill((0,0,0))
        self.efeito_escuro.set_alpha(200)

        # ICONES ------------------------------------------------------

        img_livro = pygame.image.load(
            caminho_asset("cenarios/icone_livro.png")
        ).convert_alpha()

        self.livro = pygame.transform.scale(img_livro, (60, 60))

        self.livro_rect = self.livro.get_rect(
            topright=(larg_tela - 20, 20)
        )

        # BARRA DE VIDA E DE ESCUDO --------------------------------

        self.img_barra_vida = pygame.image.load(caminho_asset("cenarios/barra_vida.png")).convert_alpha()
        self.barra_vida = pygame.transform.scale(self.img_barra_vida, (190, 50))
        self.barra_vida_rect = self.barra_vida.get_rect()
        self.barra_vida_rect.y = self.alt_cenario // 2 + 95

        self.barra_escudo = pygame.transform.scale(self.img_barra_vida, (130, 35))
        self.barra_escudo_rect = self.barra_escudo.get_rect()

        # -------------------------------------
        # POSIÇÃO DO JOGADOR 
        self.jogador.rect = self.jogador.imagem.get_rect()

        self.jogador.rect.center = (
            self.cenario_rect.centerx - 260,
            self.cenario_rect.centery + 10
        )

        self.posicionar_inimigos()

        # ATRIBUTOS JOGADOR -------------------------------------------
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

        self.jogador_escudo = self.texto_normal.render(f"Escudo: {self.jogador.escudo_maximo}", True, (255, 251, 0))
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

        # GERAIS ----------------------------------

        self.personagem_acao = None

        self.resultado = None

        self.tempo_resultado = pygame.time.get_ticks()

        self.tempo_turno = pygame.time.get_ticks()

        self.acao = None

        self.indice_inimigo = 0

        self.ver_atributos = False

        self.iniciando = True
        self.tempo_inicio = pygame.time.get_ticks()

        self.finalizando = False
        self.tempo_final = 0
        self.resultado_final = None

        # ---------------------------------------

        # MENSAGENS PARA ORIENTAR O JOGADOR -------------------------

        self.cor_orientacao = (255, 251, 0)

        self.escolher_carta = self.texto_maior.render("Escolha uma carta", True, self.cor_orientacao)
        self.escolher_carta_rect = self.escolher_carta.get_rect(
                    midtop=(
                            self.cenario_rect.centerx,
                            self.cenario_rect.top + 40
                        ))

        self.escolher_oponente = self.texto_maior.render("Escolha um oponente", True, self.cor_orientacao)
        self.escolher_oponente_rect = self.escolher_oponente.get_rect(
                    midtop=(
                            self.cenario_rect.centerx,
                            self.cenario_rect.top + 40
                        ))


    def comecar(self, janela, eventos, cenario_atual, fase_atual):

        if self.iniciando:

            self.draw_inicio(janela, cenario_atual, fase_atual)

            if pygame.time.get_ticks() - self.tempo_inicio >= 4300:

                self.iniciando = False

        else:

            self.clicou_atributos(eventos)

            self.draw(janela, cenario_atual)

            if self.finalizando:
                if pygame.time.get_ticks() - self.tempo_final >= 1000:
                    return self.resultado_final

                return

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
                            self.finalizando = True
                            self.resultado_final = "vitoria"
                            self.tempo_final = pygame.time.get_ticks()

                elif self.acao == "defender":

                    self.jogador.ativar_escudo()

                    self.acao = None

                    self.tempo_resultado = pygame.time.get_ticks()
                    self.tempo_turno = pygame.time.get_ticks()

                    self.turno = "inimigos"

            if self.turno == "inimigos":

                if pygame.time.get_ticks() - self.tempo_turno >= 1700:

                    if self.indice_inimigo < len(self.inimigos):
                        inimigo = self.inimigos[self.indice_inimigo]

                        self.resultado = inimigo.atacar(self.jogador)
                        self.personagem_acao = self.jogador
                        self.tempo_resultado = pygame.time.get_ticks()

                        self.tempo_turno = pygame.time.get_ticks()
                        self.indice_inimigo += 1

                        if self.jogador.vida <= 0:
                            self.finalizando = True
                            self.resultado_final = "derrota"
                            self.tempo_final = pygame.time.get_ticks()

                    if self.indice_inimigo >= len(self.inimigos):

                        self.indice_inimigo = 0
                        self.turno = "jogador"

    def draw(self, janela, cenario_atual):

        if cenario_atual == "Campo aberto":
            janela.blit(self.campo_aberto, (0, 0))
        elif cenario_atual == "Deserto":
            janela.blit(self.deserto, (0, 0))
        elif cenario_atual == "Zona vulcânica":
            janela.blit(self.zona_vulcanica, (0, 0))

        self.atualizar_cor_orientacao(cenario_atual)

        janela.blit(self.painel, (0, self.alt_cenario))

        self.jogador.draw(janela)
        self.draw_barra_vida(janela, self.jogador, (14, 222, 17))
        self.draw_barra_escudo(janela)

        for inimigo in self.inimigos:

            inimigo.draw(janela)
            self.draw_barra_vida(janela, inimigo, (224, 11, 11))

        self.draw_atributos(janela)

        self.draw_cartas(janela)

        self.mostrar_resultado(janela, self.personagem_acao)

        if self.acao == None and self.turno == "jogador":

            janela.blit(self.escolher_carta, self.escolher_carta_rect)

        if self.turno == "jogador" and self.acao == "atacar":

            janela.blit(self.escolher_oponente, self.escolher_oponente_rect)

        if self.inimigos:
        
            inimigo = self.inimigos[0]

            if self.ver_atributos:
                janela.blit(self.efeito_escuro, (0,0))
                self.draw_atributos_inimigo(janela, inimigo)
            else:
                janela.blit(self.livro, self.livro_rect)

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

        # NOME
        inimigo_nome = self.texto_maior.render(
            f"{inimigo.nome}",
            True,
            (255, 251, 0)
        )

        inimigo_nome_rect = inimigo_nome.get_rect(
            center=(
                self.painel_menor_rect.centerx,
                self.painel_menor_rect.top + 70
            )
        )

        # VIDA
        inimigo_vida = self.texto_medio.render(
            f"Vida: {inimigo.vida_maxima}",
            True,
            (255, 251, 0)
        )

        inimigo_vida_rect = inimigo_vida.get_rect(
            midleft=(
                self.painel_menor_rect.centerx - 240,
                self.painel_menor_rect.top + 140
            )
        )

        # DANO
        inimigo_dano = self.texto_medio.render(
            f"Dano: {inimigo.dano}",
            True,
            (255, 251, 0)
        )

        inimigo_dano_rect = inimigo_dano.get_rect(
            midleft=(
                self.painel_menor_rect.centerx - 20,
                self.painel_menor_rect.top + 140
            )
        )

        # ESQUIVA
        inimigo_esquiva = self.texto_medio.render(
            f"Esquiva: {inimigo.esquiva}",
            True,
            (255, 251, 0)
        )

        inimigo_esquiva_rect = inimigo_esquiva.get_rect(
            midleft=(
                self.painel_menor_rect.centerx - 240,
                self.painel_menor_rect.top + 220
            )
        )

        # CHANCE DE CRÍTICO
        inimigo_chance_critico = self.texto_medio.render(
            f"Chance crítico: {inimigo.chance_critico}%",
            True,
            (255, 251, 0)
        )

        inimigo_chance_critico_rect = inimigo_chance_critico.get_rect(
            midleft=(
                self.painel_menor_rect.centerx - 20,
                self.painel_menor_rect.top + 220
            )
        )

        # CRÍTICO
        inimigo_critico = self.texto_medio.render(
            f"Crítico: {inimigo.critico}X",
            True,
            (255, 251, 0)
        )

        inimigo_critico_rect = inimigo_critico.get_rect(
            center=(
                self.painel_menor_rect.centerx,
                self.painel_menor_rect.top + 300
            )
        )

        # DESENHAR
        janela.blit(inimigo_nome, inimigo_nome_rect)
        janela.blit(inimigo_vida, inimigo_vida_rect)
        janela.blit(inimigo_dano, inimigo_dano_rect)
        janela.blit(inimigo_esquiva, inimigo_esquiva_rect)
        janela.blit(inimigo_chance_critico, inimigo_chance_critico_rect)
        janela.blit(inimigo_critico, inimigo_critico_rect)

    def clicou_atributos(self, eventos):

        for evento in eventos:

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:

                    if self.ver_atributos == False:

                        if self.livro_rect.collidepoint(evento.pos):
                            self.ver_atributos = True

                    else:
                        self.ver_atributos = False

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

        quant_vida = self.texto_normal_bold.render(f"{personagem.vida:.1f}/{personagem.vida_maxima:.1f}", True, (255, 255, 255))
        quant_vida_rect = quant_vida.get_rect(
                midleft=(
                        self.barra_vida_rect.left + 15,
                        self.barra_vida_rect.centery
                    ))

        janela.blit(self.barra_vida, self.barra_vida_rect)

        pygame.draw.rect(janela, cor, vida_rect, 0, 5)

        janela.blit(quant_vida, quant_vida_rect)

    def draw_barra_escudo(self, janela):

        if self.jogador.escudo > 0:

            self.barra_escudo_rect = self.barra_escudo.get_rect(
                    center=(
                        self.jogador.rect.centerx,
                        self.jogador.rect.centery + 150
                    )
                )
            
            area_escudo = pygame.Rect(
                self.barra_escudo_rect.left + 6,
                self.barra_escudo_rect.top + 4,
                118,
                27
            )
    
            porcentagem = self.jogador.escudo / self.jogador.escudo_maximo
    
            largura_escudo = area_escudo.width * porcentagem
    
            escudo_rect = pygame.Rect(
                area_escudo.left,
                area_escudo.top,
                largura_escudo,
                area_escudo.height
            )
    
            quant_escudo = self.texto_normal_bold.render(f"{self.jogador.escudo:.1f}/{self.jogador.escudo_maximo:.1f}", True, (255, 255, 255))
            quant_escudo_rect = quant_escudo.get_rect(
                    midleft=(
                            self.barra_escudo_rect.left + 15,
                            self.barra_escudo_rect.centery
                        ))
    
            janela.blit(self.barra_escudo, self.barra_escudo_rect)
    
            pygame.draw.rect(janela, (10, 91, 245), escudo_rect, 0, 5)
    
            janela.blit(quant_escudo, quant_escudo_rect)

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

        tempo_passado = pygame.time.get_ticks() - self.tempo_resultado

        if tempo_atual - self.tempo_resultado < 1700:

            texto = self.texto_medio.render(
                str(self.resultado),
                True,
                (207, 6, 6)
            )

            rect = texto.get_rect(
                center=(personagem.rect.centerx,
                        personagem.rect.top - 5)
            )

            subida = tempo_passado * 0.02
            rect.y -= subida

            janela.blit(texto, rect)

        else:
            self.resultado = None

    def draw_inicio(self, janela, cenario_atual, fase_atual):
        if cenario_atual == "Campo aberto":
            img = self.campo_aberto.copy()
            fundo = pygame.transform.scale(img, (larg_tela, alt_tela))
            janela.blit(fundo, (0, 0))

        elif cenario_atual == "Deserto":
            img = self.deserto.copy()
            fundo = pygame.transform.scale(img, (larg_tela, alt_tela))
            janela.blit(fundo, (0, 0))

        elif cenario_atual == "Zona vulcânica":
            img = self.zona_vulcanica.copy()
            fundo = pygame.transform.scale(img, (larg_tela, alt_tela))
            janela.blit(fundo, (0, 0))

        janela.blit(self.efeito_escuro, (0, 0))

        tempo_passado = pygame.time.get_ticks() - self.tempo_inicio

        titulo = self.texto_maior.render(
            f"Fase: {fase_atual} | Cenário: {cenario_atual}",
            True,
            (255, 251, 0)
        )
        janela.blit(titulo, ((larg_tela-titulo.get_width())//2, alt_tela // 2 - 250))

        if tempo_passado < 1000:
            texto = "Combate em..."
        
        elif tempo_passado < 1900:
            texto = "3"

        elif tempo_passado < 2700:
            texto = "2"

        elif tempo_passado < 3600:
            texto = "1"

        else:
            texto = "COMEÇAR!"

        imagem = self.titulo.render(
            texto,
            True,
            (255, 251, 0)
        )

        rect = imagem.get_rect(
            center=(larg_tela // 2, alt_tela // 2)
        )

        janela.blit(imagem, rect)

    def atualizar_cor_orientacao(self, cenario_atual):

        if cenario_atual == "Campo aberto":
            self.cor_orientacao = (255, 251, 0)

        elif cenario_atual == "Deserto":
            self.cor_orientacao = (46, 39, 26)

        elif cenario_atual == "Zona vulcânica":
            self.cor_orientacao = (191, 8, 8)

        self.escolher_carta = self.texto_maior.render(
            "Escolha uma carta",
            True,
            self.cor_orientacao
        )

        self.escolher_oponente = self.texto_maior.render(
            "Escolha um oponente",
            True,
            self.cor_orientacao
        )