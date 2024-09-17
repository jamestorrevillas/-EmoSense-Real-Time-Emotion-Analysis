from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QGraphicsOpacityEffect


def create_fade_animation(widget, start_value, end_value, duration=100):
    effect = QGraphicsOpacityEffect(widget)
    widget.setGraphicsEffect(effect)

    fade = QPropertyAnimation(effect, b"opacity")
    fade.setDuration(duration)
    fade.setStartValue(start_value)
    fade.setEndValue(end_value)
    fade.setEasingCurve(QEasingCurve.InOutCubic)

    return fade, effect