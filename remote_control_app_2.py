import tkinter as tk
from tello import Tello

import tkinter as tk
from tello import Tello
from datetime import datetime
from time import sleep

#demo 1 with remote control
#just be able to take it off and land it

def onTakeoffButtonPress():
    takeoffButton.config(state=tk.DISABLED)
    landButton.config(state=tk.DISABLED)
    tello.send_command("takeoff")
    landButton.config(state=tk.ACTIVE)
    leftButton.config(state=tk.ACTIVE)
    rightButton.config(state=tk.ACTIVE)

def onLandButtonPress():
    landButton.config(state=tk.DISABLED)
    takeoffButton.config(state=tk.DISABLED)
    leftButton.config(state=tk.DISABLED)
    rightButton.config(state=tk.DISABLED)
    tello.send_command("land")
    takeoffButton.config(state=tk.ACTIVE)

def onLeftButtonPress():
    leftButton.config(state=tk.DISABLED)
    tello.send_command("left 20")
    leftButton.config(state=tk.ACTIVE)

def onRightButtonPress():
    rightButton.config(state=tk.DISABLED)
    tello.send_command("right 20")
    rightButton.config(state=tk.ACTIVE)

window = tk.Tk()
window.title("Demo Takeoff and Land")
window.minsize(200, 30)
window.maxsize(400, 500)

leftButton = tk.Button(window, text="  <<  ", command=onLeftButtonPress)
leftButton.grid(row=1, column=1)
leftButton.config(state=tk.DISABLED)

rightButton = tk.Button(window, text="  >>  ", command=onRightButtonPress)
rightButton.grid(row=1, column=2)
rightButton.config(state=tk.DISABLED)

takeoffButton = tk.Button(window, text="Take Off", command=onTakeoffButtonPress)
takeoffButton.grid(row=2, column=1)

landButton = tk.Button(window, text="Land", command=onLandButtonPress)
landButton.grid(row=2, column=2)
landButton.config(state=tk.DISABLED)

tello = Tello()
#tello.send_command("command")

window.mainloop()