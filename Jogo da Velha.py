###################################################################################
# Projeto:  Jogo da Velha 
# Objetivo: Criar o jogo da velha utilizando a biblioteca PyGame
###################################################################################

import pygame

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da janela
WIDTH, HEIGHT = 400, 400

# Definindo as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Criando a janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JOGO DA VELHA")

# Definindo as posições dos quadrados do jogo da velha
squares = [[None, None, None], [None, None, None], [None, None, None]]

# Definindo o jogador atual (X começa)
current_player = "X"

# Função para desenhar o tabuleiro do jogo da velha
def draw_board():
    screen.fill(WHITE)

    # Desenhando as linhas horizontais
    pygame.draw.line(screen, BLACK, (0, HEIGHT//3), (WIDTH, HEIGHT//3), 2)
    pygame.draw.line(screen, BLACK, (0, 2*HEIGHT//3), (WIDTH, 2*HEIGHT//3), 2)

    # Desenhando as linhas verticais
    pygame.draw.line(screen, BLACK, (WIDTH//3, 0), (WIDTH//3, HEIGHT), 2)
    pygame.draw.line(screen, BLACK, (2*WIDTH//3, 0), (2*WIDTH//3, HEIGHT), 2)

    # Desenhando os símbolos dos jogadores
    for row in range(3):
        for col in range(3):
            square = squares[row][col]
            if square == "X":
                x_pos = col * (WIDTH // 3) + (WIDTH // 6)
                y_pos = row * (HEIGHT // 3) + (HEIGHT // 6)
                pygame.draw.line(screen, BLACK, (x_pos - 20, y_pos - 20), (x_pos + 20, y_pos + 20), 2)
                pygame.draw.line(screen, BLACK, (x_pos - 20, y_pos + 20), (x_pos + 20, y_pos - 20), 2)
            elif square == "O":
                pygame.draw.circle(screen, BLACK, (col * (WIDTH // 3) + (WIDTH // 6), row * (HEIGHT // 3) + (HEIGHT // 6)), WIDTH // 12, 2)

    # Atualizando a tela
    pygame.display.update()

# Função para verificar se alguém ganhou o jogo
def check_winner():
    # Verificando linhas
    for row in range(3):
        if squares[row][0] == squares[row][1] == squares[row][2] and squares[row][0] is not None:
            return squares[row][0]

    # Verificando colunas
    for col in range(3):
        if squares[0][col] == squares[1][col] == squares[2][col] and squares[0][col] is not None:
            return squares[0][col]

# Verificando diagonais
    if squares[0][0] == squares[1][1] == squares[2][2] and squares[0][0] is not None:
        return squares[0][0]
    if squares[0][2] == squares[1][1] == squares[2][0] and squares[0][2] is not None:
        return squares[0][2]

    # Verificando se houve empate
    is_full = all(all(square is not None for square in row) for row in squares)
    if is_full:
        return "Empate"

    # Caso contrário, não há vencedor ainda
    return None

# Loop principal do jogo
running = True
while running:
    # Verificando eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if check_winner() is None:
                # Obtendo a posição do clique do mouse
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Convertendo a posição do mouse em índices de linhas e colunas
                row = mouse_y // (HEIGHT // 3)
                col = mouse_x // (WIDTH // 3)

                # Verificando se a posição está vazia
                if squares[row][col] is None:
                    # Atribuindo o símbolo do jogador atual à posição
                    squares[row][col] = current_player

                    # Alternando para o próximo jogador
                    current_player = "O" if current_player == "X" else "X"

    # Desenhando o tabuleiro do jogo da velha
    draw_board()

    # Verificando se há um vencedor
    winner = check_winner()
    if winner is not None:
        if winner == "Empate":
            message = "Empate!"
        else:
            message = f"Jogador {winner} venceu!"

        # Renderizando o texto na tela
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        # Atualizando a tela
        pygame.display.update()

        # Aguardando 2 segundos antes de reiniciar o jogo
        pygame.time.wait(2000)

        # Reiniciando o jogo
        squares = [[None, None, None], [None, None, None], [None, None, None]]
        current_player = "X"

# Finalizando o Pygame
pygame.quit()
