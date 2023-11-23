"""
Module to calculate differences in times for Show Jumping / CSO events.
Used to correct or retreive lost times
"""

from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class SinglePhaseTimingResult:
    start: datetime
    finish: datetime

    @classmethod
    def from_str(cls, start: str, finish: str):
        return cls(
            start=str_to_datetime(start),
            finish=str_to_datetime(finish),
        )

    @property
    def elapsed(self) -> timedelta:
        return time_difference(self.start, self.finish)


@dataclass
class TwoPhaseTimingResult:
    start: datetime
    inter: datetime
    finish: datetime

    @classmethod
    def from_str(cls, start: str, inter: str, finish: str):
        return cls(
            start=str_to_datetime(start),
            inter=str_to_datetime(inter),
            finish=str_to_datetime(finish),
        )

    @property
    def phase1(self) -> timedelta:
        return time_difference(self.start, self.inter)

    @property
    def phase2(self) -> timedelta:
        return time_difference(self.inter, self.finish)

    def phase_results(self) -> tuple[timedelta, timedelta]:
        return self.phase1, self.phase2


def str_to_datetime(time: str) -> datetime:
    """millisecond timestamp"""
    return datetime.strptime(time, "%H:%M:%S.%f")


def time_difference(first: datetime, second: datetime) -> timedelta:
    """Takes difference between two datetimes"""
    return second - first


def main():
    # times should be in '10:32:07.692'
    start = '00:01:47.812'
    inter = '00:02:34.850'
    finish = '00:03:10.875'

    res = TwoPhaseTimingResult.from_str(start, inter, finish)
    # phase1, phase2 = res.phase_results()

    print(f"First Phase: {res.phase1}")
    print(f"Second Phase: {res.phase2}")


if __name__ == '__main__':
    main()
