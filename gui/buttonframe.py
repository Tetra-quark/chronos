import tkinter as tk
from tkinter import ttk
from datetime import timedelta
from typing import Protocol


class InputFramelike(Protocol):

    def calculate_results(self) -> tuple[timedelta, timedelta]:
        ...

    def clear_all(self):
        ...


class ResultFramelike(Protocol):

    def update(self, phase1: timedelta, phase2: timedelta):
        ...

    def clear_all(self):
        ...


class ButtonFrame:

    def __init__(self, master: ttk.Frame | tk.Tk, calculate: callable, clear: callable):
        self.master = master

        self.calculate_button = ttk.Button(
            master=self.master,
            text="Calculate",
            command=calculate
        )

        self.clear_button = ttk.Button(
            master=self.master,
            text="Clear All",
            command=clear,
        )

        self.calculate_button.grid(row=1, column=1, pady=10, padx=10)
        self.clear_button.grid(row=1, column=0, pady=10, padx=10)

        # FIXME Always get this error from this bind usage.
        # self.master.master.bind("<Return>", calculate)

        # Traceback (most recent call last):
        # File "/usr/local/Caskroom/miniconda/base/envs/chronos/lib/python3.10/tkinter/__init__.py", line 1921,
        #   in __call__
        # return self.func(*args)
        # TypeError: calculate_timing() got multiple values for argument 'input_frame'


def calculate_timing(input_frame: InputFramelike, result_frame: ResultFramelike) -> None:
    """Calculate the timing results and update the result frame"""
    phase1, phase2 = input_frame.calculate_results()
    result_frame.update(phase1=phase1, phase2=phase2)


def clear_all(input_frame: InputFramelike, result_frame: ResultFramelike) -> None:
    """Clear all input and result fields"""
    input_frame.clear_all()
    result_frame.clear_all()
