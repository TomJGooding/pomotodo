from dataclasses import dataclass
from enum import Enum, auto


class PomodoroMode(Enum):
    WORK = auto()
    SHORT_BREAK = auto()
    LONG_BREAK = auto()


@dataclass
class PomodoroDurations:
    work: int = 25 * 60
    short_break: int = 5 * 60
    long_break: int = 15 * 60


class Pomodoro:
    def __init__(
        self,
        mode: PomodoroMode = PomodoroMode.WORK,
        durations: PomodoroDurations = PomodoroDurations(),
    ) -> None:
        self.mode: PomodoroMode = mode
        self.durations: PomodoroDurations = durations

    @property
    def timer_seconds(self) -> int:
        match self.mode:
            case PomodoroMode.WORK:
                return self.durations.work
            case PomodoroMode.SHORT_BREAK:
                return self.durations.short_break
            case PomodoroMode.LONG_BREAK:
                return self.durations.long_break

    def next_mode(self) -> None:
        match self.mode:
            case PomodoroMode.WORK:
                self.mode = PomodoroMode.SHORT_BREAK
            case PomodoroMode.SHORT_BREAK:
                self.mode = PomodoroMode.WORK
            case PomodoroMode.LONG_BREAK:
                raise NotImplementedError
