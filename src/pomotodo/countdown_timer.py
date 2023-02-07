from textual.reactive import reactive
from textual.widgets import Static


class CountdownTimer(Static):
    seconds_remaining = reactive(5)

    def on_mount(self) -> None:
        self.set_interval(1, self.update_seconds_remaining)

    def update_seconds_remaining(self) -> None:
        if self.seconds_remaining > 0:
            self.seconds_remaining -= 1
        else:
            self.app.bell()

    def watch_seconds_remaining(self, seconds_remaining: int) -> None:
        minutes, seconds = divmod(seconds_remaining, 60)
        self.update(f"{minutes:02}:{seconds:02}")
