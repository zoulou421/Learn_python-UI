"""
First example with Tkinter.
We create a simple window which welcomes
the user
"""

# We import Tkinter
from tkinter import *

# We create a window, root of our interface
window = Tk()

# We create a label (line of text) welcoming
# Note: the first parameter passed to the Label constructor is our root interface
field_label = Label(window, text="Welcome to FormationKilo !")
field_label["text"]="Welcome to our compagny"

# We display the label in the window
field_label.pack()

# We start the Tkinter loop which is interrupted when we close the window
window.mainloop()





