import tkinter as tk
import sys
import numpy as np

"""
Vey basic setup for a Tic Tac Toe game.

It is implemented using tkinter.

The actual buttons you push and the board itself are two separate classes.
I decided to separate them because I could not figure out a better
way to store the color and position index of the "plates".

I used numpy to check the state of the board at all times. I 
called it a virtual board. I figure that it would be a lot faster
to use numpy's indexing to check if someone had won than to use
the built in stuctures. Atleast it was alot faster to write
because Numpy is something I am actually somewhat comfortable
working with.

I got the problem that suddenly "self" in the functions for the TicTacToe
became a Plate instance. I do not know why. I also could not get attributes
from the TicTacToe class. The only solution I found was to declare the 
variable as global -- not a good fix but it works so...

It is very good to practice using classes and objects in this way.
Learned a lot on the way. Will have to figure somthing else out next.
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

        self.create_board()

        global virtual_board
        virtual_board = np.full((3,3), np.NaN)
        
        global turn_lst
        turn_lst = ["red"]
    

    def create_board(self):
        for r in range(3):
            for c in range(3):
                Plate(self.mainframe, r, c)
    
    def turn(self):
        Index = Plate.get_Index(self)
        new_color = TicTacToe.track_turn(self)

        Plate.change_color(self, new_color)
        Plate.create_plate(self, Index[0], Index[1])

        # Updates the VB to match the playing one.
        if new_color == "green":
            virtual_board[Index] = 0
        else:
            virtual_board[Index] = 1
        
        TicTacToe.check_board(self)
    
    def track_turn(self):
        # in the Virtual Board:
        # green = 0, red = 1
        if turn_lst[-1] == "green":
            turn_lst.append("red")
            return "red"
        else:
            turn_lst.append("green")
            return "green"
    
    def check_board(self):
        row_condition = np.all(virtual_board == virtual_board[0, :], axis = 1)
        column_condition = np.all(virtual_board == virtual_board[:, 0], axis = 0)

        def diagonal_condition(self, array):
            Major_diag = array.diagonal()
            # Flips the array horizontally and takes major diagonal.
            Minor_diag = np.flip(array, axis = 1).diagonal()

            for a in [Major_diag, Minor_diag]:
                if np.all(a == a[0]):
                    return True
            return False
        
        if np.any(row_condition | column_condition | diagonal_condition(self, virtual_board)):
            TicTacToe.message(self)
        
    def message(self):
        pop_up = tk.Toplevel(bg = "white", width = 300, height = 150)
        t = tk.StringVar()

        t.set("{} won!!".format(turn_lst[-1]))
        text_box = tk.Message(pop_up, textvariable = t)
        text_box.configure(font = ("Courier", 16, "bold"))
        text_box.pack()

def main():
    root = tk.Tk()

    TicTacToe(root)

    tk.mainloop()

if __name__ == "__main__":
    main()