import tkinter as tk
from tkinter import ttk
from datetime import timedelta

import chronos
from gui.validatedtimeentry import ValidatedTimeEntry


class InputFrame:

    def __init__(self, master: ttk.Frame | tk.Tk):
        self.master = master

        # Entries
        self.start_entry = ValidatedTimeEntry(
            master=self.master,
            text_color="blue",
        )
        self.inter_entry = ValidatedTimeEntry(
            master=self.master,
            text_color="black",
        )
        self.finish_entry = ValidatedTimeEntry(
            master=self.master,
            text_color="magenta",
        )

        self.start_entry.position(row=1)
        self.inter_entry.position(row=2)
        self.finish_entry.position(row=3)

        self.add_info_labels()

    def add_info_labels(self):
        # Labels
        start_label = ttk.Label(master=self.master, text="START: ")
        inter_label = ttk.Label(master=self.master, text="INTER: ")
        finish_label = ttk.Label(master=self.master, text="FINISH: ")

        # position
        start_label.grid(row=1, column=0)
        inter_label.grid(row=2, column=0)
        finish_label.grid(row=3, column=0)

        # Labels
        hr_label = ttk.Label(master=self.master, text="hr")
        min_label = ttk.Label(master=self.master, text="min")
        sec_label = ttk.Label(master=self.master, text="sec")
        ms_label = ttk.Label(master=self.master, text="ms")

        # position
        hr_label.grid(row=0, column=1)
        min_label.grid(row=0, column=3)
        sec_label.grid(row=0, column=5)
        ms_label.grid(row=0, column=7)

    def calculate_results(self) -> tuple[timedelta, timedelta]:
        phase1, phase2 = chronos.TwoPhaseTimingResult(
            start=self.start_entry.time(),
            inter=self.inter_entry.time(),
            finish=self.finish_entry.time(),
        ).phase_results()
        return phase1, phase2

    def clear_all(self):
        self.start_entry.clear_all()
        self.inter_entry.clear_all()
        self.finish_entry.clear_all()
