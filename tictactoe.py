# board
# display board
#play game
# handle turn
# check win
  #check row
  # check column
  #check diagonal
 # check tie
 #flip player 

 # ---Global Variables---
# Game board

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

#If game is still going
game_still_going = True

#who won?or tie?
winner = None

#whose turn is it
current_player = "X"

#displays board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2] + "    1 | 2 | 3 ")
  print(board[3] + " | " + board[4] + " | " + board[5] + "    4 | 5 | 6 ")
  print(board[6] + " | " + board[7] + " | " + board[8] + "    7 | 8 | 9 ")
  print("\n")

#play the game tic tac toe
def play_game():
        #displays initial board
        display_board()

        #loop to give turns to users until one wins game
        while game_still_going:

          #handle a single turn of an arbitary player
           handle_turn(current_player)

           #checks if  game is over
           check_if_game_over()

           #flip to other player
           flip_player()

       
# the game has been ended
        if winner == "X" or winner == "O":
           print(winner + " won.")
        elif winner == None:
           print("Tie.")  

#handles a single turn of an arbitrary player
def handle_turn(player):
  """gets the position of users input"""
  print(player + "'s turn.")
  position = input("choose a position from 1-9: ")

#checking validation of input
  valid = False
  while not valid:


    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("choose a position from 1-9: ")

    position=int(position) - 1
  
    if board[position] == "-":
     valid = True
    else:  
     print("You can't go there,try again")


  board[position] = player
  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():

  #set up global variables
  global winner

  #check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None 
  return

def check_rows():
  #set up global variables
  global game_still_going
  #check if any of the rows have all the same value (and its not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
#if any row does not have a match ,flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
    #return the winner(X or o)
  if row_1:
      return board[0]
  elif row_2:
      return board[3]
  elif row_3:
     return board[6]  
  else:
     return None


def check_columns():
  #set up global variables
  global game_still_going
  #check if any of the rows have all the same value (and its not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
#if any column does not have a match ,flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
    #return the winner(X or o)
  if column_1:
      return board[0]
  elif column_2:
      return board[1]
  elif column_3:
     return board[2]
  else:
     return None



def check_diagonals():
   #set up global variables
  global game_still_going
  #check if any of the rows have all the same value (and its not empty)
  diagonal_1= board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"
  
#if any column does not have a match ,flag that there is a win
  if diagonal_1 or diagonal_2 :
    game_still_going = False
    #return the winner(X or O)
  if diagonal_1:
      return board[0]
  elif diagonal_2:
      return board[6]
  else:
    return None

  
                 
def check_if_tie():
  global game_still_going
  if "-"not in board:
    game_still_going = False
  return

def flip_player():
  #global variable
  global current_player 
#if current_player = "X" then it changes to O and vice-versa
  if current_player == "X":
     current_player = "O"
  elif current_player == "O":
     current_player = "X"  

  return    
  
play_game()

