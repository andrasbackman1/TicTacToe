import tkinter as tk
import sys


class Plate():
    def __init__(self, frame, row, column, color = "gray"):
        self.color = color
        
        self.column = column
        self.row = row

        tk.Button(frame, bg = self.color, height =10, width = 20,
                  command = self.change_color).grid(row = self.row, column = self.column)

    def change_color(self):
        self.color = "red"
        print(self.color)



def main():
    root = tk.Tk()
    
    mainframe = tk.Frame(root, height = 30, width = 60)
    mainframe.grid()
    for r in range(3):
        for c in range(3):
            Plate(mainframe, row = r, column = c)
    


   

    tk.mainloop()

if __name__ == "__main__":
    main()
