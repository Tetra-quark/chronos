import tkinter as tk
from tkinter import ttk
import functools

from gui import ButtonFrame, InputFrame, ResultFrame, calculate_timing, clear_all


def main():
    # Initialise window
    window = tk.Tk()

    window.title("Precision Timing Calculator")
    # window.geometry("300x300")
    window.resizable(width=False, height=False)

    # Split window into three regions
    input_region = ttk.Frame(master=window, height=200)
    button_region = ttk.Frame(master=window, height=100)
    result_region = ttk.Frame(master=window, height=100)

    input_region.grid(row=0, column=0, padx=10)  # padx, pady)
    button_region.grid(row=1, column=0)
    result_region.grid(row=2, column=0, sticky='nesw')

    # Add widgets to each region
    input_frame = InputFrame(input_region)
    result_frame = ResultFrame(result_region)

    ButtonFrame(
        button_region,
        # TODO maybe buttonframe should take input/result_frame as args and these fns should be def in its class?
        calculate=functools.partial(calculate_timing, input_frame=input_frame, result_frame=result_frame),
        clear=functools.partial(clear_all, input_frame=input_frame, result_frame=result_frame),
    )

    # there are three main commands to use with entry
    # - retrieve text: .get()
    # - delete text: .delete()
    # - insert text: .insert()

    # window.update_idletasks()
    window.mainloop()


if __name__ == '__main__':
    main()
