# import everything in tkinter library
# the star means all or everything
from tkinter import *

# Tk is like the window
window = Tk()
# window.title("<window name>"")
window.title("First Window")
# size and position window.geometry(<width> x <hieght> + <x> + <y>)
window.geometry("520x450+75+100")

my_label = Label(
    window,
    text = "User Name: ",
    font = (
        # font name
        "Arial",
        # font size
        25,
        # style like (bold,italic,underline)
        "bold"
    )
)

my_label.grid(row = 0, column = 0)

# Entry is like input
name_entry = Entry(
    # first thing is the window it will show on
    window,
    # then inside here you can put your entry properties
    width = 15,
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
name_entry.grid(row = 0,column = 1)

def print_name():
    label = Label(
        window,
        text = name_entry.get(),
        font = (
            "Arial",
            20,
            ""
        )
    )
    label.grid(row=2,column=1)

my_bubtton = Button(
    window,
    text = "print name",
    command = print_name,
    font = (
        "Arial",
        20,
        ""
    )
)
my_bubtton.grid(row = 1,column = 1)

# mainloop is the run command to show the window
window.mainloop()
