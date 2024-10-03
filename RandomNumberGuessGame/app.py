import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from UI_manager import *
import os

root = ttk.Window(themename="cyborg")

basedir = os.path.dirname(__file__)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
TITLE = "Random Number Guessing Game"
ICON_PATH = os.path.join(basedir, 'icon.ico')

root.iconbitmap(ICON_PATH)
root.title(TITLE)
root.geometry(f"{screen_width}x{screen_height}")

initialise_app(root)
root.mainloop()