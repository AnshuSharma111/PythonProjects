import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from UI_manager import *

root = ttk.Window(themename="cyborg")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
TITLE = "Random Number Guessing Game"
ICON_PATH = 'RandomNumberGuessGame\icon_1.ico'

root.iconbitmap(ICON_PATH)
root.title(TITLE)
root.geometry(f"{screen_width}x{screen_height}")

homeScreen(root)
root.mainloop()