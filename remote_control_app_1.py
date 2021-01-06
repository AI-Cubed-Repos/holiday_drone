import tkinter as tk
from tello import Tello
from datetime import datetime
from time import sleep

#demo 1 with remote control
#just be able to take it off and land it

def onTakeoffButtonPress():
    takeoffButton.config(state=tk.DISABLED)

    tello.send_command("command")
    tello.send_command("takeoff")
    tello.send_command("land")

    takeoffButton.config(state=tk.ACTIVE)

window = tk.Tk()
window.title("Demo Takeoff and Land")
window.minsize(200, 30)
window.maxsize(400, 500)

demoLabel = tk.Label(window, text="Remote Control for Drones Takeoff")
demoLabel.pack()

takeoffButton = tk.Button(window, text="Take Off", command=onTakeoffButtonPress)
takeoffButton.pack()

tello = Tello()

window.mainloop()