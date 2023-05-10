import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create Label widgets containing last name, first name, and age.
        self.label_last_name = tkinter.Label(self.main_window, text='Last Name: Doe')
        self.label_first_name = tkinter.Label(self.main_window, text='First Name: John')
        self.label_age = tkinter.Label(self.main_window, text='Age: 30')

        # Call the Label widget's pack method for each label.
        self.label_last_name.pack()
        self.label_first_name.pack()
        self.label_age.pack()

        # Enter the tkinter main loop.
        self.main_window.mainloop()

# Create an instance of the MyGUI class.
if __name__ == "__main__":
    my_gui = MyGUI()
