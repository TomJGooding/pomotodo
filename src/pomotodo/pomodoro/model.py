from dataclasses import dataclass
from enum import Enum, auto


class PomodoroMode(Enum):
    WORK = auto()
    SHORT_BREAK = auto()
    LONG_BREAK = auto()


@dataclass
class PomodoroDurationSettings:
    work: int = 25 * 60
    short_break: int = 5 * 60
    long_break: int = 15 * 60


class Pomodoro:
    def __init__(
        self,
        work_sessions_count: int = 0,
        mode: PomodoroMode = PomodoroMode.WORK,
        duration_settings: PomodoroDurationSettings = PomodoroDurationSettings(),
    ) -> None:
        self.work_sessions_count: int = work_sessions_count
        self.mode: PomodoroMode = mode
        self.duration_settings: PomodoroDurationSettings = duration_settings

    @property
    def mode_duration(self) -> int:
        match self.mode:
            case PomodoroMode.WORK:
                return self.duration_settings.work
            case PomodoroMode.SHORT_BREAK:
                return self.duration_settings.short_break
            case PomodoroMode.LONG_BREAK:
                return self.duration_settings.long_break

    def next_mode(self) -> None:
        match self.mode:
            case PomodoroMode.WORK:
                self.work_sessions_count += 1
                if self.work_sessions_count % 4 == 0 and self.work_sessions_count != 0:
                    self.mode = PomodoroMode.LONG_BREAK
                else:
                    self.mode = PomodoroMode.SHORT_BREAK
            case PomodoroMode.SHORT_BREAK | PomodoroMode.LONG_BREAK:
                self.mode = PomodoroMode.WORK
