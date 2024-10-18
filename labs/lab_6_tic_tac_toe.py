'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
def coord(square_num):
    row = (square_num - 1) // 3
    column = (square_num - 1) % 3

    coord = [row, column]

    return coord

def put_in_board(board, mark, square_num):
    my_list = coord(square_num)

    row = my_list[0]
    column = my_list[1]

    board[row][column] = mark

    return board

def get_free_squares(board):
    free_squares = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_squares.append([i,j])

    print(free_squares)

if __name__ == '__main__':
    turn = 0 

    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    while turn != 9:
        if turn % 2 == 0:
            mark = "X"
        else:
            mark = "O"

        square_num = int(input("Enter your move: "))
        board = put_in_board(board, mark, square_num)
        get_free_squares(board)
    
        print_board_and_legend(board)            
        turn += 1