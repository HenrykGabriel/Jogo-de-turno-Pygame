import pygame
                # função para quebrar textos grandes
def desenhar_texto(superficie, lista_paragrafos, x, y, largura_maxima, fonte, cor):
    pos_y = y 

    for paragrafo in lista_paragrafos:
        palavras = paragrafo.split(' ')
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            test_linha = linha_atual + palavra + " "
            if fonte.size(test_linha)[0] < largura_maxima:
                linha_atual = test_linha
            else:
                linhas.append(linha_atual)
                linha_atual = palavra + " "
        linhas.append(linha_atual)

        for linha in linhas:
            texto_renderizado = fonte.render(linha.strip(), True, cor)
            superficie.blit(texto_renderizado, (x, pos_y))
            pos_y += fonte.get_linesize() 

        pos_y += 15 