import tkinter as tk
import sys
import numpy as np

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