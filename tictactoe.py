import random

# Global Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won? or Tie?
winner = None

# Whos turn is it
current_player = "X"


# Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic tac toe
def play_game():

    # Display initial board
    display_board()

    # While the game is still going
    while game_still_going:

        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Handle a single turn of an arbitrary player
def handle_turn(player):

    # Get position from player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Check to see if somebody has won
def check_for_winner():
    # Set global variables
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def check_columns():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def check_if_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


# Flip the current player from X to O, or O to X
def flip_player():
    # Global variables we need
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"


# AI for the second player
def min_max(board, depth, isMax):
    # Get the score of the board
    score = evaluate(board)

    # Check if the game is over
    if score == 10 or score == -10 or isMovesLeft(board) == False:
        return score

    # If the player is maximizing
    if isMax:
        best = -1000

        # Traverse all the cells
        for i in range(9):
            # Check if cell is empty
            if board[i] == "-":
                # Make the move
                board[i] = "O"

                # Call min_max recursively and choose the maximum value
                best = max(best, min_max(board, depth + 1, not isMax))

                # Undo the move
                board[i] = "-"

        return best

    # If the player is minimizing
    else:
        best = 1000

        # Traverse all the cells
        for i in range(9):
            # Check if cell is empty
            if board[i] == "-":
                # Make the move
                board[i] = "X"

                # Call min_max recursively and choose the minimum value
                best = min(best, min_max(board, depth + 1, not isMax))

                # Undo the move
                board[i] = "-"

        return best


# Check if there are moves left on the board
def isMovesLeft(board):
    for i in range(9):
        if board[i] == "-":
            return True
    return False


# Evaluate the board
def evaluate(board):
    # Check for rows
    row1 = board[0] == board[1] == board[2]
    row2 = board[3] == board[4] == board[5]
    row3 = board[6] == board[7] == board[8]

    # Check for columns
    col1 = board[0] == board[3] == board[6]
    col2 = board[1] == board[4] == board[7]
    col3 = board[2] == board[5] == board[8]

    # Check for diagonals
    diag1 = board[0] == board[4] == board[8]
    diag2 = board[2] == board[4] == board[6]

    # Check for wins
    if row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2:
        if board[4] == "X":
            return -10
        elif board[4] == "O":
            return 10
        else:
            return 0

    # Else return 0
    else:
        return 0


# Find the best move for the AI
def findBestMove(board):
    bestVal = -1000
    bestMove = -1

    # Traverse all cells
    for i in range(9):
        # Check if cell is empty
        if board[i] == "-":
            # Make the move
            board[i] = "O"

            # Calculate the minimax value
            moveVal = min_max(board, 0, False)

            # Undo the move
            board[i] = "-"

            # If the value of the current move is more than the best value, then update best value and best move
            if moveVal > bestVal:
                bestMove = i
                bestVal = moveVal

    return bestMove


# Make the AI move
def ai_turn():
    print("AI's turn.")

    # Find the best move
    bestMove = findBestMove(board)

    # Make the move
    board[bestMove] = "O"

    # Show the game board
    display_board()


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()
