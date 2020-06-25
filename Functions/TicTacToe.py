def DisplayBoard():
    list=[1,2,3,4,5,6,7,8,9]
    print("+-------+-------+-------+" + " \n|       |       |       |\n|   1   |   2   |   3   |\n|       |       |       |")
    print("+-------+-------+-------+" + " \n|       |       |       |\n|   4   |   5   |   6   |\n|       |       |       |")
    print("+-------+-------+-------+" + " \n|       |       |       |\n|   7   |   8   |   9   |\n|       |       |       | \n" + "+-------+-------+-------+")

def EnterMove():
    board = int(input("Enter your move: "))
    if board < 1 and board > 9:
        return None
    else:
        return board

DisplayBoard()
EnterMove()

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#