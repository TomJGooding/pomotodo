from textual.binding import Binding
from textual.reactive import reactive
from textual.widgets import Button


class CountdownTimer(Button):
    seconds_remaining = reactive(60 * 20)
    active = False
    BINDINGS = [
        Binding(
            "space",
            "start_or_pause",
            "Start/Pause Timer",
            key_display="SPACE",
        )
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

    def watch_seconds_remaining(self, seconds_remaining: int) -> None:
        minutes, seconds = divmod(seconds_remaining, 60)
        self.label = f"{minutes:02}:{seconds:02}"

    def action_start_or_pause(self) -> None:
        if self.active:
            self.update_timer.pause()
            self.active = False
        else:
            self.update_timer.resume()
            self.active = True
