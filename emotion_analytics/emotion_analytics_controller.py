import traceback
from PySide6.QtCore import QObject, QDate, Qt, QThreadPool
from PySide6.QtGui import QTextCharFormat, QColor, QBrush
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel, QSizePolicy
from emotion_analytics.emotion_analytics_engine import EmotionAnalyticsEngine
from emotion_analytics.multithreading_controller import Worker, SummaryWorker
from datetime import timedelta


class EmotionAnalyticsController(QObject):
    """
    Controller class for managing emotion analytics functionality.

    This class handles the interaction between the UI and the emotion analytics engine,
    managing data processing, chart creation, and summary generation.
    """

    def __init__(self, main_window):
        """
        Initialize the EmotionAnalyticsController.

        Args:
            main_window (QMainWindow): The main window of the application.
        """
        super().__init__()
        self.main_window = main_window
        self.ui = self.main_window.emotion_analytics_page
        self.current_time_frame = "Daily"
        self.highlight_format = QTextCharFormat()
        self.highlight_format.setBackground(QBrush(QColor(173, 216, 230)))  # Light blue
        self.highlight_format.setForeground(QBrush(Qt.black))  # Ensure text is visible
        self.engine = EmotionAnalyticsEngine(self.main_window.get_db_session())
        self.setup_connections()
        self.selected_date = QDate.currentDate()
        self.thread_pool = QThreadPool()
        self.setup_chart_container()

        # Connect the main window's resize event
        self.main_window.resizeEvent = self.on_main_window_resize

    def on_main_window_resize(self, event):
        """
        Handle the main window resize event.

        Args:
            event (QResizeEvent): The resize event object.
        """
        self.adjust_text_browser_size()
        # Call the original resize event
        super(self.main_window.__class__, self.main_window).resizeEvent(event)

    def update_summary_text(self, summary):
        """
        Update the summary text in the UI.

        Args:
            summary (str): The summary text to display.
        """
        self.ui.textBrowser_SummaryAndRecommendations.setHtml(summary)
        self.adjust_text_browser_size()

    def setup_connections(self):
        """Set up signal-slot connections for UI elements."""
        self.ui.comboBox_TimeFrame.currentIndexChanged.connect(self.update_time_frame)
        self.ui.calendarWidget_Date.clicked.connect(self.handle_calendar_selection)
        self.ui.comboBox_SelectChart.currentIndexChanged.connect(self.request_chart_update)
        self.setup_emotion_checkboxes()

    def setup_emotion_checkboxes(self):
        """Set up connections for emotion checkboxes."""
        emotion_checkboxes = [
            self.ui.checkBox_Neutral, self.ui.checkBox_Happiness, self.ui.checkBox_Contempt,
            self.ui.checkBox_Surprise, self.ui.checkBox_Anger, self.ui.checkBox_Sadness,
            self.ui.checkBox_Fear, self.ui.checkBox_Disgust
        ]
        for checkbox in emotion_checkboxes:
            checkbox.stateChanged.connect(self.request_chart_update)

    def initialize_ui(self):
        """Initialize the UI components with default values."""
        self.ui.comboBox_TimeFrame.setCurrentIndex(0)  # Set to "Daily" by default
        self.ui.comboBox_SelectChart.setCurrentIndex(0)  # Set to "Line Chart" by default
        self.update_calendar_selection()
        self.update_chart()
        self.update_summary_and_recommendations()

    def update_time_frame(self):
        """Update the time frame based on user selection."""
        self.current_time_frame = self.ui.comboBox_TimeFrame.currentText()
        self.update_calendar_selection()
        self.request_chart_update()

    def clear_all_highlights(self):
        """Clear all highlights from the calendar widget."""
        self.ui.calendarWidget_Date.setDateTextFormat(QDate(), QTextCharFormat())

    def update_calendar_selection(self):
        """Update the calendar selection based on the current time frame."""
        today = QDate.currentDate()
        self.clear_all_highlights()

        if self.current_time_frame == "Daily":
            self.select_and_highlight_daily(today)
        elif self.current_time_frame == "Weekly":
            self.select_and_highlight_weekly(today)
        elif self.current_time_frame == "Monthly":
            self.select_and_highlight_monthly(today)

        self.ui.calendarWidget_Date.updateCells()

    def handle_calendar_selection(self, selected_date):
        """
        Handle user selection of a date in the calendar.

        Args:
            selected_date (QDate): The date selected by the user.
        """
        print(f"Calendar selection: {selected_date}")
        self.clear_all_highlights()
        self.selected_date = selected_date

        if self.current_time_frame == "Daily":
            self.select_and_highlight_daily(selected_date)
        elif self.current_time_frame == "Weekly":
            self.select_and_highlight_weekly(selected_date)
        elif self.current_time_frame == "Monthly":
            self.select_and_highlight_monthly(selected_date)

        self.ui.calendarWidget_Date.updateCells()
        self.request_chart_update()

    def select_and_highlight_daily(self, date):
        """
        Select and highlight a single day in the calendar.

        Args:
            date (QDate): The date to select and highlight.
        """
        self.ui.calendarWidget_Date.setSelectedDate(date.addDays(-1))
        self.ui.calendarWidget_Date.setDateTextFormat(date, self.highlight_format)
        print(f"Selected date (Daily): {date.toString(Qt.ISODate)}")

    def select_and_highlight_weekly(self, date):
        """
        Select and highlight a week in the calendar.

        Args:
            date (QDate): A date within the week to select and highlight.
        """
        start_of_week = date.addDays(-date.dayOfWeek())
        end_of_week = start_of_week.addDays(6)
        self.ui.calendarWidget_Date.setSelectedDate(start_of_week.addDays(-1))
        for i in range(7):
            current_date = start_of_week.addDays(i)
            self.ui.calendarWidget_Date.setDateTextFormat(current_date, self.highlight_format)
        print(f"Selected dates (Weekly): {start_of_week.toString(Qt.ISODate)} to {end_of_week.toString(Qt.ISODate)}")

    def select_and_highlight_monthly(self, date):
        """
        Select and highlight a month in the calendar.

        Args:
            date (QDate): A date within the month to select and highlight.
        """
        start_of_month = QDate(date.year(), date.month(), 1)
        end_of_month = QDate(date.year(), date.month(), date.daysInMonth())
        self.ui.calendarWidget_Date.setSelectedDate(start_of_month.addDays(-1))

        current_date = QDate(start_of_month)
        while current_date <= end_of_month:
            self.ui.calendarWidget_Date.setDateTextFormat(current_date, self.highlight_format)
            current_date = current_date.addDays(1)

        print(f"Selected dates (Monthly): {start_of_month.toString(Qt.ISODate)} to {end_of_month.toString(Qt.ISODate)}")

    def request_chart_update(self):
        """Request an update to the chart based on current selections."""
        try:
            print(f"Updating chart for {self.current_time_frame} view")
            self.show_loading_message()
            self.update_chart()
            self.update_summary_and_recommendations()
        except Exception as e:
            print(f"Error updating chart: {str(e)}")
            print(traceback.format_exc())
            self.display_error_message(f"An error occurred while updating the chart: {str(e)}")

    def setup_chart_container(self):
        """Set up the container for displaying charts."""
        if self.ui.widget_ChartPlaceholder.layout():
            QWidget().setLayout(self.ui.widget_ChartPlaceholder.layout())

        self.chart_layout = QVBoxLayout(self.ui.widget_ChartPlaceholder)
        self.chart_layout.setContentsMargins(0, 0, 0, 0)

        self.message_label = QLabel()
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setStyleSheet("font-size: 16px; color: #333; background-color: white;")
        self.message_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.chart_layout.addWidget(self.message_label)

        self.message_label.hide()

    def show_loading_message(self):
        """Display a loading message while the chart is being generated."""
        self.message_label.setText("Generating chart... Please wait.")
        self.message_label.show()
        if self.chart_layout.count() > 1:
            self.chart_layout.itemAt(1).widget().hide()

    def update_chart(self):
        """Update the chart based on current user selections."""
        current_user = self.main_window.get_current_user()
        if current_user is None:
            self.display_no_user_message("No user selected")
            return

        chart_type = self.ui.comboBox_SelectChart.currentText()
        selected_emotions = self.get_selected_emotions()
        print(f"Updating {chart_type} with emotions: {', '.join(selected_emotions)}")

        user_id = current_user.id
        start_date, end_date = self.get_date_range()
        print(f"Date range: {start_date} to {end_date}")

        session_factory = self.main_window.Session
        worker = Worker(session_factory, user_id, start_date, end_date, selected_emotions, self.current_time_frame.lower())

        worker.signals.finished.connect(self.create_and_update_chart_view)
        worker.signals.error.connect(self.display_error_message)

        self.thread_pool.start(worker)

    def get_date_range(self):
        """
        Get the date range based on the current time frame and selected date.

        Returns:
            tuple: A tuple containing the start date and end date (datetime objects).
        """
        if self.current_time_frame == "Daily":
            start_date = self.selected_date.toPython()
            end_date = start_date
        elif self.current_time_frame == "Weekly":
            start_date = self.selected_date.addDays(-self.selected_date.dayOfWeek()).toPython()
            end_date = start_date + timedelta(days=6)
        elif self.current_time_frame == "Monthly":
            start_date = QDate(self.selected_date.year(), self.selected_date.month(), 1).toPython()
            end_date = QDate(self.selected_date.year(), self.selected_date.month(), self.selected_date.daysInMonth()).toPython()
        return start_date, end_date

    def create_and_update_chart_view(self, chart_data):
        """
        Create and update the chart view based on the provided chart data.

        Args:
            chart_data (dict): The data required to create the chart.
        """
        try:
            chart_view_or_message = self.engine.create_chart_view(chart_data)
            self.update_chart_view(chart_view_or_message)
        except Exception as e:
            self.display_error_message(f"Error creating chart: {str(e)}")

    def update_chart_view(self, chart_view_or_message):
        """
        Update the chart view in the UI.

        Args:
            chart_view_or_message (QChartView or str): The chart view to display or an error message.
        """
        self.message_label.hide()

        if self.chart_layout.count() > 1:
            self.chart_layout.itemAt(1).widget().deleteLater()

        if isinstance(chart_view_or_message, str):
            self.message_label.setText(chart_view_or_message)
            self.message_label.show()
        else:
            self.chart_layout.addWidget(chart_view_or_message)

    def display_no_user_message(self, message):
        """
        Display a message when no user is selected.

        Args:
            message (str): The message to display.
        """
        self.message_label.setText(f"Error: {message}")
        self.message_label.setStyleSheet("color: red; font-size: 16px; background-color: white;")
        self.message_label.show()
        if self.chart_layout.count() > 1:
            self.chart_layout.itemAt(1).widget().hide()

    def get_selected_emotions(self):
        """
        Get the list of emotions selected by the user.

        Returns:
            list: A list of selected emotion names.
        """
        selected_emotions = []
        emotion_checkboxes = {
            self.ui.checkBox_Neutral: "Neutral",
            self.ui.checkBox_Happiness: "Happiness",
            self.ui.checkBox_Contempt: "Contempt",
            self.ui.checkBox_Surprise: "Surprise",
            self.ui.checkBox_Anger: "Anger",
            self.ui.checkBox_Sadness: "Sadness",
            self.ui.checkBox_Fear: "Fear",
            self.ui.checkBox_Disgust: "Disgust"
        }
        for checkbox, emotion in emotion_checkboxes.items():
            if checkbox.isChecked():
                selected_emotions.append(emotion)
        return selected_emotions

    def update_summary_and_recommendations(self):
        """Update the summary and recommendations based on the current chart data."""
        print("Updating summary and recommendations")
        self.ui.textBrowser_SummaryAndRecommendations.setText("Generating summary and recommendations...")
        try:
            current_user = self.main_window.get_current_user()
            if current_user is None:
                raise ValueError("No user selected")

            start_date, end_date = self.get_date_range()

            session_factory = self.main_window.Session
            session = session_factory()
            chart_data = self.engine.create_chart_data(
                current_user.id,
                start_date,
                end_date,
                self.get_selected_emotions(),
                self.current_time_frame.lower()
            )
            session.close()
            print("Chart data created:", chart_data)

            if not chart_data.get('data'):
                raise ValueError("No emotion data available")

            worker = SummaryWorker(session_factory, chart_data)
            worker.signals.finished.connect(self.update_summary_text)
            worker.signals.error.connect(self.handle_summary_error)
            self.thread_pool.start(worker)

        except Exception as e:
            error_message = f"Error preparing summary generation: {str(e)}"
            print(error_message)
            self.ui.textBrowser_SummaryAndRecommendations.setText(error_message)


    def handle_summary_error(self, error):
        """
        Handle errors that occur during summary generation.

        Args:
            error (str): The error message.
        """
        error_message = f"Error generating summary: {error}"
        print(error_message)
        self.ui.textBrowser_SummaryAndRecommendations.setText(error_message)


    def display_error_message(self, message):
        """
        Display an error message in the UI.

        Args:
            message (str): The error message to display.
        """
        print(f"Error: {message}")
        self.message_label.setText(f"Error: {message}")
        self.message_label.setStyleSheet("color: red; font-size: 16px; background-color: white;")
        self.message_label.show()
        if self.chart_layout.count() > 1:
            self.chart_layout.itemAt(1).widget().hide()


    def adjust_text_browser_size(self):
        """Adjust the size of the text browser based on the main window size."""
        # Get the available height in the main window
        available_height = self.main_window.height()

        # Calculate the desired height for the text browser
        # Adjust these values as needed
        margin = 20  # pixels from the bottom of the window
        min_height = 2800  # minimum height in pixels
        max_height = available_height - 100  # maximum height, leaving space for other widgets

        # Set the height of the text browser
        new_height = max(min_height, min(max_height, available_height - margin))
        self.ui.textBrowser_SummaryAndRecommendations.setMinimumHeight(new_height)
        self.ui.textBrowser_SummaryAndRecommendations.setMaximumHeight(new_height)

        # Ensure the text is visible
        self.ui.textBrowser_SummaryAndRecommendations.verticalScrollBar().setValue(0)

