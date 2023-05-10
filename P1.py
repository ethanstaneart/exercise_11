import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Display a title.
        self.main_window.title('My First GUI')

        # Set the window size using the geometry method.
        self.main_window.geometry("300x200")

        # Enter the tkinter main loop.
        self.main_window.mainloop()


# Create an instance of the MyGUI class.
if __name__ == "__main__":
    my_gui = MyGUI()
