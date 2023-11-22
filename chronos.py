"""
Module to calculate differences in times for Show Jumping / CSO events.
Used to correct or retreive lost times
"""

from datetime import datetime, timedelta


def str_to_datetime(time: str) -> datetime:
    """millisecond timestamp"""
    return datetime.strptime(time, "%H:%M:%S.%f")


def timestamp_str(h, m, s, ms) -> str:
    """Process input from GUI"""
    return f"{h}:{m}:{s}.{ms}"


def time_diff(first: datetime, second: datetime) -> timedelta:
    """Takes difference between two datetimes"""
    return second - first


def chrono(start: str, inter: str, finish: str) -> (timedelta, timedelta):
    """Returns times for 1st and 2nd phases given the start, inter and finish times."""

    # convert to datetime
    start = str_to_datetime(start)
    inter = str_to_datetime(inter)
    finish = str_to_datetime(finish)

    first_phase = time_diff(start, inter)
    second_phase = time_diff(inter, finish)

    return first_phase, second_phase


def main():
    # times should be in '10:32:07.692'
    start = '00:01:47.879'
    inter = '00:02:34.705'
    finish = '00:03:10.522'

    first_phase, second_phase = chrono(start, inter, finish)

    print(f"First Phase: {first_phase}")
    print(f"Second Phase: {second_phase}")


if __name__ == '__main__':
    main()
