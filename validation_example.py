"""
Try and merge this with chronos GUI so that Entry Fields have appropriate character limits.
# sophisticated solution: https://www.pythontutorial.net/tkinter/tkinter-validation/
"""

import tkinter as tk
from tkinter import ttk


class ValidateSingleEntry(ttk.Frame):

    def __init__(self, parent: tk.Tk, width: int, fg="black", bg="white"):
        ttk.Frame.__init__(self, parent)
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
            foreground=fg,
            background=bg,
        )
        self.entry.pack()

    def validate(self, d, P):  # i = index, S = insert character, d = action, P = entry value
        if len(P) == self.width and d != 0:
            self.entry.tk_focusNext().focus()
        elif len(P) > self.width:
            self.bell()
            return False
        return True


def time_input(parent):
    entry1 = ValidateSingleEntry(parent, width=2)
    entry2 = ValidateSingleEntry(parent, width=2)
    entry3 = ValidateSingleEntry(parent, width=2)
    entry4 = ValidateSingleEntry(parent, width=3)

    # layout
    entry1.grid(row=1, column=1)
    entry2.grid(row=1, column=3)
    entry3.grid(row=1, column=5)
    entry4.grid(row=1, column=7)


def main2():
    window = tk.Tk()
    time_input(window)
    window.mainloop()


if __name__ == "__main__":
    main2()
