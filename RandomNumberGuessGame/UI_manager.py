import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import random
import pickle
import os

basedir = os.path.dirname(__file__)
DATA_PATH = os.path.join(basedir, 'data.pickle')

frame = None
data = None

def initialise_app(root):
    global frame
    global data
    frame = root

    with open(DATA_PATH, 'rb') as f:
        data = pickle.load(f)
        print(data)

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

def updateStats(outcome, options):
    data['totalPlayed'] += 1

    #update data
    if outcome[0]:
        data['totalWon'] += 1
        data['streak'] += 1
        # calculate score
        score = round(((options['upper'] - options['lower']) / outcome[1]), 2)
        print(score)
        if score > data['highestScore']:
            data['highestScore'] = score
    else:
        data['streak'] = 0
    
    data['winRate'] = round(((data['totalWon']/data['totalPlayed']) * 100), 2)
    with open(DATA_PATH, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def gameEnd(outcome, options):
    if not outcome[0]:
        messagebox.showinfo("Lose", f"Game Over! The number was {options['randomNumber']}")
    else:
        messagebox.showinfo("Won", f"Congratulations! You win!")

    updateStats(outcome, options)
    homeScreen()
    

def check(userInp, options, outputLabel, triesLeft):
    try:
        userInp = int(userInp)
        tl = int(triesLeft.cget("text")[13:])
        won = False

        triesLeft.config(text=f"Tries Left : {max(0,tl-1)}")
        if tl > 0:
            if userInp == options["randomNumber"]:
                outputLabel.config(text="Congratulations! You guessed right!")
                won = True
                triesLeft.config(text=f"Tries Left : {tl-1}")
                tl -= 1
                gameEnd([won, options['tries'] - tl] , options)
            elif userInp < options["randomNumber"]:
                outputLabel.config(text="You guessed lesser than the actual Number!")
            else:
                outputLabel.config(text="You guessed higher than the actual Number!")

            if tl == 1 and not won:
                outputLabel.config(text="Congratulations! You guessed right!")
                tl -= 1
                gameEnd([won, options['tries'] - tl], options)
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
    # Stats Frame
    statsFrame = ttk.Frame(frame)
    statsFrame.pack()
    # Streak
    streak = ttk.Label(statsFrame, text = f"Win Streak : {data['streak']}", font=("Helvetica", 15))
    streak.pack(side=LEFT)
    # Total Games
    games = ttk.Label(statsFrame, text = f"Games Played : {data['totalPlayed']}", font=("Helvetica", 15))
    games.pack(side=LEFT, padx=20)
    # Highest Score
    highScore = ttk.Label(statsFrame, text = f"Highest Score : {data['highestScore']}", font=("Helvetica", 15))
    highScore.pack(side=LEFT, padx=20)
    # Win rate
    winRate = ttk.Label(statsFrame, text = f"Win Rate: {data['winRate']}", font=("Helvetica", 15))
    winRate.pack(side=LEFT, padx=20)

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
    checkButton = ttk.Button(frame, bootstyle="dark", text="Proceed", command= lambda : check(inputField.get(), options, output, triesLeft))
    checkButton.pack(pady=50)