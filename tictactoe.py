import math
import tkinter as tk
import tkinter.font as tkfont

# Initial game state, blank grid
game = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

# Difficulty levels (0 - uninitialized, 1 - easy, 2 - medium, 3 - hard)
difficulty = 0

# Function to reset the game to the initial state
def reset_game():
    global game
    game = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    
    # Destroy previous widgets and create new difficulty selection page
    for widget in root.winfo_children():

        widget.destroy()
    create_select_difficulty_page()

# Function to check if the game has ended and return the winner
def is_end():
    # Check rows for winner
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != ' ': # if all elements in row are same, return winner
            return row[0]
    # Check columns for winner
    for col in range(len(game)): # if all columns in the row are same, return winner
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return check[0]
    # Check diagonals for winner
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != ' ': # check top-left to bottom-right diagonal for winner
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] != ' ': # check top-right to bottom-left diagonal for winner
        return game[0][2]
    # Check for tie (no spaces left)
    for row in game:
        for elem in row:
            if elem == ' ': # if there is a space left, return false meaning game has not ended, otherwise return tie
                return False
    return 'tie'

# Minimax function to determine best AI move
def minimax(state, depth, player):
    # Restrict depth based on difficulty
    if difficulty == 1 and depth > 1: # if easy difficulty, only look one move ahead
        return 0, None
    elif difficulty == 2 and depth > 2: # if medium difficulty, only look 2 moves ahead
        return 0, None
        # otherwise, dont restrict depth

    winner = is_end() # check if game has ended, if game has ended return a score that reflects the outcome
    if winner:
        # Return score based on winner
        if winner == 'X':
            return (10 - depth, None)
        elif winner == 'O':
            return (-10 + depth, None)
        elif winner == 'tie':
            return (0, None)

    if player:  # AI turn (maximizing)
        best_value = -math.inf
        move = None
        for i in range(3): # iterate through all possible moves
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'X'
                    value = minimax(state, depth + 1, False)[0] # recustively call minimax to evaluate best move (highest score)
                    state[i][j] = ' '
                    if value > best_value:
                        best_value = value
                        move = (i, j)
        return best_value, move
    else:  # Human turn (minimizing)
        best_value = math.inf
        move = None
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'O'
                    value = minimax(state, depth + 1, True)[0] # recustively call minimax to evaluate best move for human (lowest score)
                    state[i][j] = ' '
                    if value < best_value:
                        best_value = value
                        move = (i, j)
        return best_value, move

# Function to start the game by setting difficulty and creating game board
def start_game():
    global difficulty
    difficulty = difficulty_var.get()
    for widget in root.winfo_children():
        widget.destroy()
    create_game_board()

# Function to create game board with buttons
def create_game_board():
    global buttons
    global status_label
    # Create buttons for each cell in the grid
    buttons = [[tk.Button(root, text=' ', width=10, height=3, font=game_font, command=lambda r=row, c=col: on_click(r, c)) for col in range(3)] for row in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].grid(row=i, column=j)

    # Status label to display game messages
    status_label = tk.Label(root, text="Your move", font=status_font)
    status_label.grid(row=3, column=0, columnspan=3)

# Function to handle player's click on a cell
def on_click(row, col):
    if game[row][col] != ' ':
        return
    game[row][col] = 'O'
    buttons[row][col].config(text='O')
    winner = is_end()
    if winner:
        show_replay_button()
        if winner == 'tie':
            status_label.config(text="It's a tie!")
        else:
            status_label.config(text="You Win!")
        return

    # AI's turn
    move = best_move()
    game[move[0]][move[1]] = 'X'
    buttons[move[0]][move[1]].config(text='X')

    # Check winner again
    winner = is_end()
    if winner:
        show_replay_button()
        if winner == 'tie':
            status_label.config(text="It's a tie!")
        else:
            status_label.config(text="AI Wins!")

# Function to show replay button after game ends
def show_replay_button():
    replay_button = tk.Button(root, text="Play Again", command=reset_game, font=status_font)
    replay_button.grid(row=4, column=0, columnspan=3)

# Function to get best move using minimax algorithm
def best_move():
    return minimax(game, 0, True)[1]

# Function to create the page for difficulty selection
def create_select_difficulty_page():
    global easy_button, medium_button, hard_button, start_button
    difficulty_var.set(0)
    # Create buttons for different difficulty levels
    easy_button = tk.Radiobutton(root, text="Easy", variable=difficulty_var, value=1, font=status_font)
    medium_button = tk.Radiobutton(root, text="Medium", variable=difficulty_var, value=2, font=status_font)
    hard_button = tk.Radiobutton(root, text="Impossible", variable=difficulty_var, value=3, font=status_font)
    start_button = tk.Button(root, text="Start Game", command=start_game, font=status_font)
    
    easy_button.grid(row=0, column=0)
    medium_button.grid(row=0, column=1)
    hard_button.grid(row=0, column=2)
    start_button.grid(row=1, column=0, columnspan=3)

# Tkinter GUI setup
root = tk.Tk()
root.title("Tic Tac Toe")

# Define Fonts
game_font = tkfont.Font(family="Helvetica", size=32)
status_font = tkfont.Font(family="Helvetica", size=16)

# Difficulty Selection
difficulty_var = tk.IntVar(value=0)
easy_button = tk.Radiobutton(root, text="Easy", variable=difficulty_var, value=1, font=status_font)
medium_button = tk.Radiobutton(root, text="Medium", variable=difficulty_var, value=2, font=status_font)
hard_button = tk.Radiobutton(root, text="Impossible", variable=difficulty_var, value=3, font=status_font)
start_button = tk.Button(root, text="Start Game", command=start_game, font=status_font)

create_select_difficulty_page()

root.mainloop() # starts main event loop of application


create_select_difficulty_page()

root.mainloop() # starts main event loop of application
