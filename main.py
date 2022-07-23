from tkinter import *
from starting_window import StartWindow
from van_tonder import VanTonderEquation
from cooper_jacob import CooperJacobEquation

BACKGROUND_COLOR = "#f1faee"
WINDOW_TITLE = "CaliYield"


# ---------------------------------- Van Tonder Equation --------------------- #
def van_tonder():
    van = VanTonderEquation()
    van.config(padx=20, pady=20)
    van.van_equation()
    van.entries()
    van.labels()
    van.calculate_button()

# --------------------------------- Cooper Jacobs Equation ---------------------
def cooper_jacob():
    cooper = CooperJacobEquation()
    cooper.config(padx=20, pady=20)
    cooper.labels()
    cooper.entries()
    cooper.buttons()
    cooper.cooper_equation()

# ---------------------------------- UI SETUP -------------------------------- #
# Setting up the main window
window = StartWindow(200, 150)
window.title(WINDOW_TITLE)
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

# Setting Up the Labels For the Main Window
title_label = Label(window, text="CaliYield", font=("courier", 20, "normal"), bg=BACKGROUND_COLOR, fg="black")
title_label.grid(row=0, column=0)

#Creating Buttons
van_tonder = Button(window, text="Van Tonder Equation", width=18, command=van_tonder)
van_tonder.grid(row=1, column=0, pady=10)
cooper_jacob = Button(window, text="Cooper Jacobs Equation", command=cooper_jacob)
cooper_jacob.grid(row=2, column=0)


window.mainloop()
