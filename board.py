# -*- coding: utf-8 -*-
"""board

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13W3dKAOt4_JxS0sjeFv3hopguM4BZIqN
"""

topRow = ['-', '-', '-']
middleRow = ['-', '-', '-']
bottomRow = ['-', '-', '-']

turn = 0

def board():
    print(topRow)
    print(middleRow)
    print(bottomRow)
    
def checkWin():
    return "false"
    
def placeMark():
    row = ""
    column = ""
    while (row != "Top") or (row!= "Middle") or (row != "Bottom"):
      row = input("Which row do you want to place the mark on the board? Top, Middle, or Bottom: ")
      if (row == "Top") or (row == "Middle") or (row == "Bottom"):
        break
    while (column != 1) or (column != 2) or (column != 3):
      column = input("Which column do you want to place the mark on the board? 1, 2, or 3: ")
      if (int(column) == 1) or (int(column) == 2) or (int(column) == 3):
        break
    if turn%2 == 1:
        mark = "X"
    elif turn%2 == 0:
        mark = "O"
    if row == "Top":
      if topRow[int(column) - 1] != "-":
        print("Place already taken. Pick again.")
        while (row != "Top") or (row!= "Middle") or (row != "Bottom"):
          row = input("Which row do you want to place the mark on the board? Top, Middle, or Bottom: ")
          if (row == "Top") or (row == "Middle") or (row == "Bottom"):
            break
        while (column != 1) or (column != 2) or (column != 3):
          column = input("Which column do you want to place the mark on the board? 1, 2, or 3: ")
          if (int(column) == 1) or (int(column) == 2) or (int(column) == 3):
            break
        topRow[int(column) - 1] = mark
      else:
          topRow[int(column) - 1] = mark
    elif row == "Middle":
      if middleRow[int(column) - 1] != "-":
        print("Place already taken. Pick again.")
        while (row != "Top") or (row!= "Middle") or (row != "Bottom"):
          row = input("Which row do you want to place the mark on the board? Top, Middle, or Bottom: ")
          if (row == "Top") or (row == "Middle") or (row == "Bottom"):
            break
        while (column != 1) or (column != 2) or (column != 3):
          column = input("Which column do you want to place the mark on the board? 1, 2, or 3: ")
          if (int(column) == 1) or (int(column) == 2) or (int(column) == 3):
            break
        middleRow[int(column) - 1] = mark
      else:
        middleRow[int(column) - 1] = mark
    elif row == "Bottom":
      if bottomRow[int(column) - 1] != "-":
        print("Place already taken. Pick again.")
        while (row != "Top") or (row!= "Middle") or (row != "Bottom"):
          row = input("Which row do you want to place the mark on the board? Top, Middle, or Bottom: ")
          if (row == "Top") or (row == "Middle") or (row == "Bottom"):
            break
        while (column != 1) or (column != 2) or (column != 3):
          column = input("Which column do you want to place the mark on the board? 1, 2, or 3: ")
          if (int(column) == 1) or (int(column) == 2) or (int(column) == 3):
            break
        bottomRow[int(column) - 1] = mark
      else:
        bottomRow[int(column) - 1] = mark

board()

while checkWin() == "false":
    turn = turn + 1
    if turn%2 == 1:
        print("Player1 turn: ")
        placeMark()
        board()
    elif turn%2 == 0:
        print("Player2 turn: ")
        placeMark()
        board()
