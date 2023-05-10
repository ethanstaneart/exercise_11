import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create three Button widgets with different positive quotes
        self.button1 = tkinter.Button(self.main_window, text='Quote 1', command=self.show_quote1)
        self.button2 = tkinter.Button(self.main_window, text='Quote 2', command=self.show_quote2)
        self.button3 = tkinter.Button(self.main_window, text='Quote 3', command=self.show_quote3)

        # Pack the Buttons
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

        # Enter the tkinter main loop
        self.main_window.mainloop()

    def show_quote1(self):
        tkinter.messagebox.showinfo('Quote 1', 'Believe you can and you\'re halfway there.')

    def show_quote2(self):
        tkinter.messagebox.showinfo('Quote 2', 'Live, Laugh, Love.')

    def show_quote3(self):
        tkinter.messagebox.showinfo('Quote 3', 'You\'re okay. <3')

# Create an instance of the MyGUI class
if __name__ == "__main__":
    my_gui = MyGUI()
