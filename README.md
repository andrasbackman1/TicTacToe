# TicTacToe
 TicTacToe built using python`s tkinter module.


Vey basic setup for a Tic Tac Toe game.

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
became a Plate. I do not know why. I also could not get attributes
from the TicTacToe class. The only solution I found was to declare the 
variable as global -- not a good fix but it works so...

It is very good to practice using classes and objects in this way.
Learned a lot on the way. Will have to figure somthing else out next.
