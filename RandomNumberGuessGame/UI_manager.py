import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import random

frame = None
def initialise(root):
    global frame
    frame = root
    homeScreen()

def clearFrame():
    for widget in frame.winfo_children():
        widget.destroy()

def submitProceed(l, u, t):
    lr = l.get()
    ur = u.get()
    tr = t.get()

    try:
        lr = int(lr)
    except:
        lr = 10
    try:
        ur = int(ur)
    except:
        ur = 100
    try:
        tr = int(tr)
    except:
        tr = 10

    options = {"lower" : lr, "upper" : ur, "tries" : tr, "randomNumber" : random.randrange(lr, ur)}
    playScreen(options)

def gameEnd(outcome, randNum):
    if not outcome:
        messagebox.showinfo("Lose", f"Game Over! The number was {randNum}")
    else:
        messagebox.showinfo("Won", f"Congratulations! You win!")
    
    homeScreen()
    

def check(userInp, actualVal, outputLabel, triesLeft):
    try:
        userInp = int(userInp)
        tl = int(triesLeft.cget("text")[13:])
        won = False

        triesLeft.config(text=f"Tries Left : {max(0,tl-1)}")
        if tl > 0:
            if userInp == actualVal:
                outputLabel.config(text="Congratulations! You guessed right!")
                won = True
                triesLeft.config(text=f"Tries Left : {tl-1}")
                tl -= 1
                gameEnd(won, actualVal)
            elif userInp < actualVal:
                outputLabel.config(text="You guessed lesser than the actual Number!")
            else:
                outputLabel.config(text="You guessed higher than the actual Number!")

            if tl == 1 and not won:
                outputLabel.config(text="Congratulations! You guessed right!")
                tl -= 1
                gameEnd(False, actualVal)
        else:
            outputLabel.config(text = "Out of tries!")
    except:
        outputLabel.config(text="Please enter an integral value!")
    

def homeScreen():
    clearFrame()

    # Heading Label
    heading = ttk.Label(frame, text = "Random Number Guessing Game!", font=("Helvetica", 20))
    heading.pack(pady=20)
    # Play Button
    playButton = ttk.Button(frame, bootstyle="dark", text="Play!", command= lambda : optionsScreen())
    playButton.pack(pady=50)

def optionsScreen():
    clearFrame()

    # Heading Label
    heading = ttk.Label(frame, text = "Choose Settings", font=("Helvetica", 20))
    heading.pack(pady=20)
    # Range Selector
    rangeText = ttk.Label(frame, text = "Select lower and upper bound", font = ("Helvetica", 15))
    rangeText.pack(pady=10)

    lr = ttk.Label(frame, text = "Lower Range", font = ("Helvetica", 15))
    lowerRange = ttk.Entry(frame)
    lowerRange.insert(END, "10 by default")
    lr.pack(pady=10)
    lowerRange.pack()

    ur = ttk.Label(frame, text = "Upper Range", font = ("Helvetica", 15))
    upperRange = ttk.Entry(frame)
    upperRange.insert(END, "100 by default")
    ur.pack(pady=10)
    upperRange.pack()

    # Number of tries
    triesLabel = ttk.Label(frame, text="Number of Tries", font=("Helvetica", 15))
    triesLabel.pack(pady=10)

    tries = ttk.Entry(frame)
    tries.insert(END, "10 by default")
    tries.pack(pady=10)

    #Submit and proceed
    submitButton = ttk.Button(frame, bootstyle="dark", text="Proceed", command= lambda : submitProceed(lowerRange, upperRange, tries))
    submitButton.pack(pady=50)

def playScreen(options):
    clearFrame()

    print(options)
    # Heading
    heading = ttk.Label(frame, text = "Guess Number!", font=("Helvetica", 20))
    heading.pack(pady=20)

    # Tries left label
    triesText = f"Tries Left : {options['tries']}"
    triesLeft = ttk.Label(frame, text = triesText, font=("Helvetica", 15))
    triesLeft.pack(pady=10)

    # Value input Field
    inputField = ttk.Entry(frame)
    inputField.pack(pady=30)

    # Output Field
    output = ttk.Label(frame, text = "Start Guessing to get Result", font = ("Helvetica", 15))
    output.pack(pady=10)

    # check button
    checkButton = ttk.Button(frame, bootstyle="dark", text="Proceed", command= lambda : check(inputField.get(), options['randomNumber'], output, triesLeft))
    checkButton.pack(pady=50)