import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create two Label widgets with solid borders
        self.label1 = tkinter.Label(self.main_window,
                                     text='Hello World!',
                                     borderwidth=1, relief='solid')
        self.label2 = tkinter.Label(self.main_window,
                                     text='This is my GUI program',
                                     borderwidth=1, relief='solid')

        # Create two additional labels with a positive quote
        self.label3 = tkinter.Label(self.main_window,
                                     text='Believe you can',
                                     borderwidth=1, relief='solid')
        self.label4 = tkinter.Label(self.main_window,
                                     text='and you\'re halfway there.',
                                     borderwidth=1, relief='solid')

        # Display the Labels with 20 pixels of horizontal and vertical internal padding
        self.label1.pack(ipadx=20, ipady=20)
        self.label2.pack(ipadx=20, ipady=20)
        self.label3.pack(ipadx=20, ipady=20)
        self.label4.pack(ipadx=20, ipady=20)

        # Enter the tkinter main loop
        self.main_window.mainloop()

# Create an instance of the MyGUI class.
if __name__ == "__main__":
    my_gui = MyGUI()
