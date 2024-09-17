from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QCheckBox, QVBoxLayout, QGridLayout


class PyToggle(QCheckBox):
    def __init__(
            self,
            old_checkbox,
            width=60,
            height=30,
            bg_color="#777",
            circle_color="#DDD",
            active_color="#011BA1",
            animation_curve=QEasingCurve.InOutCubic,
            animation_duration=300
    ):
        super().__init__(old_checkbox.parent())

        self.old_checkbox = old_checkbox
        self.replace_old_checkbox()

        # Set default parameters
        self.setFixedSize(width, height)
        self.setCursor(Qt.PointingHandCursor)

        # Colors
        self._bg_color = QColor(bg_color)
        self._circle_color = QColor(circle_color)
        self._active_color = QColor(active_color)

        # Animation
        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(animation_duration)

        # Connect state changed signal
        self.stateChanged.connect(self.start_transition)

    def replace_old_checkbox(self):
        parent_widget = self.old_checkbox.parent()
        if parent_widget:
            parent_layout = parent_widget.layout()
            if isinstance(parent_layout, QGridLayout):
                index = parent_layout.indexOf(self.old_checkbox)
                row, column, rowSpan, columnSpan = parent_layout.getItemPosition(index)
                parent_layout.removeWidget(self.old_checkbox)
                parent_layout.addWidget(self, row, column, rowSpan, columnSpan)
            elif parent_layout:
                index = parent_layout.indexOf(self.old_checkbox)
                parent_layout.removeWidget(self.old_checkbox)
                parent_layout.insertWidget(index, self)
            else:
                new_layout = QVBoxLayout(parent_widget)
                new_layout.addWidget(self)
                new_layout.setContentsMargins(0, 0, 0, 0)

        self.old_checkbox.setParent(None)
        self.old_checkbox.deleteLater()

    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def start_transition(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - self.height() + 3)
        else:
            self.animation.setEndValue(3)
        self.animation.start()

    def hitButton(self, pos):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(Qt.NoPen)

        # Calculate the color for the current state
        if self.isChecked():
            bg_color = self._active_color
        else:
            bg_color = self._bg_color

        # Interpolate between the two colors based on circle position
        progress = (self._circle_position - 3) / (self.width() - self.height())
        r = int(self._bg_color.red() * (1 - progress) + self._active_color.red() * progress)
        g = int(self._bg_color.green() * (1 - progress) + self._active_color.green() * progress)
        b = int(self._bg_color.blue() * (1 - progress) + self._active_color.blue() * progress)

        # Draw the background
        p.setBrush(QColor(r, g, b))
        p.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)

        # Draw the circle
        p.setBrush(self._circle_color)
        p.drawEllipse(int(self._circle_position), 3, self.height() - 6, self.height() - 6)

        p.end()