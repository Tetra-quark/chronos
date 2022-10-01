"""
Try and merge this with chronos GUI so that Entry Fields have appropriate character limits. 
"""

import tkinter as tk  # python 3.x
# import Tkinter as tk # python 2.x

class InputFrame(tk.Frame):

    def __init__(self, parent, fg="black", bg="white"):
        tk.Frame.__init__(self, parent)

        hms_width = 2
        ms_width = 3    

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

        vcmd_hms = (self.register(self.onValidate), '%i', 2) # only 2 digit allowed
        vcmd_ms = (self.register(self.onValidate), '%i', 3) # only 3 digits allowed
        self.entry_h = tk.Entry(self, fg=fg, bg=bg, width=hms_width, validate="key", validatecommand=vcmd_hms)
        self.entry_m = tk.Entry(self, fg=fg, bg=bg, width=hms_width, validate="key", validatecommand=vcmd_hms)
        self.entry_s = tk.Entry(self, fg=fg, bg=bg, width=hms_width, validate="key", validatecommand=vcmd_hms)
        self.entry_ms = tk.Entry(self, fg=fg, bg=bg, width=ms_width, validate="key", validatecommand=vcmd_ms)

        self.entry_h.grid(row=1, column=1)
        self.entry_m.grid(row=1, column=3)
        self.entry_s.grid(row=1, column=5)
        self.entry_ms.grid(row=1, column=7)

    def onValidate(self, i, width):
        # Disallow anything but lowercase letters
        if int(i) <= int(width) - 1:
            return True
        else:
            self.bell()
            return False

if __name__ == "__main__":
    window = tk.Tk()
    InputFrame(window, fg="blue").pack(fill="both", expand=True)
    InputFrame(window, fg="black").pack(fill="both", expand=True)
    InputFrame(window, fg="magenta").pack(fill="both", expand=True)
    window.update_idletasks()
    window.mainloop()