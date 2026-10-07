import pygame
from config import alt_tela, larg_tela, caminho_asset
from botao import Botao
from cavaleiro import Cavaleiro
from mago import Mago
from arqueira import Arqueira

class EscolherClasse:
    def __init__(self, fontes):
        self.titulo = fontes.titulo
        self.texto_maior = fontes.texto_maior
        self.texto_medio = fontes.texto_medio
        self.texto_normal = fontes.texto_normal
        self.texto_pequeno = fontes.texto_pequeno

        # CLASSES

        self.cavaleiro = Cavaleiro()
        self.mago = Mago()
        self.arqueira = Arqueira()
        img = pygame.image.load(caminho_asset("cenarios/Campo aberto.png")).convert_alpha()
        self.fundo = pygame.transform.scale(img, (larg_tela, alt_tela))

        self.efeito_escuro = pygame.Surface((larg_tela, alt_tela))
        self.efeito_escuro.fill((0,0,0))
        self.efeito_escuro.set_alpha(230)
        
        # TITULO ESCOLHER CLASSE

        self.titulo_tela = self.texto_maior.render("Escolha sua classe!", True, (255, 251, 0))
        self.titulo_rect = self.titulo_tela.get_rect(
            center=(
                self.fundo.get_rect().centerx,
                self.fundo.get_rect().centery - 250)
                )

        # CONTAINER CLASSES

        img_container = pygame.image.load(caminho_asset("cenarios/container_classe.png")).convert_alpha()

        self.larg_container_classes = 220
        self.alt_container_classes = 540

        self.container_cavaleiro = pygame.Rect((larg_tela-self.larg_container_classes)//2 - self.larg_container_classes - 30, 
                                    180, self.larg_container_classes, self.alt_container_classes)

        self.container_mago = pygame.Rect((larg_tela-self.larg_container_classes)//2, 
                                    180, self.larg_container_classes, self.alt_container_classes)

        self.container_arqueira = pygame.Rect((larg_tela-self.larg_container_classes)//2 + self.larg_container_classes + 30, 
                                    180, self.larg_container_classes, self.alt_container_classes)
        
        self.container_classe_img = pygame.transform.scale(img_container, (self.larg_container_classes, self.alt_container_classes))

        self.containers_classes = [self.container_cavaleiro, self.container_mago, self.container_arqueira]# self.container_arqueira

    def rodar(self, janela, eventos):

        self.draw(janela)

        classe_escolhida = self.clicou_classe(eventos)

        return classe_escolhida

    def clicou_classe(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:

                    for classe in self.containers_classes:

                        if classe.collidepoint(evento.pos):

                            if classe == self.container_cavaleiro:
                                return self.cavaleiro
                            
                            elif classe == self.container_mago:
                                return self.mago
                            
                            elif classe == self.container_arqueira:
                                return self.arqueira

        return None
            

    def draw(self, janela):

        janela.blit(self.fundo, (0,0))
        janela.blit(self.efeito_escuro, (0,0))

        janela.blit(self.titulo_tela, self.titulo_rect)

        self.draw_classes(janela)

    def draw_classes(self, janela):

        for container in self.containers_classes:
            if container == self.container_cavaleiro:
                classe = self.cavaleiro
            elif container == self.container_mago:
                classe = self.mago
            elif container == self.container_arqueira:
                classe = self.arqueira

            janela.blit(self.container_classe_img, container)

            imagem_rect = classe.imagem.get_rect(
                midtop=(
                    container.centerx,
                    container.top + 5
                )
            )

            janela.blit(classe.imagem, imagem_rect)

            classe_nome = self.texto_medio.render(classe.classe, True, (255, 251, 0))
            janela.blit(classe_nome, (container.centerx - classe_nome.get_width() // 2, container.centery - 70))

            classe_vida = self.texto_normal.render(f"Vida: {classe.vida_maxima}", True, (255, 251, 0))
            janela.blit(classe_vida, (container.centerx - classe_vida.get_width() // 2, container.centery - 10))

            classe_dano = self.texto_normal.render(f"Dano: {classe.dano_min} - {classe.dano_max}", True, (255, 251, 0))
            janela.blit(classe_dano, (container.centerx - classe_dano.get_width() // 2, container.centery + 30))

            classe_chance = self.texto_normal.render(f"Chance crítico: {classe.chance_critico}", True, (255, 251, 0))
            janela.blit(classe_chance, (container.centerx - classe_chance.get_width() // 2, container.centery + 70))

            classe_critico = self.texto_normal.render(f"Crítico: {classe.critico}", True, (255, 251, 0))
            janela.blit(classe_critico, (container.centerx - classe_critico.get_width() // 2, container.centery + 110))

            classe_esquiva = self.texto_normal.render(f"Esquiva: {classe.esquiva}", True, (255, 251, 0))
            janela.blit(classe_esquiva, (container.centerx - classe_esquiva.get_width() // 2, container.centery + 150))

            classe_escudo = self.texto_normal.render(f"Escudo: {classe.escudo_maximo}", True, (255, 251, 0))
            janela.blit(classe_escudo, (container.centerx - classe_escudo.get_width() // 2, container.centery + 190))
