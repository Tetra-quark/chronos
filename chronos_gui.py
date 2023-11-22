import tkinter as tk
from datetime import timedelta
from tkinter import ttk
from string import Template
import chronos


class DeltaTemplate(Template):
    delimiter = "%"


def strfdelta(tdelta: timedelta, fmt: str):
    """Convert a timedelta object into a custom-formatted string"""
    d = {"D": tdelta.days}
    hours, rem = divmod(tdelta.total_seconds(), 3600)
    minutes, precise_sec = divmod(rem, 60)
    seconds, milliseconds = divmod(precise_sec, 1)
    d["H"] = str(round(hours)).zfill(2)
    d["M"] = str(round(minutes)).zfill(2)
    d["S"] = str(round(seconds)).zfill(2)
    d["f"] = str(round(milliseconds * 1e3)).zfill(3)
    t = DeltaTemplate(fmt)
    return t.substitute(**d)


def main():
    # Initialise window
    window = tk.Tk()

    window.title("Precision Timing Calculator")
    # window.geometry("300x300")
    window.resizable(width=False, height=False)

    # Initialise and position frames
    input_frame = ttk.Frame(master=window, height=200)
    button_frame = ttk.Frame(master=window, height=100)
    result_frame = ttk.Frame(master=window, height=100)

    input_frame.grid(row=0, column=0, padx=10)  # padx, pady)
    button_frame.grid(row=1, column=0)
    result_frame.grid(row=2, column=0, sticky='nesw')

    start_h = ttk.Entry(master=input_frame, foreground="blue", background="white", width=2)
    start_m = ttk.Entry(master=input_frame, foreground="blue", background="white", width=2)
    start_s = ttk.Entry(master=input_frame, foreground="blue", background="white", width=2)
    start_ms = ttk.Entry(master=input_frame, foreground="blue", background="white", width=3)

    inter_h = ttk.Entry(master=input_frame, foreground="black", background="white", width=2)
    inter_m = ttk.Entry(master=input_frame, foreground="black", background="white", width=2)
    inter_s = ttk.Entry(master=input_frame, foreground="black", background="white", width=2)
    inter_ms = ttk.Entry(master=input_frame, foreground="black", background="white", width=3)

    finish_h = ttk.Entry(master=input_frame, foreground="magenta", background="white", width=2)
    finish_m = ttk.Entry(master=input_frame, foreground="magenta", background="white", width=2)
    finish_s = ttk.Entry(master=input_frame, foreground="magenta", background="white", width=2)
    finish_ms = ttk.Entry(master=input_frame, foreground="magenta", background="white", width=3)

    entries = [start_h, start_m, start_s, start_ms, inter_h, inter_m, inter_s, inter_ms, finish_h, finish_m, finish_s,
               finish_ms]

    # timestring = ttk.Entry(master=input_frame, foreground="blue", background="white", width=5)

    # process input
    start_label = ttk.Label(master=input_frame, text="START: ")
    inter_label = ttk.Label(master=input_frame, text="INTER: ")
    finish_label = ttk.Label(master=input_frame, text="FINISH: ")

    colon = [ttk.Label(master=input_frame, text=":") for _ in range(6)]
    fullstop = [ttk.Label(master=input_frame, text=".") for _ in range(3)]

    hr_label = ttk.Label(master=input_frame, text="hr")
    min_label = ttk.Label(master=input_frame, text="min")
    sec_label = ttk.Label(master=input_frame, text="sec")
    ms_label = ttk.Label(master=input_frame, text="ms")

    hr_label.grid(row=0, column=1)  # , sticky="w")N.E.S.W.
    min_label.grid(row=0, column=3)
    sec_label.grid(row=0, column=5)
    ms_label.grid(row=0, column=7)

    start_label.grid(row=1, column=0)
    inter_label.grid(row=2, column=0)
    finish_label.grid(row=3, column=0)

    colon[0].grid(row=1, column=2)
    colon[1].grid(row=2, column=2)
    colon[2].grid(row=3, column=2)
    colon[3].grid(row=1, column=4)
    colon[4].grid(row=2, column=4)
    colon[5].grid(row=3, column=4)
    fullstop[0].grid(row=1, column=6)
    fullstop[1].grid(row=2, column=6)
    fullstop[2].grid(row=3, column=6)

    start_h.grid(row=1, column=1)  # , sticky="w")N.E.S.W.
    start_m.grid(row=1, column=3)
    start_s.grid(row=1, column=5)
    start_ms.grid(row=1, column=7)

    inter_h.grid(row=2, column=1)  # , sticky="w")N.E.S.W.
    inter_m.grid(row=2, column=3)
    inter_s.grid(row=2, column=5)
    inter_ms.grid(row=2, column=7)

    finish_h.grid(row=3, column=1)  # , sticky="w")N.E.S.W.
    finish_m.grid(row=3, column=3)
    finish_s.grid(row=3, column=5)
    finish_ms.grid(row=3, column=7)

    def calculate_timing():
        valid_entries = [0 if entry.get() == "" else entry.get() for entry in entries]

        kwarg_labels = ["h", "m", "s", "ms"]
        start_kwargs = dict(zip(kwarg_labels, valid_entries[:4]))
        inter_kwargs = dict(zip(kwarg_labels, valid_entries[4:8]))
        finish_kwargs = dict(zip(kwarg_labels, valid_entries[8:]))

        start = chronos.timestamp_str(**start_kwargs)
        inter = chronos.timestamp_str(**inter_kwargs)
        finish = chronos.timestamp_str(**finish_kwargs)

        phase1, phase2 = chronos.chrono(start=start, inter=inter, finish=finish)

        phase1_result_label["text"] = strfdelta(phase1, "%H:%M:%S.%f")
        phase2_result_label["text"] = strfdelta(phase2, "%H:%M:%S.%f")
        return

    # also enable enter key detection
    calculate_button = ttk.Button(
        master=button_frame,
        text="Calculate",
        command=calculate_timing)

    def clear_input():
        # clear data input
        for entry in entries:
            entry.delete(0, tk.END)

        # clear result
        phase1_result_label['text'] = "00:00:00.000"
        phase2_result_label['text'] = "00:00:00.000"
        return

    clear_button = ttk.Button(
        master=button_frame,
        text="Clear All",
        command=clear_input)

    calculate_button.bind("<Button-1>", calculate_timing)
    window.bind("<Return>", calculate_timing)

    calculate_button.grid(row=1, column=1, pady=10, padx=10)
    clear_button.grid(row=1, column=0, pady=10, padx=10)

    phase1_result_label = ttk.Label(
        master=result_frame,
        text="00:00:00.000",
        foreground="green",
        background="black",
        padding=(80, 5),

    )

    phase2_result_label = ttk.Label(
        master=result_frame,
        text="00:00:00.000",
        foreground="green",
        background="black",
        padding=(80, 5),
    )

    phase1_result_label.config(font=("TkFixedFont", 24))
    phase2_result_label.config(font=("TkFixedFont", 24))

    phase1_label = ttk.Label(
        master=result_frame,
        text="Phase 1",
        foreground="red",
        background="black",
        padding=(80, 0),
    )

    phase2_label = ttk.Label(
        master=result_frame,
        text="Phase 2",
        foreground="red",
        background="black",
        padding=(80, 0),
    )

    phase1_label.config(font=("TkDefaultFont", 14))
    phase2_label.config(font=("TkDefaultFont", 14))

    phase1_label.grid(row=0, column=0, sticky="nesw")
    phase2_label.grid(row=2, column=0, sticky="nesw")

    phase1_result_label.grid(row=1, column=0, sticky="nesw")
    phase2_result_label.grid(row=3, column=0, sticky="nesw")

    # TODO or I could physically inser the : & . in hh:mm:ss.fff using the .insert() method?

    # there are three main commands to use with entry
    # - retrieve text: .get()
    # - delete text: .delete()
    # - insert text: .insert()

    # window.update_idletasks()
    window.mainloop()


if __name__ == '__main__':
    main()
