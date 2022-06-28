import tkinter
from tkinter import *
import random
from PIL import ImageTk, Image  

colors = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
timeleft = 60
score = 0
disp_color = ' '

def startGame():
    global disp_color 
    # if time left is equal to 60sec the countdown starts      
    if timeleft == 60:
        countdown()
        disp_color = random.choice(colors).lower()
        disp_word.config(text=random.choice(colors), fg=disp_color)
        # to change the colors when pressed enter
        entry_box.bind('<Return>', nextColour)  

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        time_label.config(text = "Time left: "+str(timeleft))
        # after 1s = 1000 ms run the function again till the timeleft becomes less than 0
        time_label.after(1000, countdown)
        if (timeleft == 0):
            time_label.config(text = "Game Over!!!")

def nextColour(event):
    global score
    global disp_color
    if timeleft>0:
        #if the time left is greater than 0, make the entry box active
        entry_box.focus_set()
        # if the color typed in the entry box is equal to the colour of the text
        if disp_color == entry_box.get().lower():
            score += 1  
            #update the score
            score_label.config(text = "Your Score: "+str(score))
        # If the color typed and the colour of the text does not match decrement the score
        else:
            score -=1
            #update the score
            score_label.config(text = "Your Score: "+str(score))
        # clear the text entry box
        entry_box.delete(0, END)
        # change the color to type, by changing the text and the colour to a random colour value
        disp_color = random.choice(colors).lower()
        disp_word.config(text = random.choice(colors), fg = disp_color)

def resetGame():
    global timeleft, score, disp_color
    timeleft = 60
    score = 0
    disp_color = ''
    score_label.config(text = "Your Score : " + str(score))
    disp_word.config(text = '') 
    entry_box.delete(0, END)


# Create a GUI window
root = tkinter.Tk()
root.geometry("360x200")
root.title("Colour Game")

img = Image.open('pic2.png') 
bg = ImageTk.PhotoImage(img)
label = Label(root, image = bg)
label.place(x=0, y=0)

instructions = tkinter.Label(root, text = "Type the color of the word and not the word text!", font = ("comicsansms",13), bg = "light green", fg = "green")
instructions.pack()

score_label = tkinter.Label(root, text = "Your Score: "+str(score), font = ("comicsansms",13), bg='pink', fg = 'purple')
score_label.pack()

time_label = tkinter.Label(root, text = "Time Left: "+str(timeleft), font = ("comicsansms",13), bg = 'yellow', fg='orange')
time_label.pack()

# Add a label for displaying the colors	
disp_word = tkinter.Label(root, font = ("comicsansms", 13))
disp_word.pack()

# Add a text entry box for typing the colors
entry_box = tkinter.Entry(root, bg = "cyan")
entry_box.pack()

start_button = Button(root, text = "Start", font = ("comicsansms", 13), bg='green', command = startGame)
start_button.pack()

reset_button = Button(root, text = "Reset", font = ("comicsansms", 13), bg = 'blue',command = resetGame)
reset_button.pack()

# set focus on entry box
entry_box.focus_set()

# start of GUI
root.mainloop()