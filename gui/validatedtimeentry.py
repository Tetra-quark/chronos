"""
Validated Time Entry class.
Bunch of width validated entries that make up a timestamp.
Also focuses on the next entry when the current entry is filled.
"""

import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
from datetime import datetime


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

    def get(self) -> str:
        if self.entry.get() == "":
            return "0"  # TODO rethink this
        return self.entry.get()


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

    def get_hmsms(self) -> tuple[str, str, str, str]:
        return (
            self.hours.get(),
            self.minutes.get(),
            self.seconds.get(),
            self.milliseconds.get(),
        )

    @staticmethod
    def join_timestamp_str(h: str, m: str, s: str, ms: str) -> str:
        """Joins individual hour, minute, second, millisecond strings into one timestamp string"""
        return f"{h}:{m}:{s}.{ms}"

    def time(self) -> datetime:
        """Returns datetime object from timestamp string"""
        timestamp = self.join_timestamp_str(*self.get_hmsms())
        return datetime.strptime(timestamp, "%H:%M:%S.%f")

    def clear_all(self):
        self.hours.entry.delete(0, 'end')  # tk.END?
        self.minutes.entry.delete(0, 'end')
        self.seconds.entry.delete(0, 'end')
        self.milliseconds.entry.delete(0, 'end')


def example(master: tk.Tk):

    start = ValidatedTimeEntry(
        master=master,
        text_color="blue",
    )
    start.position(row=0)

    inter = ValidatedTimeEntry(
        master=master,
        text_color="black",
    )
    inter.position(row=1)

    finish = ValidatedTimeEntry(
        master=master,
        text_color="magenta",
    )
    finish.position(row=2)


if __name__ == "__main__":
    window = tk.Tk()
    example(master=window)
    window.mainloop()
