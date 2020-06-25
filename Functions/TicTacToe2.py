# -----------Global variabes------------
game_still_going = True

#Who won?
winner = None

#Who turns is it?
current_player = "X"

#list of board
board = ['-','-','-',
        '-','-','-',
        '-','-','-']

#-----------------------------------------

#Function for initial board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Funciton to play the game
def play_game():
    display_board()
    while game_still_going:
        #Invoke function to handle the turn
        handle_turn(current_player)

        #Invoke check if game is over
        check_if_game_over()

        #Invoke funtion to flip player
        flip_player()
    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


#Function to handle which turns
def handle_turn(player):

    print(player + "'s " + "turn.")
    position = (input("Choose a position from 1-9: "))
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = (input("Invalid input. Choose a position from 1-9: "))

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Can't go bro.")

    #Replace list's value with X if there is an input
    board[position] = player
    #Invoke function board again to display an updated board
    display_board()

#Funtion to check if the game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()

#Function if wins
def check_for_winner():

    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check cross
    cross_winner = check_cross()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif cross_winner:
        winner = cross_winner
    else:
        #there was no win
        winner = None

def check_rows():
    #set up global variable
    global game_still_going
    #check if any of the rows have all the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #If there is a win, var will change to False
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    else:
        return None

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    else:
        return None

def check_cross():
    global game_still_going
    cross_1 = board[0] == board[4] == board[8] != "-"
    cross_2 = board[6] == board[4] == board[2] != "-"
    if cross_1 or cross_2:
        game_still_going = False
    if cross_1:
        return board[0]
    if cross_2:
        return board[2]
    else:
        return None

#Function if loses
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return None

#Function to flip player's turn
def flip_player():
    #make var becommes global
    global current_player
    #changes turns
    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"
    return

play_game()