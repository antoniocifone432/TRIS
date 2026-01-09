def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("---------")
    print()

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw(board):
    return " " not in board

def main():
    board = [" "] * 9
    current_player = "X"

    print("🎮 Benvenuto al Tris!")
    print("Scegli una posizione da 1 a 9 come questo schema:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")

    while True:
        print_board(board)

        try:
            move = int(input(f"Giocatore {current_player}, scegli una posizione (1-9): ")) - 1
            if board[move] != " ":
                print("❌ Posizione già occupata!")
                continue
        except (ValueError, IndexError):
            print("❌ Inserisci un numero valido da 1 a 9.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Giocatore {current_player} ha vinto!")
            break

        if is_draw(board):
            print_board(board)
            print("🤝 Pareggio!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
