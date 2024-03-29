from textual.reactive import reactive
from textual.widgets import Button, Label

from pomotodo.pomodoro.model import Pomodoro, PomodoroMode

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


class PomodoroTimer(Button):
    pomodoro = Pomodoro()
    seconds_remaining = reactive(pomodoro.mode_duration)
    active = False
    BINDINGS = [
        ("space", "start_or_pause", "Start/Pause Timer"),
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
            self.pomodoro.next_mode()
            self.seconds_remaining = self.pomodoro.mode_duration

            message: Label = self.app.query_one("PomodoroMessage")  # type: ignore
            match self.pomodoro.mode:
                case PomodoroMode.WORK:
                    message.update("Time to focus!")
                case PomodoroMode.SHORT_BREAK:
                    message.update("Time for a short break!")
                case PomodoroMode.LONG_BREAK:
                    message.update("Time for a longer break!")

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

        self.seconds_remaining = self.pomodoro.mode_duration

    def action_focus_todo_list(self) -> None:
        self.app.query_one("TodoListView").focus()
