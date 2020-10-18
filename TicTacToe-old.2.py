import tkinter as tk
import sys
import numpy as np


class plate():
    def __init__(self, frame, row, column, color = "gray"):
        self.row = row
        self.column = column
        self.color = color

        self.create_plate(frame)

    def create_plate(self, frame):
        tk.Button(frame, bg = self.color, height =10, width = 20,
                  command = lambda: TicTacToe.turn(self)
                  ).grid(row = self.row, column = self.column)

    def get_position(self):
        return self.row, self.column


class TicTacToe(tk.Frame):
    def __init__ (self, master = None):
        super().__init__(master)
        self.grid()
        self.build_frame()
        
    
    def build_frame(self):
        mainframe = tk.Frame(self, height = 30, width = 60).grid()
        for r in range(3):
            for c in range(3):
                plate(mainframe, r, c)
    
    def turn(self):
        rc_touple = plate.get_position(self)
        plate(mainframe, rc_touple[0], rc_touple[1], color = "red")

        return None

    def track_turn(self):
       return None
    
   # def check_state(self):
        ## returns boolean if a player winds.
    #    return None


def main():
    root = tk.Tk()

    TicTacToe(root)

    tk.mainloop()

if __name__ == "__main__":
    main()