"""
Try and merge this with chronos GUI so that Entry Fields have appropriate character limits.
# sophisticated solution: https://www.pythontutorial.net/tkinter/tkinter-validation/
"""

import tkinter as tk
from tkinter import ttk


class ValidatedEntry(ttk.Frame):

    def __init__(self, parent: tk.Tk, width: int, foreground="black", background="white"):
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


def validated_time_entry(parent, foreground, row):

    ve1 = ValidatedEntry(parent, foreground=foreground, background="white", width=2)
    ve2 = ValidatedEntry(parent, foreground=foreground, background="white", width=2)
    ve3 = ValidatedEntry(parent, foreground=foreground, background="white", width=2)
    ve4 = ValidatedEntry(parent, foreground=foreground, background="white", width=3)

    # layout
    ve1.grid(row=row, column=1)
    ttk.Label(master=parent, text=":").grid(row=row, column=2)
    ve2.grid(row=row, column=3)
    ttk.Label(master=parent, text=":").grid(row=row, column=4)
    ve3.grid(row=row, column=5)
    ttk.Label(master=parent, text=".").grid(row=row, column=6)
    ve4.grid(row=row, column=7)


def main():
    window = tk.Tk()
    validated_time_entry(window,
                         foreground="blue",
                         row=1)
    validated_time_entry(window,
                         foreground="black",
                         row=2)
    validated_time_entry(window,
                         foreground="magenta",
                         row=3)
    window.mainloop()


if __name__ == "__main__":
    main()
