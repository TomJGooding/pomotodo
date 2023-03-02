from enum import Enum

from textual.binding import Binding
from textual.reactive import reactive
from textual.widgets import Button

ASCII_NUMBERS: dict[str, str] = {
    "0": "██████\n██  ██\n██  ██\n██  ██\n██████",
    "1": "    ██\n    ██\n    ██\n    ██\n    ██",
    "2": "██████\n    ██\n██████\n██    \n██████",
    "3": "██████\n    ██\n █████\n    ██\n██████",
    "4": "██  ██\n██  ██\n██████\n    ██\n    ██",
    "5": "██████\n██    \n██████\n    ██\n██████",
    "6": "██████\n██    \n██████\n██  ██\n██████",
    "7": "██████\n    ██\n    ██\n    ██\n    ██",
    "8": "██████\n██  ██\n██████\n██  ██\n██████",
    "9": "██████\n██  ██\n██████\n    ██\n██████",
    ":": "  \n██\n  \n██\n  ",
}


class TimerMode(Enum):
    POMODORO = 25 * 60
    SHORT_BREAK = 5 * 60
    LONG_BREAK = 15 * 60


class PomodoroTimer(Button):
    session = TimerMode.POMODORO
    seconds_remaining = reactive(session.value)
    active = False
    BINDINGS = [
        Binding(
            "space",
            "start_or_pause",
            "Start/Pause Timer",
            key_display="SPACE",
        ),
        ("r", "reset", "Reset Timer"),
        ("t", "focus_todo_list", "Todo List"),
    ]

    def on_mount(self) -> None:
        self.update_timer = self.set_interval(
            1, self.update_seconds_remaining, pause=True
        )

    def update_seconds_remaining(self) -> None:
        if self.seconds_remaining > 0:
            self.seconds_remaining -= 1
        else:
            self.app.bell()
            message = self.app.query_one("PomodoroMessage")
            if self.session is TimerMode.POMODORO:
                self.session = TimerMode.SHORT_BREAK
                message.update("Time for a break!")
                self.seconds_remaining = self.session.value
            elif self.session is TimerMode.SHORT_BREAK:
                self.session = TimerMode.POMODORO
                message.update("Time to focus!")
                self.seconds_remaining = self.session.value

    def watch_seconds_remaining(self, seconds_remaining: int) -> None:
        minutes, seconds = divmod(seconds_remaining, 60)
        time_string: str = f"{minutes:02}:{seconds:02}"

        time_display: list[str] = [""] * 5
        for char in time_string:
            ascii_lines: list[str] = ASCII_NUMBERS[char].splitlines()
            for idx, line in enumerate(ascii_lines):
                time_display[idx] += line + " "

        self.label = "\n ".join(time_display)

    def action_start_or_pause(self) -> None:
        if self.active:
            self.update_timer.pause()
            self.active = False
        else:
            self.update_timer.resume()
            self.active = True

    def action_reset(self) -> None:
        if self.active:
            self.update_timer.pause()
            self.active = False

        self.seconds_remaining = self.session.value

    def action_focus_todo_list(self):
        self.app.query_one("TodoList").focus()
