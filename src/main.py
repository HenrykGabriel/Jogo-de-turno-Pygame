import pygame
from config import larg_tela, alt_tela
from gerenciador import Gerenciador
from jogador import Jogador
from cavaleiro import Cavaleiro
from menu import Menu
from fontes import Fontes
from sons import Sons

pygame.init()

janela = pygame.display.set_mode((larg_tela, alt_tela))
pygame.display.set_caption("The Last Vanguard")

clock = pygame.time.Clock()

# MÚSICA DE FUNDO

sons = Sons()

sons.iniciar_musica()

rodando = True

cavaleiro = Cavaleiro()

jogador = Jogador(cavaleiro)

fontes = Fontes()

menu = Menu(fontes)

gerenciador = Gerenciador(jogador)

estado = "menu"

while rodando:

    eventos = pygame.event.get()

    for evento in eventos:

        if evento.type == pygame.QUIT:

            rodando = False

    if estado == "menu":

        menu.draw(janela)
        menu.update(eventos)
        if menu.update_comecar(eventos) == True:
            estado = "jogando"

    elif estado == "jogando":

        gerenciador.rodar(janela, eventos)

    pygame.display.update()

    clock.tick(60)

pygame.quit()