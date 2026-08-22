import pygame
from config import larg_tela, alt_tela
from gerenciador import Gerenciador
from jogador import Jogador
from guerreiro import Guerreiro
from menu import Menu
from fontes import Fontes

pygame.init()

janela = pygame.display.set_mode((larg_tela, alt_tela))
pygame.display.set_caption("Jogo de turno")

clock = pygame.time.Clock()

rodando = True

gerenciador = Gerenciador()

jogador = Jogador()
guerreiro = Guerreiro()

fontes = Fontes()

menu = Menu(fontes)

jogador.escolher_classe(guerreiro)

estado = "menu"

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            rodando = False

    if estado == "menu":

        menu.draw(janela)

    if estado == "jogando":

        gerenciador.rodar(janela, jogador)

    pygame.display.update()

    clock.tick(60)

pygame.quit()