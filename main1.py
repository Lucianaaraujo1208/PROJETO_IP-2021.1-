import os
import pygame
import random
from pygame.locals import *


def maça_random():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return (x * 10, y * 10)


def colisao(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

cobrinha = [(200, 200), (210, 200), (220, 200)]
cobrinha_skin = pygame.Surface((10, 10))
cobrinha_skin.fill((0, 255, 0))

maça_pos = maça_random()
maça = pygame.Surface((10, 10))
maça.fill((255, 0, 0))

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cobrinha')

minha_direçao = BAIXO

relogio = pygame.time.Clock()

fonte = pygame.font.Font('freesansbold.ttf', 18)
pontuaçao = 0

fim_de_jogo = False

bg = pygame.image.load(os.path.join("cobrinha1.jpeg"))

while not fim_de_jogo:
    relogio.tick(10)
    tela.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                minha_direçao = CIMA
            if event.key == K_DOWN:
                minha_direçao = BAIXO
            if event.key == K_LEFT:
                minha_direçao = ESQUERDA
            if event.key == K_RIGHT:
                minha_direçao = DIREITA

    if colisao(cobrinha[0], maça_pos):
        maça_pos = maça_random()
        cobrinha.append((0, 0))
        pontuaçao += 1

    if cobrinha[0][0] == 600 or cobrinha[0][1] == 600 or cobrinha[0][0] < 0 or cobrinha[0][1] < 0:
        fim_de_jogo = True
        break

    for i in range(1, len(cobrinha) - 1):
        if cobrinha[0][0] == cobrinha[i][0] and cobrinha[0][1] == cobrinha[i][1]:
            fim_de_jogo = True
            break

    if fim_de_jogo:
        break

    for i in range(len(cobrinha) -1, 0, -1):
        cobrinha[i] = (cobrinha[i-1][0], cobrinha[i-1][1])

    if minha_direçao == CIMA:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
    if minha_direçao == BAIXO:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
    if minha_direçao == DIREITA:
        cobrinha[0] = (cobrinha[0][0] + 10,  cobrinha[0][1])
    if minha_direçao == ESQUERDA:
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])

    tela.fill((0, 0, 0))
    tela.blit(maça, maça_pos)


    for x in range(0, 600, 10):
        pygame.draw.line(tela, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):
        pygame.draw.line(tela, (40, 40, 40), (y, 0), (y, 600))

    pontuaçao_fonte = fonte.render(f'Pontuação: {pontuaçao}', True, (255, 255, 255))
    pontuaçao_rect = pontuaçao_fonte.get_rect()
    pontuaçao_rect.topright = (600 - 120, 10)
    tela.blit(pontuaçao_fonte, pontuaçao_rect)

    for pos in cobrinha:
        tela.blit(cobrinha_skin, pos)
        pygame.display.update()

while True:
    fim_de_jogo_fonte = pygame.font.Font('freesansbold.ttf', 40)
    fim_de_jogo_tela = fim_de_jogo_fonte.render(f'FIM DE JOGO', True,  (0, 0, 0))
    fim_de_jogo_rect = fim_de_jogo_tela.get_rect()
    fim_de_jogo_rect.midtop = (600 / 2, 100)
    tela.blit(fim_de_jogo_tela, fim_de_jogo_rect)

    sua_prontuaçao = pygame.font.Font('freesansbold.ttf', 40)
    sua_prontuaçao_tela = sua_prontuaçao.render(f'Sua pontuação foi {pontuaçao}', True, (0, 0, 0))
    sua_prontuaçao_rect = sua_prontuaçao_tela.get_rect()
    sua_prontuaçao_rect.midtop = (600 / 2, 300)
    tela.blit(sua_prontuaçao_tela, sua_prontuaçao_rect)
    pygame.display.update()
    pygame.time.wait(500)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
