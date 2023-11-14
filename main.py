import pygame
import sys

def initialize_board():
    return [[[0] * 3 for _ in range(3)] for _ in range(3)]

def print_board(board):
    for layer in board:
        for row in layer:
            print(" | ".join(map(str, row)))
            print("-" * 9)
        print("-" * 27)

def make_move(board, player, layer, row, col):
    if board[layer][row][col] == 0:
        board[layer][row][col] = player
        return True
    else:
        print("Invalid move. Try again.")
        return False

def check_win(board, player):
    for layer in board:
        # Checking rows and columns
        for i in range(3):
            if all(cell == player for cell in layer[i]) or all(layer[j][i] == player for j in range(3)):
                return True

        # Check diagonals
        if all(layer[i][i] == player for i in range(3)) or all(layer[i][2 - i] == player for i in range(3)):
            return True

     #Checking 3D diagonals
    if all(board[i][i][i] == player for i in range(3)) or all(board[i][i][2 - i] == player for i in range(3)):
        return True

    # Check vertical columns
    for i in range(3):
        if all(board[j][i][i] == player for j in range(3)) or all(board[j][i][2 - i] == player for j in range(3)):
            return True

    return False

def is_board_full(board):
    return all(all(all(cell != 0 for cell in row) for row in layer) for layer in board)

def play_game():
    board = initialize_board()
    current_player = 1

    while True:
        print_board(board)

        print(f"Player {current_player}'s turn:")
        layer = int(input("Enter layer (0-2): "))
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if make_move(board, current_player, layer, row, col):
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = 3 - current_player  # Switch between players 1 and 2

if __name__ == "__main__":
    play_game()

