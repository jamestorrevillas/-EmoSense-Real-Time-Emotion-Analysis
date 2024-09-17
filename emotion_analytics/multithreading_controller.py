from PySide6.QtCore import QObject, QRunnable, Slot, Signal
import traceback
from emotion_analytics.emotion_analytics_engine import EmotionAnalyticsEngine

class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    """
    finished = Signal(dict)
    error = Signal(str)

class Worker(QRunnable):
    """
    Worker thread for processing emotion analytics data.

    Inherits from QRunnable to handle worker thread setup, signals and wrap-up.
    """

    def __init__(self, session_factory, user_id, start_date, end_date, selected_emotions, time_frame):
        """
        Initialize the worker with necessary parameters.

        Args:
            session_factory (callable): A factory function to create database sessions.
            user_id (int): The ID of the user whose data is being processed.
            start_date (datetime): The start date of the data range.
            end_date (datetime): The end date of the data range.
            selected_emotions (list): List of emotions to include in the analysis.
            time_frame (str): The time frame for data aggregation ('daily', 'weekly', or 'monthly').
        """
        super().__init__()
        self.session_factory = session_factory
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.selected_emotions = selected_emotions
        self.time_frame = time_frame
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        """
        The main processing method for the worker thread.

        This method is called when the thread starts. It creates a database session,
        initializes the EmotionAnalyticsEngine, prepares the chart data, and emits
        the result or any errors that occur during processing.
        """
        try:
            session = self.session_factory()
            engine = EmotionAnalyticsEngine(session)
            chart_data = self.prepare_chart_data(engine)
            self.signals.finished.emit(chart_data)
        except Exception as e:
            self.signals.error.emit(str(e))
            print(f"Error in ChartWorker: {str(e)}")
            print(traceback.format_exc())
        finally:
            session.close()

    def prepare_chart_data(self, engine):
        """
        Prepare the chart data using the EmotionAnalyticsEngine.

        Args:
            engine (EmotionAnalyticsEngine): An instance of the EmotionAnalyticsEngine.

        Returns:
            dict: The prepared chart data.
        """
        return engine.prepare_chart_data(
            self.user_id,
            self.start_date,
            self.end_date,
            self.selected_emotions,
            self.time_frame
        )

class SummaryWorker(QRunnable):
    """
    Worker thread for generating emotion summary and recommendations.

    Inherits from QRunnable to handle worker thread setup, signals and wrap-up.
    """

    class Signals(QObject):
        """
        Defines the signals available from a running summary worker thread.
        """
        finished = Signal(str)
        error = Signal(str)

    def __init__(self, session_factory, chart_data):
        """
        Initialize the summary worker with necessary parameters.

        Args:
            session_factory (callable): A factory function to create database sessions.
            chart_data (dict): The chart data used to generate the summary and recommendations.
        """
        super().__init__()
        self.session_factory = session_factory
        self.chart_data = chart_data
        self.signals = self.Signals()

    @Slot()
    def run(self):
        """
        The main processing method for the summary worker thread.

        This method is called when the thread starts. It creates a database session,
        initializes the EmotionAnalyticsEngine, generates the summary and recommendations,
        and emits the result or any errors that occur during processing.
        """
        try:
            session = self.session_factory()
            engine = EmotionAnalyticsEngine(session)
            summary = engine.generate_summary_and_recommendations(self.chart_data)
            self.signals.finished.emit(summary)
        except Exception as e:
            self.signals.error.emit(str(e))
        finally:
            session.close()