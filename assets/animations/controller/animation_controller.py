from PySide6.QtCore import QObject, QSequentialAnimationGroup, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QGraphicsOpacityEffect


class AnimationController(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def switch_and_fade_in(self, next_widget):
        current_widget = self.main_window.ui.stackedWidget.currentWidget()

        # Instantly switch to the next widget
        self.main_window.ui.stackedWidget.setCurrentWidget(next_widget)

        # Create and start the fade-in animation
        self._start_fade_in(next_widget)

    def _start_fade_in(self, widget):
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)

        fade_in = QPropertyAnimation(effect, b"opacity")
        fade_in.setDuration(500)  # 500ms duration
        fade_in.setStartValue(0.0)
        fade_in.setEndValue(1.0)
        fade_in.setEasingCurve(QEasingCurve.InOutCubic)

        # Use QSequentialAnimationGroup to ensure the animation completes
        animation_group = QSequentialAnimationGroup(self)
        animation_group.addAnimation(fade_in)
        animation_group.finished.connect(lambda: self._cleanup_effect(widget))
        animation_group.start()

    def _cleanup_effect(self, widget):
        widget.setGraphicsEffect(None)
