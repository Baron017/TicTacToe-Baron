import pygame
import sys

pygame.init()

# Constants
#3D version
WIDTH = 600
HEIGHT = 600
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)
PLAYER1_COLOR = (255, 0, 0)
PLAYER2_COLOR = (0, 0, 255)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Tic Tac Toe")

# Initialize the game board
board = [[[0] * BOARD_SIZE for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
current_player = 1  # Player 1 starts

# Functions
def draw_board():
    screen.fill(WHITE)

    # Draw horizontal lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

    # Draw vertical lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)

    # Draw the moves
    for z in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if board[z][y][x] == 1:
                    pygame.draw.circle(screen, PLAYER1_COLOR, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
                elif board[z][y][x] == 2:
                    pygame.draw.line(screen, PLAYER2_COLOR, (x * CELL_SIZE, y * CELL_SIZE), ((x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE), 2)
                    pygame.draw.line(screen, PLAYER2_COLOR, ((x + 1) * CELL_SIZE, y * CELL_SIZE), (x * CELL_SIZE, (y + 1) * CELL_SIZE), 2)

    pygame.display.flip()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0] // CELL_SIZE
            y = pos[1] // CELL_SIZE

            # Check if the selected cell is empty
            if board[0][y][x] == 0:
                # Find the lowest empty layer
                z = 0
                while z < BOARD_SIZE - 1 and board[z + 1][y][x] == 0:
                    z += 1

                # Make the move
                board[z][y][x] = current_player

                # Check for a winner
                # (You need to implement the check_win function based on your specific win conditions)

                # Switch to the next player
                current_player = 3 - current_player  # Switch between players 1 and 2

    # Draw the game board
    draw_board()