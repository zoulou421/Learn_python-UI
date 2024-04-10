from tkinter import *

class MyKiloInterface(Frame):
    """Our main window.
    All widgets are stored as attributes of this window."""

    def __init__(self, window, **kwargs):
        Frame.__init__(self,window,width=768,height=576,**kwargs)
        self.pack(fill=BOTH)
        self.nb_click=0

        # Creation of our widgets
        self.message=Label(self, text="You did not click the button.")
        self.message.pack()

        self.bouton_quit=Button(self, text="Quit",command=self.quit)
        self.bouton_quit.pack(side="left")

        self.bouton_click = Button(self, text="Click here",fg="red",command=self.my_click)
        self.bouton_click.pack(side="right")

    def my_click(self):
        """There was a click of the button.
        We change the value of the message label."""
        self.nb_click += 1
        self.message["text"] = "You clicked {} times.".format(self.nb_click)




# MyKiloInterface test class in the file
if __name__ == "__main__":
    window1=Tk()
    interface = MyKiloInterface(window1)
    interface.mainloop()

    interface.destroy()

    #explaination in order:
    '''
     In order :
     1. We create a class which will contain the entire window. This class inherits from Frame, that is, a Tkinter frame.
     2. In the window constructor, we call the frame constructor and pack (position and display) the frame.
     3. Still in the constructor, we create the different window widgets. We also position and display them.
     4. We create a click_button method, which is called when we click on the click_button. She doesn't take
        no settings. It will update the text contained in the self.message label to display the number of clicks
        recorded on the button.
     5. We create the window Tk which is the parent object of the interface which we then instantiate.
     6. We enter the mainloop. It will stop when you close the window.
     7. Then, we destroy the window using the destroy method...
    '''






