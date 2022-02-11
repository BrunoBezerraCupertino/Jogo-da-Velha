import pygame, sys
import numpy as np

pygame.init()

LINE_WIDTH = 15
WIDTH = 600
HEIGHT = 600
BLUE = (0, 230, 255)
RED = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
BOARDS_ROWS = 3
BOARDS_COLS = 3
SQUARE_SIZE = WIDTH//BOARDS_COLS
LARGURA_CIRCULO = 15
CIRCULO = 60
COR = (239, 231, 200)
X_WIDTH = 25
ESPACO = 55
COR_X = (66, 66, 66)

tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JOGO DA VELHA')
tela.fill(BLUE)

# board
board = np.zeros((BOARDS_ROWS, BOARDS_COLS))
print(board)


# pygame.draw.line( tela, RED, (10, 10), (300, 300), 10)


def draw_line():
    # 1 horisontal
    pygame.draw.line(tela, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # 2 horisontal
    pygame.draw.line(tela, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # 1 vetical
    pygame.draw.line(tela, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(tela, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def formas():
    for linhas in range(BOARDS_ROWS):
        for colunas in range(BOARDS_COLS):
            if board[linhas][colunas] == 1:
                pygame.draw.circle(tela, COR, (int(colunas * 200 + 100), int(linhas * 200 + 100)), CIRCULO,
                                   LARGURA_CIRCULO)
            elif board[linhas][colunas] == 2:
                pygame.draw.line(tela, COR_X, (colunas * 200 + ESPACO, linhas * 200 + 200 - ESPACO),
                                 (colunas * 200 + 200 - ESPACO, linhas * 200 + ESPACO), X_WIDTH)
                pygame.draw.line(tela, COR_X, (colunas * 200 + ESPACO, linhas * 200 + ESPACO),
                                 (colunas * 200 + 200 - ESPACO, linhas * 200 + 200 - ESPACO), X_WIDTH)


def marcar_quadrado(linha, coluna, jogador):
    board[linha][coluna] = jogador


def espaco_vazio(linha, coluna):
    return board[linha][coluna] == 0


def mesa_vazia():
    for linha in range(BOARDS_ROWS):
        for coluna in range(BOARDS_COLS):
            if board[linha][coluna] == 0:
                return False

    return True


def win(jogador):
    # vitoria vertical
    for coluna in range(BOARDS_COLS):
        if board[0][coluna] == jogador and board[1][coluna] == jogador and board[2][coluna] == jogador:
            vitoria_vertical(coluna, jogador)
            return True
    for linha in range(BOARDS_ROWS):
        if board[linha][0] == jogador and board[linha][1] == jogador and board[linha][2] == jogador:
            vitoria_horizontal(linha, jogador)
            return True

    if board[2][0] == jogador and board[1][1] == jogador and board[0][2] == jogador:
        asc_win(jogador)
        return True
    if board[0][0] == jogador and board[1][1] == jogador and board[2][2] == jogador:
        desc_win(jogador)
        return True

    return False


def vitoria_vertical(coluna, jogador):
    posX = coluna * 200 + 100

    if jogador == 1:
        cor = COR
    elif jogador == 2:
        cor = COR_X

    pygame.draw.line(tela, cor, (posX, 15), (posX, HEIGHT - 15), 15)


def vitoria_horizontal(linha, jogador):
    posY = linha * 200 + 100

    if jogador == 1:
        cor = COR
    elif jogador == 2:
        cor = COR_X

    pygame.draw.line(tela, cor, (15, posY), (WIDTH - 15, posY), 15)


def asc_win(jogador):
    if jogador == 1:
        cor = COR
    elif jogador == 2:
        cor = COR_X

    pygame.draw.line( tela, cor, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def desc_win(jogador):
    if jogador == 1:
        cor = COR
    elif jogador == 2:
        cor = COR_X

    pygame.draw.line(tela, cor, (15, 15), (WIDTH -15, HEIGHT - 15), 15)


def restart():
    tela.fill(BLUE)
    draw_line()
    jogador = 1
    for linhas in range(BOARDS_ROWS):
        for colunas in range(BOARDS_COLS):
            board[linhas][colunas] = 0


draw_line()

jogador = 1
game_over = False

# Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            linhas_clicadas = int(mouseY // 200)
            colunas_clicadas = int(mouseX // 200)

            if espaco_vazio(linhas_clicadas, colunas_clicadas):
                if jogador == 1:
                    marcar_quadrado(linhas_clicadas, colunas_clicadas, 1)
                    if win(jogador):
                        game_over = True
                    jogador = 2

                elif jogador == 2:
                    marcar_quadrado(linhas_clicadas, colunas_clicadas, 2)
                    if win(jogador):
                        game_over = True
                    jogador = 1

                formas()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                jogador = 1
                restart()


    pygame.display.update() 
