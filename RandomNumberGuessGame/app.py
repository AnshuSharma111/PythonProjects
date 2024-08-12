import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

root = ttkb.Window(themename="cyborg")
root.iconbitmap('RandomNumberGuessGame\icon_1.ico')
root.geometry('1000x700')
root.title("Random Number Guessing Game")

root.mainloop()