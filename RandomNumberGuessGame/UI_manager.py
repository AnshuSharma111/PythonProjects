import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def homeScreen(frame):
    clearFrame(frame)

    # Heading Label
    heading = ttk.Label(frame, text = "Random Number Guessing Game!", font=("Helvetica", 20))
    heading.pack(pady=20)
    # Play Button
    playButton = ttk.Button(frame, bootstyle="dark", text="Play!", command= lambda : playScreen(frame))
    playButton.pack(pady=50)

def playScreen(frame):
    clearFrame(frame)

    # Heading
    heading = ttk.Label(frame, text = "Guess Number!", font=("Helvetica", 20))
    heading.pack(pady=20)

    # Value input Field
    inputField = ttk.Entry(frame)
    inputField.pack(pady=30)

    # Output Field
    output = ttk.Label(frame, text = "Start Guessing to get Result", font = ("Helvetica", 15))
    output.pack(pady=10)