from pomotodo.pomodoro.model import Pomodoro, PomodoroMode


def test_pomodoro_timer_property():
    work_pomodoro = Pomodoro(mode=PomodoroMode.WORK)
    short_break_pomodoro = Pomodoro(mode=PomodoroMode.SHORT_BREAK)
    long_break_pomodoro = Pomodoro(mode=PomodoroMode.LONG_BREAK)

    assert work_pomodoro.mode_duration == 25 * 60
    assert short_break_pomodoro.mode_duration == 5 * 60
    assert long_break_pomodoro.mode_duration == 15 * 60


def test_pomodoro_next_mode():
    pomodoro = Pomodoro(work_sessions_count=0, mode=PomodoroMode.WORK)

    pomodoro.next_mode()
    assert pomodoro.work_sessions_count == 1
    assert pomodoro.mode == PomodoroMode.SHORT_BREAK
    pomodoro.next_mode()
    assert pomodoro.mode == PomodoroMode.WORK

    pomodoro.next_mode()
    assert pomodoro.work_sessions_count == 2
    assert pomodoro.mode == PomodoroMode.SHORT_BREAK
    pomodoro.next_mode()
    assert pomodoro.mode == PomodoroMode.WORK

    pomodoro.next_mode()
    assert pomodoro.work_sessions_count == 3
    assert pomodoro.mode == PomodoroMode.SHORT_BREAK
    pomodoro.next_mode()
    assert pomodoro.mode == PomodoroMode.WORK

    pomodoro.next_mode()
    assert pomodoro.work_sessions_count == 4
    assert pomodoro.mode == PomodoroMode.LONG_BREAK
