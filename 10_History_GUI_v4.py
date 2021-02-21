from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class history:
    def __init__(self, partner):

        background = "#a9ef99"    # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE-WINDOW', partial(self.close_history,))


        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # History text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent "
                                                           "calculations. Please use the"
                                                           "export button to create a text"
                                                           "file of all your calculations"
                                                           "for this session",
                                                      wrap=250,
                                                      font="arial 10 italic",
                                                      justify=LEFT, width=40, bg=background, fg="maroon",
                                                      padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here... (row 2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=0, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss button (row 2)
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_history(partner)))
        self.dismiss_button.grid(row=0, column=1)


    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = history()
    root.mainloop()