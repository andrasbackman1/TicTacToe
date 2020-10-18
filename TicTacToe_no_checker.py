import tkinter as tk
import sys
import numpy as np

"""
Need to finish the board checker
"""
class Plate:
    def __init__ (self, frame, row, column, color = "gray"):
        self.row = row
        self.column = column
        self.color = color
        self.frame = frame

        self.create_plate(self.row, self.column)
    
    def create_plate(self, r, c):
        tk.Button(self.frame, bg = self.color, height =10, width = 20,
                  command = lambda: TicTacToe.turn(self)
                  ).grid(row = r, column = c)
    
    def change_color(self, new_color):
        self.color = new_color

    def get_Index(self):
        return self.row, self.column


class TicTacToe:
    def __init__ (self, root):
        self.root = root
        self.mainframe = tk.Frame(self.root).grid()
        self.__create_board()
        
        global turn_lst
        turn_lst = ["red"]

    def __create_board(self):
        for r in range(3):
            for c in range(3):
                Plate(self.mainframe, r, c)
    
    def turn(self):
        Index = Plate.get_Index(self)
        new_color = TicTacToe.__track_turn(self)

        Plate.change_color(self, new_color)
        Plate.create_plate(self, Index[0], Index[1])

    def __track_turn(self):
        # in the Virtual Board:
        # green = 0, red = 1
        if turn_lst[-1] == "green":
            turn_lst.append("red")
            return "red"
        else:
            turn_lst.append("green")
            return "green"
        
       

def main():
    root = tk.Tk()

    TicTacToe(root)

    tk.mainloop()

if __name__ == "__main__":
    main()