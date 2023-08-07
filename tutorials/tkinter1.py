# import everything in tkinter library
# the star means all or everything
from tkinter import *

# Tk is like the window
window = Tk()
# window.title("<window name>"")
window.title("First Window")
# size and position window.geometry(<width> x <hieght> + <x> + <y>)
window.geometry("500x450+75+100")

# Entry is like input
name_entry = Entry(
    # first thing is the window it will show on
    window,
    # then inside here you can put your entry properties
    width = 25,
    font = (
        # font name
        "Arial",
        # font size
        25,
        # style like (bold,italic,underline)
        "bold"
    )
)

# just show it in med top of the screen
name_entry.pack()

# mainloop is the run command to show the window
window.mainloop()