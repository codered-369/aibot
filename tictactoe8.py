# Set up board as a list with 9 elements, each representing an empty space
board = [" "] * 9

# Set up player variables
player1 = "X"
player2 = "O"

# Set up function to display the board
def display_board():
    print(" | ".join(board[:3]))
    print("---------")
    print(" | ".join(board[3:6]))
    print("---------")
    print(" | ".join(board[6:]))

# Set up function to ask player for their next move
def ask_player(player):
    while True:
        try:
            move = int(input(f"{player}, please enter your move (1-9): "))
            if  board[move-1] == " ":
                board[move-1] = player
                break
            else:
                print("That space is already taken. Please try again.")
        except(ValueError, IndexError):
            print("Invalid input. Please try again.")

# Set up function to check for a win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Set up main game loop
while True:
    display_board()
    ask_player(player1)
    if check_win(player1):
        print(f"{player1} wins!")
        break
    if all(space != " " for space in board):
        print("It's a tie!")
        break
    display_board()
    ask_player(player2)
    if check_win(player2):
        print(f"{player2} wins!")   
        break
