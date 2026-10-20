import sys

def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == mark:
            return True
    return False

def check_draw(board):
    return all(pos in ['X', 'O'] for pos in board)

def get_move(board, player):
    while True:
        try:
            move = input(f"שחקן {player}, בחר משבצת (1-9): ")
            if move.lower() == 'exit':
                print("יציאה מהמשחק.")
                sys.exit()
            move = int(move)
            if move < 1 or move > 9:
                print("יש לבחור מספר בין 1 ל-9.")
                continue
            if board[move-1] in ['X', 'O']:
                print("משבצת זו כבר תפוסה.")
                continue
            return move-1
        except ValueError:
            print("יש להכניס מספר תקין.")

def play():
    board = [str(i+1) for i in range(9)]
    current_player = "X"
    print("ברוכים הבאים לאיקס עיגול! (כדי לצאת כתבו exit)")
    print_board(board)

    while True:
        idx = get_move(board, current_player)
        board[idx] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"שחקן {current_player} ניצח!")
            break
        if check_draw(board):
            print("תיקו!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play()