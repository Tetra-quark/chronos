import tkinter as tk
from tkinter import ttk
from string import Template
from datetime import timedelta

ZERO_STR_TIME = "00:00:00.000"


class ResultFrame:

    def __init__(self, master: ttk.Frame | tk.Tk):
        self.master = master

        self.phase1 = ttk.Label(
            master=master,
            text=ZERO_STR_TIME,
            foreground="green",
            background="black",
            padding=(80, 5),
        )

        self.phase2 = ttk.Label(
            master=master,
            text=ZERO_STR_TIME,
            foreground="green",
            background="black",
            padding=(80, 5),
        )

        self.phase1.config(font=("TkFixedFont", 24))
        self.phase2.config(font=("TkFixedFont", 24))

        self.phase1.grid(row=1, column=0, sticky="nesw")
        self.phase2.grid(row=3, column=0, sticky="nesw")

        self.add_info_labels()

    def add_info_labels(self):
        phase1_label = ttk.Label(
            master=self.master,
            text="Phase 1",
            foreground="red",
            background="black",
            padding=(80, 0),
        )

        phase2_label = ttk.Label(
            master=self.master,
            text="Phase 2",
            foreground="red",
            background="black",
            padding=(80, 0),
        )

        phase1_label.config(font=("TkDefaultFont", 14))
        phase2_label.config(font=("TkDefaultFont", 14))

        phase1_label.grid(row=0, column=0, sticky="nesw")
        phase2_label.grid(row=2, column=0, sticky="nesw")

    def clear_all(self):
        self.phase1["text"] = ZERO_STR_TIME
        self.phase2["text"] = ZERO_STR_TIME

    def update(self, phase1, phase2):
        self.phase1["text"] = self.strfdelta(phase1, "%H:%M:%S.%f")
        self.phase2["text"] = self.strfdelta(phase2, "%H:%M:%S.%f")

    class DeltaTemplate(Template):
        """Helper class for strfdelta"""
        delimiter = "%"

    def strfdelta(self, tdelta: timedelta, fmt: str) -> str:
        """Convert a timedelta object into a custom-formatted string"""
        d = {"D": tdelta.days}
        hours, rem = divmod(tdelta.total_seconds(), 3600)
        minutes, precise_sec = divmod(rem, 60)
        seconds, milliseconds = divmod(precise_sec, 1)
        d["H"] = str(round(hours)).zfill(2)
        d["M"] = str(round(minutes)).zfill(2)
        d["S"] = str(round(seconds)).zfill(2)
        d["f"] = str(round(milliseconds * 1e3)).zfill(3)
        t = self.DeltaTemplate(fmt)
        return t.substitute(**d)
