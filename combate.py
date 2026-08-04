import pygame

def combate(janela, gerenciador, inimigos_fase, jogador):

    while True:

        desenhar_cenario(janela, gerenciador)

        if gerenciador.turno == "jogador":

            gerenciador.turno = "inimigo"

        elif gerenciador.turno == "inimigo":

            for inimigo in inimigos_fase:

                inimigo.atacar(jogador)


def desenhar_cenario(janela, gerenciador):

    janela.blit(gerenciador.cenario, (0, 0))

    janela.blit(gerenciador.painel, (0, gerenciador.alt_cenario))