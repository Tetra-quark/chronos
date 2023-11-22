"""
Try and merge this with chronos GUI so that Entry Fields have appropriate character limits.
# sophisticated solution: https://www.pythontutorial.net/tkinter/tkinter-validation/
"""

import tkinter as tk
from dataclasses import dataclass
from tkinter import ttk


class ValidatedEntry(ttk.Frame):

    def __init__(self, master: ttk.Frame, width: int, foreground="black", background="white"):
        ttk.Frame.__init__(self, master)
        self.width = width

        # valid percent substitutions (from the Tk entry man page)
        # note: you only have to register the ones you need; this
        # example registers them all for illustrative purposes (not any more)..
        #
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget

        vcmd = (self.register(self.validate), '%d', '%P')
        self.entry = ttk.Entry(
            self,
            width=self.width,
            validate='key',
            validatecommand=vcmd,
            foreground=foreground,
            background=background,
        )
        self.entry.pack()

    def validate(self, d, P):  # i = index, S = insert character, d = action, P = entry value
        if len(P) == self.width and d != 0:
            self.entry.tk_focusNext().focus()
        elif len(P) > self.width:
            self.bell()
            return False
        return True


@dataclass
class ValidatedTimeEntry:
    master: ttk.Frame | tk.Tk
    text_color: str = "black"
    background_color: str = "white"

    def __post_init__(self):
        self.hours = ValidatedEntry(
            master=self.master,
            foreground=self.text_color,
            background=self.background_color,
            width=2,
        )
        self.minutes = ValidatedEntry(
            master=self.master,
            foreground=self.text_color,
            background=self.background_color,
            width=2,
        )
        self.seconds = ValidatedEntry(
            master=self.master,
            foreground=self.text_color,
            background=self.background_color,
            width=2,
        )
        self.milliseconds = ValidatedEntry(
            master=self.master,
            foreground=self.text_color,
            background=self.background_color,
            width=3,
        )

    def position(self, row):
        self.hours.grid(row=row, column=1)
        self.minutes.grid(row=row, column=3)
        self.seconds.grid(row=row, column=5)
        self.milliseconds.grid(row=row, column=7)

        ttk.Label(master=self.master, text=":").grid(row=row, column=2)
        ttk.Label(master=self.master, text=":").grid(row=row, column=4)
        ttk.Label(master=self.master, text=".").grid(row=row, column=6)


def main():
    window = tk.Tk()

    start = ValidatedTimeEntry(
        master=window,
        text_color="blue",
    )
    start.position(row=0)

    inter = ValidatedTimeEntry(
        master=window,
        text_color="black",
    )
    inter.position(row=1)

    stop = ValidatedTimeEntry(
        master=window,
        text_color="magenta",
    )
    stop.position(row=2)

    window.mainloop()


if __name__ == "__main__":
    main()
