import logging
from PySide6.QtCore import QDateTime, Qt
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis, \
    QCategoryAxis
from PySide6.QtGui import QPainter, QColor, QPen
from models.emotion_log import EmotionLog
from datetime import date, datetime, timedelta


class EmotionAnalyticsEngine:
    """
    Engine for analyzing and visualizing emotion data.

    This class provides methods for creating charts, processing emotion logs,
    and generating summaries and recommendations based on emotion data.
    """

    def __init__(self, db_session):
        """
        Initialize the EmotionAnalyticsEngine.

        Args:
            db_session (sqlalchemy.orm.session.Session): The database session for querying emotion logs.
        """
        self.db_session = db_session
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.emotion_colors = {
            "Neutral": "#808080",  # Gray - lack of strong emotion
            "Happiness": "#FFD700",  # Gold - joy and positivity
            "Sadness": "#4169E1",  # Royal Blue - melancholy and calm
            "Anger": "#FF0000",  # Red - intensity and danger
            "Fear": "#800080",  # Purple - mystery and uncertainty
            "Surprise": "#00FFFF",  # Cyan - alertness and energy
            "Disgust": "#008000",  # Green - sickness and aversion
            "Contempt": "#FFA500"  # Orange - intensity and judgment
        }

    def create_chart_data(self, user_id, start_date, end_date, selected_emotions=None, time_frame='daily'):
        """
        Create chart data for the specified user, date range, and emotions.

        Args:
            user_id (int): The ID of the user.
            start_date (datetime): The start date of the data range.
            end_date (datetime): The end date of the data range.
            selected_emotions (list): List of selected emotions to include in the chart.
            time_frame (str): The time frame for data aggregation ('daily', 'weekly', or 'monthly').

        Returns:
            dict: A dictionary containing the chart data.
        """
        self.logger.info(f"Creating {time_frame} chart data for user {user_id} from {start_date} to {end_date}")

        session = self.db_session

        try:
            # Convert date objects to datetime objects if necessary
            if isinstance(start_date, date):
                start_date = datetime.combine(start_date, datetime.min.time())
            if isinstance(end_date, date):
                end_date = datetime.combine(end_date, datetime.max.time())

            # Adjust the date range to match the selected date
            if time_frame == 'daily':
                end_date = start_date.replace(hour=23, minute=59, second=59, microsecond=999999)
            elif time_frame == 'weekly':
                end_date = start_date + timedelta(days=6, hours=23, minutes=59, seconds=59, microseconds=999999)
            elif time_frame == 'monthly':
                next_month = start_date.replace(day=28) + timedelta(days=4)
                end_date = next_month - timedelta(days=next_month.day)
                end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)

            emotions = list(self.emotion_colors.keys())
            colors = [self.emotion_colors[emotion] for emotion in emotions]

            if selected_emotions:
                emotions = [e for e in emotions if e in selected_emotions]
                colors = [self.emotion_colors[e] for e in emotions]

            raw_data = self.fetch_emotion_logs(session, user_id, start_date, end_date)
            processed_data = self.process_emotion_logs(raw_data, emotions, time_frame)

            self.logger.debug(f"Processed data: {processed_data}")

            chart_data = {
                'title': f"Emotion Distribution Over Time ({time_frame.capitalize()})",
                'time_frame': time_frame,
                'start_date': start_date,
                'end_date': end_date,
                'emotions': emotions,
                'colors': colors,
                'data': processed_data
            }

            return chart_data
        finally:
            pass

    def fetch_emotion_logs(self, session, user_id, start_date, end_date):
        """
        Fetch emotion logs for the specified user and date range.

        Args:
            session (sqlalchemy.orm.session.Session): The database session.
            user_id (int): The ID of the user.
            start_date (datetime): The start date of the data range.
            end_date (datetime): The end date of the data range.

        Returns:
            list: A list of EmotionLog objects.
        """
        self.logger.info(f"Fetching emotion logs for user {user_id}")

        query = session.query(EmotionLog).filter(
            EmotionLog.user_id == user_id,
            EmotionLog.created_at >= start_date,
            EmotionLog.created_at <= end_date
        ).order_by(EmotionLog.created_at)

        self.logger.debug(f"SQL Query: {query}")

        logs = query.all()
        self.logger.info(f"Retrieved {len(logs)} log entries")

        return logs

    def process_emotion_logs(self, raw_data, emotions, time_frame):
        """
        Process raw emotion log data into a format suitable for charting.

        Args:
            raw_data (list): List of EmotionLog objects.
            emotions (list): List of emotions to process.
            time_frame (str): The time frame for data aggregation ('daily', 'weekly', or 'monthly').

        Returns:
            dict: Processed emotion data.
        """
        processed_data = {emotion.lower(): {} for emotion in emotions}

        for log in raw_data:
            time_key = self.get_time_key(log.created_at, time_frame)
            for emotion in emotions:
                emotion_lower = emotion.lower()
                if time_key not in processed_data[emotion_lower]:
                    processed_data[emotion_lower][time_key] = []
                processed_data[emotion_lower][time_key].append(getattr(log, emotion_lower))

        # Calculate average intensity for each time key
        for emotion in processed_data:
            for time_key in processed_data[emotion]:
                processed_data[emotion][time_key] = sum(processed_data[emotion][time_key]) / len(processed_data[emotion][time_key])

        self.logger.debug(f"Processed data: {processed_data}")
        return processed_data

    def get_time_key(self, timestamp, time_frame):
        """
        Get the appropriate time key based on the time frame.

        Args:
            timestamp (datetime): The timestamp to process.
            time_frame (str): The time frame ('daily', 'weekly', or 'monthly').

        Returns:
            Various: The time key in the appropriate format for the given time frame.
        """
        if time_frame == 'daily':
            return timestamp.replace(minute=0, second=0, microsecond=0)
        elif time_frame == 'weekly':
            return timestamp.strftime('%a')  # Return day name (Sun, Mon, etc.)
        elif time_frame == 'monthly':
            return timestamp.day  # Return day of the month (1-31)
        else:
            return timestamp.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    def create_emotion_series(self, emotion, data, start_date, end_date, time_frame):
        """
        Create a QLineSeries for a specific emotion.

        Args:
            emotion (str): The name of the emotion.
            data (dict): The processed emotion data.
            start_date (datetime): The start date of the data range.
            end_date (datetime): The end date of the data range.
            time_frame (str): The time frame ('daily', 'weekly', or 'monthly').

        Returns:
            QLineSeries: A series representing the emotion data.
        """
        series = QLineSeries()

        if not start_date or not end_date:
            self.logger.warning(f"Missing start_date or end_date for {emotion}")
            return series

        if time_frame == 'weekly':
            days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
            for i, day in enumerate(days):
                intensity = data.get(day, 0)
                series.append(i, intensity)
        elif time_frame == 'monthly':
            days_in_month = (end_date - start_date).days + 1
            for day in range(1, days_in_month + 1):
                intensity = data.get(day, 0)
                series.append(day - 1, intensity)
        else:
            time_delta = self.get_time_delta(time_frame)
            current_time = start_date
            while current_time <= end_date:
                intensity = data.get(self.get_time_key(current_time, time_frame), 0)
                q_datetime = QDateTime(current_time)
                series.append(q_datetime.toMSecsSinceEpoch(), intensity)
                current_time += time_delta

        return series

    def get_time_delta(self, time_frame):
        """
        Get the time delta for iterating through the date range.

        Args:
            time_frame (str): The time frame ('daily', 'weekly', or 'monthly').

        Returns:
            timedelta: The time delta for the given time frame.
        """
        if time_frame == 'daily':
            return timedelta(hours=1)
        elif time_frame == 'weekly':
            return timedelta(days=1)
        else:  # monthly
            return timedelta(days=1)

    def setup_axes(self, chart, start_date, end_date, time_frame):
        """
        Set up the axes for the chart.

        Args:
            chart (QChart): The chart object.
            start_date (datetime): The start date of the data range.
            end_date (datetime): The end date of the data range.
            time_frame (str): The time frame ('daily', 'weekly', or 'monthly').
        """
        if time_frame == 'weekly':
            axis_x = QCategoryAxis()
            days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
            for i, day in enumerate(days):
                axis_x.append(day, i)
            axis_x.setRange(0, 6)
            axis_x.setLabelsPosition(QCategoryAxis.AxisLabelsPositionOnValue)
        elif time_frame == 'monthly':
            axis_x = QValueAxis()
            days_in_month = (end_date - start_date).days + 1
            axis_x.setRange(1, days_in_month)
            axis_x.setTickCount(min(days_in_month, 10))  # Set a maximum of 10 ticks for readability
            axis_x.setLabelFormat("%d")  # Display as integers
        else:
            axis_x = QDateTimeAxis()
            if time_frame == 'daily':
                axis_x.setFormat("HH:00")
                axis_x.setTickCount(13)  # Show every 2 hours
            axis_x.setRange(QDateTime(start_date), QDateTime(end_date))

        axis_x.setTitleText("Time")
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)

        axis_y = QValueAxis()
        axis_y.setRange(0, 1)
        axis_y.setTitleText("Intensity")
        axis_y.setTickCount(6)  # 0, 0.2, 0.4, 0.6, 0.8, 1.0
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        for series in chart.series():
            series.attachAxis(axis_x)
            series.attachAxis(axis_y)

        self.logger.debug("Chart axes set up completed")

    def prepare_chart_data(self, user_id, start_date, end_date, selected_emotions=None, time_frame='daily'):
        """
        Prepare chart data for the specified user, date range, and emotions.

        Args:
            user_id (int): The ID of the user.
            start_date (datetime): The start date of the data range.
            end_date (datetime): The end date of the data range.
            selected_emotions (list): List of selected emotions to include in the chart.
            time_frame (str): The time frame for data aggregation ('daily', 'weekly', or 'monthly').

        Returns:
            dict: A dictionary containing the prepared chart data.
        """
        self.logger.info(f"Preparing {time_frame} chart data for user {user_id} from {start_date} to {end_date}")

        session = self.db_session

        # Convert date objects to datetime objects if necessary
        if isinstance(start_date, date) and not isinstance(start_date, datetime):
            start_date = datetime.combine(start_date, datetime.min.time())
        if isinstance(end_date, date) and not isinstance(end_date, datetime):
            end_date = datetime.combine(end_date, datetime.max.time())

        # Adjust the date range to match the selected date
        if time_frame == 'daily':
            end_date = start_date.replace(hour=23, minute=59, second=59, microsecond=999999)
        elif time_frame == 'weekly':
            end_date = start_date + timedelta(days=6, hours=23, minutes=59, seconds=59, microseconds=999999)
        elif time_frame == 'monthly':
            next_month = start_date.replace(day=28) + timedelta(days=4)
            end_date = next_month - timedelta(days=next_month.day)
            end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)

        emotions = list(self.emotion_colors.keys())
        colors = list(self.emotion_colors.values())

        if selected_emotions:
            emotions = [e for e in emotions if e in selected_emotions]
            colors = [self.emotion_colors[e] for e in emotions]

        raw_data = self.fetch_emotion_logs(session, user_id, start_date, end_date)
        processed_data = self.process_emotion_logs(raw_data, emotions, time_frame)

        self.logger.debug(f"Processed data: {processed_data}")

        return {
            'data': processed_data,
            'emotions': emotions,
            'colors': colors,
            'start_date': start_date,
            'end_date': end_date,
            'time_frame': time_frame
        }

    def create_chart_view(self, chart_data):
        """
        Create a QChartView based on the provided chart data.

        Args:
            chart_data (dict): The prepared chart data.

        Returns:
            QChartView or str: A QChartView object if successful, or an error message string if there's an issue.
        """
        self.logger.debug(f"Received chart_data: {chart_data}")

        if 'data' not in chart_data:
            self.logger.error("'data' key not found in chart_data")
            return self.create_no_data_message("Error: No data available")

        if not chart_data['data'] or all(len(data) == 0 for data in chart_data['data'].values()):
            return self.create_no_data_message(chart_data.get('time_frame', 'selected'))

        chart = QChart()
        chart.setTitle(chart_data.get('title', 'Emotion Distribution Over Time'))

        for emotion, color in zip(chart_data.get('emotions', []), chart_data.get('colors', [])):
            emotion_data = chart_data['data'].get(emotion.lower(), {})
            if emotion_data:
                series = self.create_emotion_series(emotion, emotion_data,
                                                    chart_data.get('start_date'),
                                                    chart_data.get('end_date'),
                                                    chart_data.get('time_frame'))
                series.setName(emotion)
                pen = QPen(QColor(color))
                pen.setWidth(2)
                series.setPen(pen)
                chart.addSeries(series)
                self.logger.debug(f"Added series for {emotion} with {series.count()} points")

        self.setup_axes(chart, chart_data.get('start_date'), chart_data.get('end_date'), chart_data.get('time_frame'))

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.logger.info(f"Created line chart view with {len(chart.series())} series")
        return chart_view

    def create_no_data_message(self, time_frame):
        """
        Create a message for when no data is available.

        Args:
            time_frame (str): The time frame for which no data is available.

        Returns:
            str: A message indicating that no data is available for the specified time frame.
        """
        return f"No emotion data available for the selected {time_frame} period"

    def generate_summary_and_recommendations(self, chart_data):
        """
        Generate a summary and recommendations based on the chart data.

        Args:
            chart_data (dict): The prepared chart data.

        Returns:
            str: HTML-formatted string containing the summary and recommendations.
        """
        print("Chart data received:", chart_data)

        emotions = chart_data.get('emotions', [])
        data = chart_data.get('data', {})
        time_frame = chart_data.get('time_frame', 'unknown')
        start_date = chart_data.get('start_date', 'unknown')
        end_date = chart_data.get('end_date', 'unknown')

        if not data:
            return "<h2 style='color: red;'>Error: No processed emotion data available.</h2>"

        emotion_summary = {}
        for emotion in emotions:
            emotion_lower = emotion.lower()
            if emotion_lower in data and data[emotion_lower]:
                values = list(data[emotion_lower].values())
                emotion_summary[emotion] = {
                    'avg': sum(values) / len(values),
                    'max': max(values),
                    'min': min(values)
                }

        if not emotion_summary:
            return "No emotion data available for analysis."

        summary = self.generate_emotion_summary(emotion_summary, start_date, end_date, time_frame)

        return f"<div>{summary}</div>"

    def generate_emotion_summary(self, emotion_summary, start_date, end_date, time_frame):
        """
        Generate a detailed summary of emotions based on the provided data.

        Args:
            emotion_summary (dict): Summary statistics for each emotion.
            start_date (datetime): The start date of the analysis period.
            end_date (datetime): The end date of the analysis period.
            time_frame (str): The time frame of the analysis ('daily', 'weekly', or 'monthly').

        Returns:
            str: HTML-formatted string containing the detailed emotion summary.
        """
        styles = """
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
            h2 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
            h3 { color: #2980b9; }
            .emotion-header { color: #e74c3c; font-weight: bold; }
            .emotion-summary { font-weight: bold; }
            .sub-summary { font-style: italic; }
            ul, ol { padding-left: 20px; }
            li { margin-bottom: 10px; }
            table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
        """

        summary = f"{styles}<h2>Comprehensive Emotional Analysis: {start_date.date()} to {end_date.date()} ({time_frame} view)</h2>"

        # Add table
        summary += "<table>"
        summary += "<tr><th>Emotion</th><th>Average (%)</th><th>Summary</th></tr>"
        for emotion, stats in emotion_summary.items():
            avg_percent = stats['avg'] * 100
            intensity_level = self.get_intensity_level(stats['avg'])
            main_summary = self.get_main_summary(emotion, stats['avg'])
            summary += f"<tr><td>{emotion}</td><td>{avg_percent:.2f}%</td><td>{main_summary}</td></tr>"
        summary += "</table>"

        for emotion, stats in emotion_summary.items():
            summary += self.get_detailed_emotion_summary(emotion, stats['avg'])

        return summary

    def get_detailed_emotion_summary(self, emotion, avg_intensity):
        """
        Get a detailed summary for a specific emotion.

        Args:
            emotion (str): The name of the emotion.
            avg_intensity (float): The average intensity of the emotion.

        Returns:
            str: HTML-formatted string containing the detailed emotion summary.
        """
        intensity_level = self.get_intensity_level(avg_intensity)
        main_summary = self.get_main_summary(emotion, avg_intensity)
        sub_summary = self.get_emotion_summary(emotion, intensity_level)

        summary = f"<h3>{emotion} (Intensity: {avg_intensity * 100:.2f}%)</h3>"
        summary += f"<p class='emotion-summary'><strong>Summary:</strong> {main_summary}</p>"
        summary += f"<p class='sub-summary'>{sub_summary}</p>"

        recommendations = self.get_emotion_recommendations(emotion, avg_intensity)
        summary += "<h4>Recommendations:</h4>"
        summary += recommendations

        return summary

    def get_intensity_level(self, avg_intensity):
        """
        Get the intensity level category based on the average intensity.

        Args:
            avg_intensity (float): The average intensity of the emotion.

        Returns:
            str: The intensity level category.
        """
        if avg_intensity < 0.11:
            return "0.00 to 0.10"
        elif avg_intensity < 0.21:
            return "0.11 to 0.20"
        elif avg_intensity < 0.31:
            return "0.21 to 0.30"
        elif avg_intensity < 0.41:
            return "0.31 to 0.40"
        elif avg_intensity < 0.51:
            return "0.41 to 0.50"
        elif avg_intensity < 0.61:
            return "0.51 to 0.60"
        elif avg_intensity < 0.71:
            return "0.61 to 0.70"
        elif avg_intensity < 0.81:
            return "0.71 to 0.80"
        elif avg_intensity < 0.91:
            return "0.81 to 0.90"
        else:
            return "0.91 to 0.99"

    def get_main_summary(self, emotion, avg_intensity):
        """
        Get the main summary for an emotion based on its average intensity.

        Args:
            emotion (str): The name of the emotion.
            avg_intensity (float): The average intensity of the emotion.

        Returns:
            str: A brief summary of the emotion's intensity.
        """
        intensity_level = self.get_intensity_level(avg_intensity)
        summaries = {
            "Neutral": {
                "0.00 to 0.10": "Extreme deviation from neutral",
                "0.11 to 0.20": "Very strong deviation from neutral",
                "0.21 to 0.30": "Strong deviation from neutral",
                "0.31 to 0.40": "Significant deviation from neutral",
                "0.41 to 0.50": "Noticeable deviation from neutral",
                "0.51 to 0.60": "Moderate deviation from neutral",
                "0.61 to 0.70": "Mild deviation from neutral",
                "0.71 to 0.80": "Slightly less neutral",
                "0.81 to 0.90": "Mostly neutral",
                "0.91 to 0.99": "Completely neutral"
            },
            "Happiness": {
                "0.00 to 0.10": "No happiness",
                "0.11 to 0.20": "Slight contentment",
                "0.21 to 0.30": "Mild pleasure",
                "0.31 to 0.40": "Moderate cheerfulness",
                "0.41 to 0.50": "Noticeable happiness",
                "0.51 to 0.60": "Considerable joy",
                "0.61 to 0.70": "High delight",
                "0.71 to 0.80": "Very joyful",
                "0.81 to 0.90": "Extremely happy",
                "0.91 to 0.99": "Ecstatic"
            },
            "Sadness": {
                "0.00 to 0.10": "No sadness",
                "0.11 to 0.20": "Slight melancholy",
                "0.21 to 0.30": "Mild disappointment",
                "0.31 to 0.40": "Moderate unhappiness",
                "0.41 to 0.50": "Noticeable sadness",
                "0.51 to 0.60": "Considerable sorrow",
                "0.61 to 0.70": "High despondency",
                "0.71 to 0.80": "Very sorrowful",
                "0.81 to 0.90": "Extremely sad",
                "0.91 to 0.99": "Devastated"
            },
            "Anger": {
                "0.00 to 0.10": "No anger",
                "0.11 to 0.20": "Slight annoyance",
                "0.21 to 0.30": "Mild irritation",
                "0.31 to 0.40": "Moderate frustration",
                "0.41 to 0.50": "Noticeable anger",
                "0.51 to 0.60": "Considerable rage",
                "0.61 to 0.70": "High fury",
                "0.71 to 0.80": "Very angry",
                "0.81 to 0.90": "Extremely enraged",
                "0.91 to 0.99": "Livid"
            },
            "Fear": {
                "0.00 to 0.10": "No fear",
                "0.11 to 0.20": "Slight unease",
                "0.21 to 0.30": "Mild worry",
                "0.31 to 0.40": "Moderate anxiety",
                "0.41 to 0.50": "Noticeable fear",
                "0.51 to 0.60": "Considerable dread",
                "0.61 to 0.70": "High terror",
                "0.71 to 0.80": "Very fearful",
                "0.81 to 0.90": "Extremely frightened",
                "0.91 to 0.99": "Panic-stricken"
            },
            "Surprise": {
                "0.00 to 0.10": "No surprise",
                "0.11 to 0.20": "Slight curiosity",
                "0.21 to 0.30": "Mild wonder",
                "0.31 to 0.40": "Moderate amazement",
                "0.41 to 0.50": "Noticeable surprise",
                "0.51 to 0.60": "Considerable astonishment",
                "0.61 to 0.70": "High shock",
                "0.71 to 0.80": "Very surprised",
                "0.81 to 0.90": "Extremely stunned",
                "0.91 to 0.99": "Utterly flabbergasted"
            },
            "Disgust": {
                "0.00 to 0.10": "No disgust",
                "0.11 to 0.20": "Slight distaste",
                "0.21 to 0.30": "Mild aversion",
                "0.31 to 0.40": "Moderate repulsion",
                "0.41 to 0.50": "Noticeable disgust",
                "0.51 to 0.60": "Considerable revulsion",
                "0.61 to 0.70": "High loathing",
                "0.71 to 0.80": "Very disgusted",
                "0.81 to 0.90": "Extremely repulsed",
                "0.91 to 0.99": "Utterly revolted"
            },
            "Contempt": {
                "0.00 to 0.10": "No contempt",
                "0.11 to 0.20": "Slight disapproval",
                "0.21 to 0.30": "Mild disdain",
                "0.31 to 0.40": "Moderate scorn",
                "0.41 to 0.50": "Noticeable contempt",
                "0.51 to 0.60": "Considerable derision",
                "0.61 to 0.70": "High mockery",
                "0.71 to 0.80": "Very contemptuous",
                "0.81 to 0.90": "Extremely scornful",
                "0.91 to 0.99": "Utter disdain"
            }
        }
        return summaries.get(emotion, {}).get(intensity_level, "Emotion level not classified")

    def get_emotion_summary(self, emotion, intensity_level):
        """
        Get a detailed summary for an emotion at a specific intensity level.

        Args:
            emotion (str): The name of the emotion.
            intensity_level (str): The intensity level category.

        Returns:
            str: A detailed description of the emotion at the given intensity level.
        """
        summaries = {
            "Neutral": {
                "0.00 to 0.10": "There is no trace of neutrality, only extreme emotional expression. The person's feelings are at their peak intensity, completely dominating their appearance and behavior.",
                "0.11 to 0.20": "Neutrality has all but disappeared, with very intense emotions on display. The person's feelings are unmistakable and highly pronounced.",
                "0.21 to 0.30": "Any semblance of neutrality is largely gone, replaced by strong emotional cues. The person's feelings are now the dominant feature of their expression.",
                "0.31 to 0.40": "Neutrality is now significantly compromised by emotional expression. The person's feelings are clearly visible, despite attempts to maintain composure.",
                "0.41 to 0.50": "The neutral mask is slipping, revealing clear signs of emotion. While still somewhat composed, the person's feelings are becoming increasingly apparent.",
                "0.51 to 0.60": "Emotions are becoming more evident, challenging the neutral expression. The person is visibly struggling to maintain a completely impassive demeanor.",
                "0.61 to 0.70": "The neutral facade is starting to crack, revealing mild emotional cues. Although composed, the person's neutrality is noticeably less pronounced.",
                "0.71 to 0.80": "Some subtle signs of emotion are beginning to show. While still largely neutral, there are faint indications of an underlying feeling.",
                "0.81 to 0.90": "There's a hint of expression, but it's barely noticeable. The person maintains an overall neutral appearance with only the slightest deviation.",
                "0.91 to 0.99": "The person shows no discernible emotional expression. Their face and demeanor appear completely impassive."
            },
            "Happiness": {
                "0.00 to 0.10": "The person shows no signs of happiness or positive emotion. Their expression is completely devoid of joy or pleasure.",
                "0.11 to 0.20": "A faint glimmer of contentment can be detected. The person may have a barely perceptible upward tilt to their mouth corners.",
                "0.21 to 0.30": "Mild pleasure is evident in the person's expression. There might be a subtle softening around the eyes or a slight smile.",
                "0.31 to 0.40": "The person is displaying noticeable signs of cheerfulness. Their smile is more pronounced, and their eyes may be slightly crinkled.",
                "0.41 to 0.50": "Clear happiness is visible on the person's face. They are smiling warmly, with visible teeth and slightly raised cheeks.",
                "0.51 to 0.60": "The person is exhibiting considerable joy in their expression. Their smile is broad, eyes are bright, and they may be starting to laugh.",
                "0.61 to 0.70": "High levels of delight are evident in the person's demeanor. They are likely laughing, with crinkled eyes and raised eyebrows.",
                "0.71 to 0.80": "The person is showing very joyful expressions. They might be grinning widely, laughing heartily, with their whole face engaged in the expression.",
                "0.81 to 0.90": "Extreme happiness is radiating from the person. They are likely beaming with joy, possibly jumping or clapping with excitement.",
                "0.91 to 0.99": "The person is in a state of pure ecstasy. They may be crying tears of joy, laughing uncontrollably, or showing other signs of overwhelming positive emotion."
            },
            "Sadness": {
                "0.00 to 0.10": "The person shows no signs of sadness or negative emotion. Their expression is neutral and doesn't indicate any unhappiness.",
                "0.11 to 0.20": "A slight hint of melancholy can be detected in the person's expression. There might be a barely noticeable downward tilt to their mouth corners.",
                "0.21 to 0.30": "Mild disappointment is visible on the person's face. Their eyes may appear slightly less bright, and their overall expression is somewhat subdued.",
                "0.31 to 0.40": "The person is showing noticeable signs of unhappiness. Their brow might be slightly furrowed, and their smile may have disappeared.",
                "0.41 to 0.50": "Clear sadness is evident in the person's expression. Their eyes may appear downcast, and their mouth might be turned down at the corners.",
                "0.51 to 0.60": "The person is exhibiting considerable sorrow in their demeanor. They might have watery eyes, and their shoulders may be slightly slumped.",
                "0.61 to 0.70": "High levels of despondency are visible in the person's expression. They may be fighting back tears, with a trembling lip or quivering chin.",
                "0.71 to 0.80": "The person is showing very sorrowful expressions. Tears might be flowing, and they may be audibly sniffling or taking shaky breaths.",
                "0.81 to 0.90": "Extreme sadness is evident in the person's entire being. They could be sobbing openly, with their face contorted in grief.",
                "0.91 to 0.99": "The person appears completely devastated. They may be wailing, their body wracked with sobs, showing signs of utter heartbreak or despair."
            },
            "Anger": {
                "0.00 to 0.10": "The person shows no signs of anger or irritation. Their expression is calm and composed.",
                "0.11 to 0.20": "A slight hint of annoyance can be detected in the person's expression. There might be a barely perceptible tightening around their eyes or mouth.",
                "0.21 to 0.30": "Mild irritation is visible on the person's face. Their brow might be slightly furrowed, and their lips may be pressed together.",
                "0.31 to 0.40": "The person is showing noticeable signs of frustration. Their jaw might be clenched, and their eyes may have a harder look.",
                "0.41 to 0.50": "Clear anger is evident in the person's expression. Their eyes may be narrowed, and their nostrils might be slightly flared.",
                "0.51 to 0.60": "The person is exhibiting considerable rage in their demeanor. They might be visibly gritting their teeth, with a reddening face.",
                "0.61 to 0.70": "High levels of fury are visible in the person's expression. They may be glaring intensely, with tense muscles in their face and neck.",
                "0.71 to 0.80": "The person is showing very angry expressions. They might be yelling or shouting, with their face contorted in rage.",
                "0.81 to 0.90": "Extreme anger is radiating from the person. They could be red-faced, possibly shaking with fury, and showing aggressive body language.",
                "0.91 to 0.99": "The person appears completely livid. They may be screaming uncontrollably, possibly engaging in violent gestures or actions."
            },
            "Fear": {
                "0.00 to 0.10": "The person shows no signs of fear or anxiety. Their expression is calm and relaxed.",
                "0.11 to 0.20": "A slight hint of unease can be detected in the person's expression. There might be a barely noticeable tension in their eyes.",
                "0.21 to 0.30": "Mild worry is visible on the person's face. Their eyebrows might be slightly raised, and they may be more alert than usual.",
                "0.31 to 0.40": "The person is showing noticeable signs of anxiety. Their eyes might be wider, and they may be swallowing more frequently.",
                "0.41 to 0.50": "Clear fear is evident in the person's expression. Their body may be tense, and they might be breathing more rapidly.",
                "0.51 to 0.60": "The person is exhibiting considerable dread in their demeanor. They might be visibly trembling, with a pale complexion.",
                "0.61 to 0.70": "High levels of terror are visible in the person's expression. They may be frozen in place, with widened eyes and a gaping mouth.",
                "0.71 to 0.80": "The person is showing very fearful expressions. They might be cowering or trying to hide, with visible signs of panic.",
                "0.81 to 0.90": "Extreme fright is evident in the person's entire being. They could be shaking uncontrollably, possibly screaming or crying in fear.",
                "0.91 to 0.99": "The person appears completely panic-stricken. They may be in a state of hysteria, unable to think or act rationally due to overwhelming fear."
            },
            "Surprise": {
                "0.00 to 0.10": "The person shows no signs of surprise. Their expression is neutral and doesn't indicate any unexpected occurrence.",
                "0.11 to 0.20": "A slight hint of curiosity can be detected in the person's expression. There might be a barely noticeable raising of their eyebrows.",
                "0.21 to 0.30": "Mild wonder is visible on the person's face. Their eyes might be slightly widened, and their mouth may be partially open.",
                "0.31 to 0.40": "The person is showing noticeable signs of amazement. Their eyebrows are raised higher, and their eyes are clearly widened.",
                "0.41 to 0.50": "Clear surprise is evident in the person's expression. Their mouth may form an 'O' shape, and they might have taken a sharp intake of breath.",
                "0.51 to 0.60": "The person is exhibiting considerable astonishment in their demeanor. They might have taken a step back, with their hand possibly moving towards their face.",
                "0.61 to 0.70": "High levels of shock are visible in the person's expression. They may have audibly gasped, with their whole body reacting to the surprise.",
                "0.71 to 0.80": "The person is showing very surprised expressions. They might be frozen in place, with their jaw dropped and eyes as wide as possible.",
                "0.81 to 0.90": "Extreme stun is evident in the person's entire being. They could be physically jolted, possibly losing their balance or dropping things they were holding.",
                "0.91 to 0.99": "The person appears utterly flabbergasted. They may be rendered speechless, with their entire body language conveying complete and utter disbelief."
            },
            "Disgust": {
                "0.00 to 0.10": "The person shows no signs of disgust. Their expression is neutral and doesn't indicate any aversion.",
                "0.11 to 0.20": "A slight hint of distaste can be detected in the person's expression. There might be a barely noticeable wrinkling of their nose.",
                "0.21 to 0.30": "Mild aversion is visible on the person's face. Their upper lip might be slightly raised, and they may have a faint grimace.",
                "0.31 to 0.40": "The person is showing noticeable signs of repulsion. Their nose is clearly wrinkled, and their mouth may be drawn down at the corners.",
                "0.41 to 0.50": "Clear disgust is evident in the person's expression. They might be visibly recoiling, with their upper lip curled and eyes narrowed.",
                "0.51 to 0.60": "The person is exhibiting considerable revulsion in their demeanor. They might be turning their head away, with their whole face contorted in disgust.",
                "0.61 to 0.70": "High levels of loathing are visible in the person's expression. They may be making gagging sounds, with their body language showing strong aversion.",
                "0.71 to 0.80": "The person is showing very disgusted expressions. They might be physically backing away, possibly covering their mouth or nose.",
                "0.81 to 0.90": "Extreme repulsion is evident in the person's entire being. They could be on the verge of vomiting, with their whole body conveying intense disgust.",
                "0.91 to 0.99": "The person appears utterly revolted. They may be actively retching or violently turning away, showing the most extreme physical signs of disgust possible."
            },
            "Contempt": {
                "0.00 to 0.10": "The person shows no signs of contempt. Their expression is neutral and doesn't indicate any disdain.",
                "0.11 to 0.20": "A slight hint of disapproval can be detected in the person's expression. There might be a barely noticeable tightening of one side of their mouth.",
                "0.21 to 0.30": "Mild disdain is visible on the person's face. One corner of their mouth might be slightly raised, creating an asymmetrical expression.",
                "0.31 to 0.40": "The person is showing noticeable signs of scorn. Their lips may be pursed, with one side of their mouth raised more prominently.",
                "0.41 to 0.50": "Clear contempt is evident in the person's expression. They might have a distinct smirk, with one eyebrow slightly raised.",
                "0.51 to 0.60": "The person is exhibiting considerable derision in their demeanor. They might be looking down their nose at the object of their contempt, with a pronounced sneer.",
                "0.61 to 0.70": "High levels of mockery are visible in the person's expression. They may be rolling their eyes or shaking their head dismissively.",
                "0.71 to 0.80": "The person is showing very contemptuous expressions. They might be openly scoffing or making dismissive gestures with their hands.",
                "0.81 to 0.90": "Extreme scorn is evident in the person's entire being. They could be laughing derisively or making exaggerated expressions of disbelief and disdain.",
                "0.91 to 0.99": "The person appears to be in a state of utter disdain. They may be combining multiple contemptuous expressions and gestures, showing the most intense disrespect possible."
            }
        }
        return summaries.get(emotion, {}).get(intensity_level,
                                              "The person is experiencing this emotion at varying levels of intensity.")

    def get_emotion_recommendations(self, emotion, avg_intensity):
        """
        Get recommendations based on the emotion and its average intensity.

        Args:
            emotion (str): The name of the emotion.
            avg_intensity (float): The average intensity of the emotion.

        Returns:
            str: HTML-formatted string containing recommendations for managing the emotion.
        """
        intensity_level = self.get_intensity_level(avg_intensity)
        recommendations = {
            "Neutral": {
                "0.00 to 0.10": "<ul><li>Engage in mindfulness meditation to cultivate a greater sense of presence and awareness.</li><li>Practice deep breathing exercises to maintain your calm state.</li><li>Spend time in nature, observing your surroundings without judgment.</li><li>Listen to ambient or instrumental music to preserve your neutral mood.</li><li>Use this time for self-reflection and introspection, journaling your thoughts and feelings.</></ul>",
                "0.11 to 0.20": "<ul><li>Take up a new hobby that requires focus and concentration, like puzzles or origami.</li><li>Organize your living or working space to maintain a sense of order and control.</li><li>Read non-fiction books on topics that interest you to stimulate your mind without emotional engagement.</li><li>Practice yoga or tai chi to promote balance in both body and mind.</li><li>Engage in routine tasks that provide a sense of accomplishment without emotional investment.</li></ul>",
                "0.21 to 0.30": "<ul><li>Explore new podcasts on topics you find intellectually stimulating but emotionally neutral.</li><li>Take a leisurely walk in a familiar neighborhood, observing changes and constants.</li><li>Engage in low-stakes social interactions, like casual conversations with acquaintances.</li><li>Try your hand at still life drawing or photography, focusing on capturing objects objectively.</li><li>Spend time planning future activities or organizing your schedule to maintain a sense of purpose without emotional attachment.</li></ul>",
                "0.31 to 0.40": "<ul><li>Attend a documentary screening or educational lecture on a subject you find intriguing.</li><li>Experiment with new recipes that challenge your culinary skills but don't hold emotional significance.</li><li>Practice active listening in conversations, focusing on understanding without emotional involvement.</li><li>Engage in gentle stretching or body scan exercises to increase bodily awareness.</li><li>Start learning a new language, focusing on the technical aspects of grammar and vocabulary.</li></ul>",
                "0.41 to 0.50": "<ul><li>Volunteer for community service activities that align with your values but don't evoke strong emotions.</li><li>Explore different types of tea or coffee, focusing on the sensory experience rather than emotional associations.</li><li>Take up gardening or plant care, observing growth and changes over time.</li><li>Engage in low-impact physical activities like swimming or cycling, focusing on the physical sensations.<li><li>Practice mindful eating, paying close attention to flavors and textures without judgment.</li></ul>",
                "0.51 to 0.60": "<ul><li>Explore museums or art galleries, focusing on objective appreciation of techniques and styles.</li><li>Engage in group activities or classes that promote skill-building without emotional intensity, such as cooking or crafting workshops.</li><li>Practice progressive muscle relaxation to maintain physical and mental equilibrium.</li><li>Spend time observing animals or wildlife, noting behaviors and patterns without anthropomorphizing.</li><li>Engage in simple home improvement or DIY projects that provide a sense of accomplishment.</li></ul>",
                "0.61 to 0.70": "<ul><li>Participate in group discussions or debates on neutral topics, practicing logical reasoning and respectful discourse.</li><li>Explore new genres of music or literature that you haven't experienced before, focusing on analysis rather than emotional response.</li><li>Practice mindful walking, paying close attention to your movements and surroundings.</li><li>Engage in low-stakes problem-solving activities like sudoku or crossword puzzles.</li><li>Experiment with different forms of artistic expression, such as abstract painting or sculpting, focusing on the process rather than the outcome.</li></ul>",
                "0.71 to 0.80": "<ul><li>Take up a new skill that requires concentration and practice, such as juggling or card tricks.</li><li>Engage in mindful observation exercises, like cloud watching or people-watching in a busy area.</li><li>Practice active imagination techniques, visualizing neutral scenarios or landscapes.</li><li>Explore scientific concepts or theories through documentaries or online courses, focusing on understanding rather than emotional engagement.</li><li>Participate in group meditation or mindfulness sessions to maintain a balanced state of mind.</li></ul>",
                "0.81 to 0.90": "<ul><li>Engage in activities that promote cognitive flexibility, such as learning a new board game or strategy game.</li><li>Practice mindful technology use, being aware of your digital consumption without emotional attachment.</li><li>Explore different cultural practices or customs through research or virtual tours, maintaining an objective perspective.</li><li>Engage in controlled breathing exercises or pranayama to maintain physical and mental balance.</li><li>Participate in community forums or online discussions on neutral topics, practicing clear and unbiased communication.</li></ul>",
                "0.91 to 0.99": "<ul><li>Practice mindful observation of your thoughts and emotions without trying to change them.</li><li>Engage in activities that require focused attention but low emotional investment, such as assembling complex models or jigsaw puzzles.</li><li>Explore philosophical concepts or ethical dilemmas through reading or discussion groups, maintaining an objective stance.</li><li>Practice body awareness exercises, such as the body scan meditation, to stay connected with physical sensations.</li><li>Engage in creative writing exercises focused on descriptive or technical writing rather than emotional expression.</li></ul>"
            },
            "Happiness": {
                "0.00 to 0.10": "<ul><li>Engage in simple activities that bring a small smile to your face, like watching cute animal videos or reading light-hearted jokes.</li><li>Take a moment to appreciate the little things in your environment, such as the warmth of sunlight or the aroma of your favorite beverage.</li><li>Reach out to a friend or family member for a brief, pleasant conversation.</li><li>Practice gentle stretching or take a short walk to boost your mood through light physical activity.</li><li>Listen to upbeat music that you enjoy to gradually elevate your spirits.</li></ul>",
                "0.11 to 0.20": "<ul><li>Plan a small outing or activity that you've been looking forward to, like visiting a local cafe or bookstore.</li><li>Engage in a hobby or pastime that typically brings you joy, even if it's for a short duration.</li><li>Write down three things you're grateful for, focusing on positive aspects of your life.</li><li>Watch a favorite comedy show or stand-up routine to induce more laughter and lightheartedness.</li><li>Treat yourself to a small indulgence, like a piece of chocolate or a relaxing bath, to boost your mood.</li></ul>",
                "0.21 to 0.30": "<ul><li>Participate in a group activity or class that aligns with your interests, fostering social connections and shared enjoyment.</li><li>Start a creative project that excites you, allowing yourself to explore and express your ideas freely.</li><li>Spend time in nature, whether it's a park or your own backyard, to uplift your spirits through natural beauty.</li><li>Engage in acts of kindness, such as helping a neighbor or complimenting a stranger, to boost both their mood and yours.</li><li>Try a new recipe or order from a restaurant you've been wanting to try, savoring the experience of new flavors.</li></ul>",
                "0.31 to 0.40": "<ul><li>Plan a get-together with friends or family, focusing on creating a fun and relaxed atmosphere.</li><li>Engage in physical activities that you enjoy, such as dancing, hiking, or playing a sport, to release endorphins and increase happiness.</li><li>Start a gratitude journal, writing down positive experiences and things you appreciate each day.</li><li>Explore a new area of your city or town, allowing yourself to be curious and discover hidden gems.</li><li>Attend a live performance, such as a concert, play, or comedy show, to immerse yourself in entertaining experiences.</li></ul>",
                "0.41 to 0.50": "<ul><li>Set and achieve a personal goal, no matter how small, to experience a sense of accomplishment and boost your happiness.</li><li>Engage in volunteer work or community service, connecting with others and making a positive impact.</li><li>Plan a themed movie or game night with friends, creating a fun and engaging social experience.</li><li>Try a new form of exercise or physical activity that challenges and excites you, like rock climbing or dance classes.</li><li>Start learning a new skill or hobby that you've always been interested in, embracing the joy of discovery and progress.</li></ul>",
                "0.51 to 0.60": "<ul><li>Plan a weekend getaway or day trip to a place you've been wanting to visit, focusing on new experiences and adventure.</li><li>Organize a potluck or dinner party with friends, sharing good food and creating lasting memories.</li><li>Engage in creative expression through art, music, or writing, allowing yourself to fully immerse in the process.</li><li>Participate in a local festival or community event, embracing the collective joy and energy of the crowd.</li><li>Start a passion project that aligns with your values and interests, working towards a meaningful goal.</li></ul>",
                "0.61 to 0.70": "<ul><li>Plan a surprise celebration for a loved one, focusing on bringing joy to others and sharing in their happiness.</li><li>Take on a challenging but exciting project at work or in your personal life, pushing yourself to grow and achieve.</li><li>Organize a group outing or adventure, like a hiking trip or escape room experience, to create shared memories and strengthen bonds.</li><li>Engage in adrenaline-pumping activities like zip-lining or roller coaster rides, if you enjoy thrills.</li><li>Start a happiness-boosting routine, incorporating daily practices like meditation, affirmations, or exercise.</li></ul>",
                "0.71 to 0.80": "<ul><li>Plan a vacation or extended trip to a dream destination, immersing yourself in new cultures and experiences.</li><li>Take steps towards a major life goal, such as starting a business or pursuing higher education, channeling your positive energy into personal growth.</li><li>Organize a large-scale charity event or fundraiser, combining your happiness with making a significant positive impact.</li><li>Attend a multi-day festival or retreat centered around your passions or interests, fully immersing yourself in joyful experiences.</li><li>Start a support group or club focused on spreading happiness and positivity in your community.</li></ul>",
                "0.81 to 0.90": "<ul><li>Embark on a life-changing adventure, such as a sabbatical or around-the-world trip, embracing new experiences and personal growth.</li><li>Make a significant positive change in your life, like pursuing a dream career or moving to a place you've always wanted to live.</li><li>Organize a large family reunion or friends' gathering, bringing together loved ones from far and wide to celebrate connections.</li><li>Start a foundation or non-profit organization aligned with your passions, channeling your happiness into long-term positive impact.</li><li>Create and host a community-wide event or festival celebrating joy, creativity, and connection.</li></ul>",
                "0.91 to 0.99": "<ul><li>Reflect on your journey and personal growth, celebrating your achievements and the positive impact you've had on others.</li><li>Engage in grand gestures of kindness and generosity, using your heightened state of happiness to make a significant difference in others' lives.</li><li>Plan and execute a major life milestone celebration, such as a wedding, graduation, or retirement party, sharing your joy with a wide circle of friends and family.</li><li>Start a movement or campaign focused on spreading happiness and well-being on a large scale</li><li>Dedicate yourself to mentoring and uplifting others, sharing your wisdom and positive outlook to inspire and guide those around you.</li></ul>"
            },
            "Sadness": {
                "0.00 to 0.10": "<ul><li>Acknowledge your feelings without judgment, allowing yourself to experience mild sadness as a natural part of life.</li><li>Engage in gentle self-care activities like taking a warm bath or reading a comforting book.</li><li>Reach out to a friend for a casual conversation, sharing your day without focusing on negative emotions.</li><li>Practice light stretching or take a short walk to gently boost your mood through movement.</li><li>Listen to calming music or nature sounds to create a soothing atmosphere around you.</li></ul>",
                "0.11 to 0.20": "<ul><li>Write in a journal to express and process your emotions, gaining clarity on what's causing your sadness.</li><li>Engage in a hobby or activity that typically brings you joy, even if you don't feel particularly enthusiastic at the moment.</li><li>Practice mindfulness meditation to observe your thoughts and feelings without getting caught up in them.</li><li>Spend time in nature, such as a local park or your backyard, to connect with the world around you.</li><li>Reach out to a supportive friend or family member to share your feelings and receive comfort.</li></ul>",
                "0.21 to 0.30": "<ul><li>Create a self-care routine that includes activities like gentle exercise, healthy eating, and adequate sleep.</li><li>Engage in creative expression through art, music, or writing to channel your emotions productively.</li><li>Seek out uplifting content, such as inspiring documentaries or podcasts, to shift your perspective.</li><li>Practice gratitude by listing three things you appreciate, even in the midst of sadness.</li><li>Consider talking to a therapist or counselor to gain professional support and guidance.</li></ul>",
                "0.31 to 0.40": "<ul><li>Join a support group or online community where you can connect with others who understand what you're going through.</li><li>Engage in volunteer work or acts of kindness to focus on helping others and gain a sense of purpose.</li><li>Practice self-compassion exercises, treating yourself with the same kindness you would offer a friend.</li><li>Explore relaxation techniques like progressive muscle relaxation or guided imagery to ease emotional tension.</li><li>Set small, achievable goals for each day to maintain a sense of accomplishment and forward movement.</li></ul>",
                "0.41 to 0.50": "<ul><li>Seek professional help from a therapist or counselor to develop coping strategies and work through underlying issues.</li><li>Create a \"comfort box\" filled with items that soothe or uplift you, using it when sadness intensifies.</li><li>Engage in physical activities that release endorphins, such as jogging, dancing, or cycling.</li><li>Practice mindfulness-based stress reduction techniques to manage difficult emotions more effectively.</li><li>Reach out to loved ones for support, allowing them to be there for you during this challenging time.</li></ul>",
                "0.51 to 0.60": "<ul><li>Consider medication options in consultation with a healthcare professional if sadness is persistent or impacting daily functioning.</li><li>Engage in expressive therapies like art therapy or music therapy to process emotions non-verbally.</li><li>Create a structured daily routine to provide stability and purpose during difficult times.</li><li>Join a mental health support group or workshop to learn from others and share experiences.</li><li>Practice self-reflection through journaling or guided introspection to gain insights into your emotional patterns.</li></ul>",
                "0.61 to 0.70": "<ul><li>Work with a mental health professional to develop a comprehensive treatment plan addressing your specific needs.</li><li>Engage in regular physical exercise, aiming for at least 30 minutes of moderate activity most days of the week.</li><li>Practice cognitive restructuring techniques to challenge and reframe negative thought patterns.</li><li>Consider alternative therapies like acupuncture or light therapy, under professional guidance.</li><li>Create a support network of trusted friends, family, and professionals to rely on during difficult times.</li></ul>",
                "0.71 to 0.80": "<ul><li>Consult with a psychiatrist to explore medication options if not already doing so, especially if sadness is severe or long-lasting.</li><li>Engage in intensive therapy programs or retreats designed to address deep-seated emotional issues.</li><li>Practice radical acceptance to reduce suffering caused by resisting your current emotional state.</li><li>Implement major lifestyle changes that support mental health, such as changing jobs or living situations if they contribute to your sadness.</li><li>Engage in regular mindfulness practices, such as daily meditation or yoga, to develop emotional resilience.</li></ul>",
                "0.81 to 0.90": "<ul><li>Consider inpatient treatment or partial hospitalization programs for intensive support and monitoring.</li><li>Work closely with a mental health team to manage medication, therapy, and other treatments effectively.</li><li>Engage in trauma-focused therapies if past experiences contribute to your current emotional state.</li><li>Practice extreme self-care, prioritizing your mental health above other commitments when necessary.</li><li>Participate in support groups specifically designed for individuals dealing with severe depression or emotional challenges.</li></ul>",
                "0.91 to 0.99": "<ul><li>Seek immediate professional help, including emergency services if you're experiencing thoughts of self-harm or suicide.</li><li>Engage in crisis management techniques learned through therapy or support programs.</li><li>Utilize safety plans developed with mental health professionals to navigate intense emotional states.</li><li>Consider temporary residence in a supportive environment, such as a mental health facility or retreat center.</li><li>Focus on moment-to-moment coping strategies, breaking down survival into small, manageable steps with the support of professionals and loved ones.</li></ul>"
            },
            "Anger": {
                "0.00 to 0.10": "<ul><li>Practice deep breathing exercises to maintain calm and prevent anger from escalating.</li><li>Engage in a brief physical activity, like a short walk or stretching, to release mild tension.</li><li>Use positive self-talk to reframe minor frustrations and maintain perspective.</li><li>Take a momentary break from the situation that's causing irritation to collect your thoughts.</li><li>Listen to soothing music or nature sounds to create a peaceful environment and prevent anger from building.</li></ul>",
                "0.11 to 0.20": "<ul><li>Practice progressive muscle relaxation to release physical tension associated with rising anger.</li><li>Engage in a calming hobby or activity that requires focus, like puzzles or gardening, to redirect your energy.</li><li>Use \"I\" statements to express your feelings assertively without blaming others.</li><li>Take a time-out from heated situations to cool down and gather your thoughts.</li><li>Write in a journal to express and process your anger in a healthy, non-destructive way.</li></ul>",
                "0.21 to 0.30": "<ul><li>Engage in moderate exercise, like jogging or cycling, to release pent-up energy and frustration.</li><li>Practice mindfulness meditation to observe angry thoughts without getting caught up in them.</li><li>Use cognitive restructuring techniques to challenge and reframe angry thoughts.</li><li>Seek support from a trusted friend or family member to talk through your feelings.</li><li>Engage in creative expression, like painting or playing music, to channel your emotions productively.</li></ul>",
                "0.31 to 0.40": "<ul><li>Attend an anger management workshop or class to learn effective coping strategies.</li><li>Practice assertiveness training to communicate your needs and boundaries effectively.</li><li>Engage in high-intensity exercise, like boxing or martial arts, in a controlled environment to release intense emotions.</li><li>Use visualization techniques to imagine calm scenarios and reduce anger levels.</li><li>Seek professional help from a therapist specializing in anger management for personalized strategies.</li></ul>",
                "0.41 to 0.50": "<ul><li>Work with a therapist to identify and address underlying issues contributing to your anger.</li><li>Practice conflict resolution skills to handle disagreements more effectively.</li><li>Engage in regular stress-reduction activities, such as yoga or tai chi, to manage overall tension.</li><li>Implement a \"cooling off\" period before responding to anger-inducing situations.</li><li>Start a daily mindfulness practice to increase overall emotional regulation.</li></ul>",
                "0.51 to 0.60": "<ul><li>Participate in group therapy sessions focused on anger management and emotional regulation.</li><li>Explore and address childhood or past experiences that may be fueling current anger issues.</li><li>Implement a structured anger management plan with specific coping strategies for different situations.</li><li>Practice empathy exercises to better understand others' perspectives and reduce reactive anger.</li><li>Engage in regular journaling to track anger triggers and patterns over time.</li></ul>",
                "0.61 to 0.70": "<ul><li>Work with a therapist to develop a comprehensive anger management treatment plan.</li><li>Practice intensive relaxation techniques, such as biofeedback or hypnotherapy, to gain better control over physiological responses to anger.</li><li>Engage in role-playing exercises to practice responding to anger-inducing scenarios calmly.</li><li>Implement significant lifestyle changes to reduce overall stress and anger triggers.</li><li>Participate in support groups specifically for individuals struggling with anger management.</li></ul>",
                "0.71 to 0.80": "<ul><li>Consider medication options in consultation with a psychiatrist if anger is significantly impacting daily life.</li><li>Engage in intensive outpatient programs focused on anger management and emotional regulation.</li><li>Practice radical acceptance techniques to reduce suffering caused by resisting anger-inducing situations.</li><li>Implement major changes in your environment or relationships if they consistently contribute to anger issues.</li><li>Engage in regular, intensive physical activities like long-distance running or rock climbing to channel intense emotions.</li></ul>",
                "0.81 to 0.90": "<ul><li>Seek intensive individual therapy, possibly multiple sessions per week, to address severe anger issues.</li><li>Consider partial hospitalization or day treatment programs for comprehensive anger management support.</li><li>Implement crisis management techniques developed with mental health professionals for intense anger episodes.</li><li>Engage in trauma-focused therapies if past traumatic experiences contribute to current anger issues.</li><li>Practice extreme self-care and boundary-setting to protect your mental health and prevent anger escalation.</li></ul>",
                "0.91 to 0.99": "<ul><li>Seek immediate professional help, including emergency services if anger is accompanied by thoughts of harming yourself or others.</li><li>Consider inpatient treatment for intensive monitoring and support in managing severe anger.</li><li>Implement a detailed safety plan developed with mental health professionals to navigate intense anger episodes.</li><li>Engage in intensive, multi-modal therapy approaches combining individual, group, and alternative therapies.</li><li>Focus on moment-to-moment coping strategies, breaking down anger management into small, manageable steps with constant professional support.</li></ul>"
            },
            "Fear": {
                "0.00 to 0.10": "<ul><li>Practice gentle deep breathing exercises to maintain calm and prevent mild anxiety from escalating.</li><li>Engage in positive self-talk, reminding yourself of past successes and your ability to handle challenges.</li><li>Use grounding techniques, like focusing on your senses, to stay present and reduce mild worry.</li><li>Reach out to a friend for a casual conversation to distract from minor fears.Listen to calming music or nature sounds to create a soothing environment.</li></ul>",
                "0.11 to 0.20": "<ul><li>Practice progressive muscle relaxation to release physical tension associated with rising fear.</li><li>Engage in light exercise, like a short walk or gentle yoga, to release nervous energy.</li><li>Use journaling to express and examine your fears, gaining perspective on their realistic nature.</li><li>Try guided imagery or visualization exercises to create a sense of safety and calm.</li><li>Implement a brief mindfulness practice, focusing on the present moment to reduce anticipatory anxiety.</li></ul>",
                "0.21 to 0.30": "<ul><li>Engage in cognitive restructuring techniques to challenge and reframe fearful thoughts.</li><li>Practice exposure exercises for minor fears in a controlled, gradual manner.</li><li>Use aromatherapy or other sensory calming techniques to reduce anxiety levels.</li><li>Seek support from a trusted friend or family member to talk through your fears.</li><li>Engage in a hobby or activity that brings you joy and confidence to counteract fearful feelings.</li></ul>",
                "0.31 to 0.40": "<ul><li>Work with a therapist to develop personalized coping strategies for managing fear and anxiety.</li><li>Practice regular mindfulness meditation to increase overall emotional regulation.</li><li>Engage in moderate exercise routines to boost confidence and release tension.</li><li>Join a support group or online community for individuals dealing with similar fears.</li><li>Implement a structured daily routine to provide stability and reduce uncertainty-related anxiety.</li></ul>",
                "0.41 to 0.50": "<ul><li>Seek professional help from a therapist specializing in anxiety disorders for targeted interventions.</li><li>Practice systematic desensitization techniques under professional guidance for specific phobias.</li><li>Engage in regular relaxation practices, such as yoga or tai chi, to manage overall anxiety levels.</li><li>Implement cognitive-behavioral strategies to address negative thought patterns fueling fear.</li><li>Consider joining group therapy sessions focused on fear and anxiety management.</li></ul>",
                "0.51 to 0.60": "<ul><li>Work with a mental health professional to develop a comprehensive treatment plan for managing fear and anxiety.</li><li>Engage in exposure therapy under professional guidance to gradually confront and overcome significant fears.</li><li>Practice intensive relaxation techniques, such as biofeedback or clinical hypnotherapy.</li><li>Implement significant lifestyle changes to reduce overall stress and anxiety triggers.</li><li>Participate in workshops or classes specifically designed for managing fear and anxiety.</li></ul>",
                "0.61 to 0.70": "<ul><li>Consider medication options in consultation with a psychiatrist if fear is significantly impacting daily functioning.</li><li>Engage in intensive cognitive-behavioral therapy (CBT) or acceptance and commitment therapy (ACT) for managing severe anxiety.</li><li>Implement a structured anxiety management plan with specific coping strategies for different fear-inducing situations.</li><li>Practice intensive mindfulness-based stress reduction techniques to develop greater emotional resilience.</li><li>Engage in regular, challenging physical activities to build confidence and reduce fear responses.</li></ul>",
                "0.71 to 0.80": "<ul><li>Seek intensive individual therapy, possibly multiple sessions per week, to address severe fear and anxiety issues.</li><li>Consider partial hospitalization or day treatment programs for comprehensive anxiety management support.</li><li>Implement crisis management techniques developed with mental health professionals for intense fear episodes.</li><li>Engage in trauma-focused therapies if past traumatic experiences contribute to current fear issues.</li><li>Practice radical acceptance techniques to reduce suffering caused by resisting fear-inducing situations.</li></ul>",
                "0.81 to 0.90": "<ul><li>Engage in intensive outpatient programs specifically designed for severe anxiety and fear management.</li><li>Work closely with a mental health team to manage medication, therapy, and other treatments effectively.</li><li>Implement major changes in your environment or relationships if they consistently contribute to fear and anxiety.</li><li>Participate in support groups specifically for individuals dealing with severe phobias or anxiety disorders.</li><li>Practice extreme self-care and boundary-setting to protect your mental health and prevent fear escalation.</li></ul>",
                "0.91 to 0.99": "<ul><li>Seek immediate professional help, including emergency services if fear is accompanied by panic attacks or thoughts of self-harm.</li><li>Consider inpatient treatment for intensive monitoring and support in managing severe fear and anxiety.</li><li>Implement a detailed safety plan developed with mental health professionals to navigate intense fear episodes.</li><li>Engage in intensive, multi-modal therapy approaches combining individual, group, and alternative therapies for comprehensive treatment.</li><li>Focus on moment-to-moment coping strategies, breaking down fear management into small, manageable steps with constant professional support.</li></ul>"
            },
            "Surprise": {
                "0.00 to 0.10": "<ul><li>Take a moment to pause and breathe deeply, allowing yourself to process the mild surprise.</li><li>Engage in a brief mindfulness exercise to ground yourself in the present moment.</li><li>Reflect on the source of the surprise and consider its significance in the broader context of your day.</li><li>Share the surprising moment with a friend or colleague to gain perspective.</li><li>Use the mild surprise as an opportunity to practice adaptability and openness to unexpected events.</li></ul>",
                "0.11 to 0.20": "<ul><li>Take time to journal about the surprising experience, exploring your thoughts and reactions.</li><li>Engage in a calming activity, like a short walk or stretching, to help process the surprise.</li><li>Practice curiosity by asking questions about the surprising event or information.</li><li>Use the surprise as a prompt for creative thinking or problem-solving.</li><li>Take a moment to reassess your expectations and adjust your plans if necessary.</li></ul>",
                "0.21 to 0.30": "<ul><li>Channel the energy of surprise into a productive activity, like brainstorming or tackling a challenging task.</li><li>Practice reframing techniques to view the surprise as an opportunity for growth or learning.</li><li>Engage in a brief meditation to center yourself and regain focus after the surprise.</li><li>Use the surprising event as a conversation starter to connect with others and gain different perspectives.</li><li>Take time to analyze the surprise and consider how it might inform future decisions or actions.</li></ul>",
                "0.31 to 0.40": "<ul><li>Engage in physical activity to release the energy associated with the surprise and regain emotional balance.</li><li>Practice mindfulness techniques to observe your reactions to the surprise without judgment.</li><li>Use the surprising event as an opportunity to challenge and expand your comfort zone.</li><li>Seek support from friends or colleagues to process and make sense of the surprising situation.</li><li>Take time to reflect on how the surprise aligns with or challenges your existing beliefs and expectations.</li></ul>",
                "0.41 to 0.50": "<ul><li>Channel the heightened awareness from the surprise into a creative project or problem-solving session.</li><li>Practice adaptability exercises to improve your ability to handle unexpected situations.</li><li>Engage in journaling or artistic expression to process the emotional impact of the surprise.</li><li>Use the surprising event as a catalyst for personal growth or skill development.</li><li>Seek out new experiences or information related to the surprise to deepen your understanding.</li></ul>",
                "0.51 to 0.60": "<ul><li>Use the energy of surprise to motivate a positive change or new initiative in your life.</li><li>Engage in group discussions or brainstorming sessions to explore the implications of the surprising event.</li><li>Practice scenario planning to better prepare for future unexpected situations.</li><li>Seek professional guidance, such as coaching or counseling, to help process and learn from significant surprises.</li><li>Use the surprising experience as an opportunity to reassess and potentially adjust your long-term goals or plans.</li></ul>",
                "0.61 to 0.70": "<ul><li>Channel the intense surprise into a major creative or innovative project.</li><li>Engage in intensive research or learning related to the source of the surprise to gain deeper understanding.</li><li>Practice advanced mindfulness techniques to develop greater emotional resilience in the face of unexpected events.</li><li>Seek out challenging new experiences that push you out of your comfort zone to build adaptability.</li><li>Use the surprising event as a catalyst for significant personal or professional transformation.</li></ul>",
                "0.71 to 0.80": "<ul><li>Engage in intensive problem-solving or strategic planning sessions to address the implications of the major surprise.</li><li>Seek professional support, such as therapy or life coaching, to process the emotional impact of significant unexpected events.</li><li>Use the surprising experience as motivation for a major life change or new direction.</li><li>Engage in extreme sports or adventure activities (safely) to channel the intense energy of surprise.</li><li>Develop a comprehensive plan for increasing overall resilience and adaptability in various areas of life.</li></ul>",
                "0.81 to 0.90": "<ul><li>Seek immediate professional support to process and navigate the impact of an extremely surprising or shocking event.</li><li>Engage in intensive self-care and grounding practices to maintain emotional stability.</li><li>Use the profound surprise as a turning point for major life reassessment and potential restructuring.</li><li>Participate in support groups or communities for individuals who have experienced similar shocking events. Develop a detailed crisis management plan for handling future unexpected and potentially destabilizing events.</li></ul>",
                "0.91 to 0.99": "<ul><li>Seek immediate professional help, including emergency services if the extreme surprise is causing severe distress or disorientation.</li><li>Engage in intensive grounding and reality-checking exercises to maintain a sense of stability.</li><li>Work closely with mental health professionals to develop a comprehensive plan for processing and integrating the highly shocking experience.</li><li>Consider temporary changes in environment or routine to provide a sense of safety and control.</li><li>Focus on moment-to-moment coping strategies, breaking down the process of handling the extreme surprise into small, manageable steps with constant professional support.</li></ul>"
            },
            "Disgust": {
                "0.00 to 0.10": "<ul><li>Take a few deep breaths to center yourself and maintain composure.</li><li>Briefly remove yourself from the source of mild disgust if possible.</li><li>Practice neutral observation of your reaction without judgment.</li><li>Engage in a quick distraction technique, like counting backwards or reciting a favorite poem.</li><li>Use humor or light-hearted self-talk to put the mildly disgusting situation into perspective.</li></ul>",
                "0.11 to 0.20": "<ul><li>Practice mindfulness techniques to observe your disgust reaction without getting caught up in it.</li><li>Engage in a brief physical activity, like stretching or walking, to shift your focus.</li><li>Use cognitive reframing to challenge and adjust your perception of the disgusting stimulus.</li><li>Practice self-compassion if the disgust is directed towards yourself or your actions.</li><li>Engage in a pleasant sensory experience, like smelling a favorite scent, to counteract the disgust response.</li></ul>",
                "0.21 to 0.30": "<ul><li>Engage in a cleansing ritual, like washing your hands or tidying your space, to alleviate feelings of disgust.</li><li>Practice exposure techniques in a controlled manner to build tolerance for mildly disgusting stimuli.</li><li>Use journaling to explore the source of your disgust and gain insight into your reactions.</li><li>Engage in a creative activity to channel the energy of disgust into something productive.</li><li>Seek support from a friend or family member to talk through your feelings of disgust.</li></ul>",
                "0.31 to 0.40": "<ul><li>Practice cognitive-behavioral techniques to challenge and reframe thoughts associated with disgust.</li><li>Engage in moderate exercise to release tension and improve overall mood.</li><li>Use guided imagery or visualization to create mental distance from the source of disgust.</li><li>Implement specific coping strategies for managing disgust in various situations.</li><li>Consider seeking professional help if disgust reactions are interfering with daily life.</li></ul>",
                "0.41 to 0.50": "<ul><li>Work with a therapist to explore the root causes of intense disgust reactions.</li><li>Practice systematic desensitization techniques under professional guidance.</li><li>Engage in regular mindfulness meditation to increase overall emotional regulation.</li><li>Implement significant lifestyle changes to reduce exposure to common disgust triggers.</li><li>Participate in support groups or workshops focused on managing strong emotional responses.</li></ul>",
                "0.51 to 0.60": "<ul><li>Seek specialized therapy, such as exposure and response prevention (ERP), for managing severe disgust reactions.</li><li>Engage in intensive cognitive restructuring to address deeply ingrained disgust-related beliefs.</li><li>Practice advanced relaxation techniques, such as progressive muscle relaxation or biofeedback.</li><li>Implement a comprehensive self-care routine to build overall emotional resilience.</li><li>Consider medication options in consultation with a psychiatrist if disgust significantly impacts daily functioning.</li></ul>",
                "0.61 to 0.70": "<ul><li>Work closely with a mental health professional to develop a tailored treatment plan for severe disgust reactions.</li><li>Engage in intensive exposure therapy under close professional supervision.</li><li>Practice radical acceptance techniques to reduce suffering caused by resisting disgust-inducing situations.</li><li>Implement major changes in your environment or lifestyle to manage severe disgust triggers.</li><li>Participate in intensive group therapy or support groups specifically for individuals dealing with extreme disgust or related disorders.</li></ul>",
                "0.71 to 0.80": "<ul><li>Seek intensive individual therapy, possibly multiple sessions per week, to address severe disgust issues.</li><li>Consider partial hospitalization or day treatment programs for comprehensive support in managing extreme disgust reactions.</li><li>Implement crisis management techniques developed with mental health professionals for intense disgust episodes.</li><li>Engage in trauma-focused therapies if past traumatic experiences contribute to current disgust issues.</li><li>Practice extreme self-care and boundary-setting to protect your mental health and prevent disgust escalation.</li></ul>",
                "0.81 to 0.90": "<ul><li>Engage in intensive outpatient programs specifically designed for severe disgust-related disorders.</li><li>Work closely with a mental health team to manage medication, therapy, and other treatments effectively.</li><li>Implement major changes in your environment, relationships, or career if they consistently contribute to extreme disgust reactions.</li><li>Participate in support groups specifically for individuals dealing with severe disgust-related disorders or phobias.</li><li>Focus on developing a highly structured daily routine to provide stability and control in the face of extreme disgust reactions.</li></ul>",
                "0.91 to 0.99": "<ul><li>Seek immediate professional help, including emergency services if disgust is causing severe distress or impairment.</li><li>Consider inpatient treatment for intensive monitoring and support in managing extreme disgust reactions.</li><li>Implement a detailed safety plan developed with mental health professionals to navigate intense disgust episodes.</li><li>Engage in intensive, multi-modal therapy approaches combining individual, group, and alternative therapies for comprehensive treatment.</li><li>Focus on moment-to-moment coping strategies, breaking down disgust management into small, manageable steps with constant professional support.</li></ul>"
            },
            "Contempt": {
                "0.00 to 0.10": "<ul><li>Practice self-awareness to recognize and acknowledge feelings of mild contempt.</li><li>Engage in a brief mindfulness exercise to observe your thoughts without judgment.</li><li>Take a moment to consider the perspective of the person or situation you feel contempt towards.</li><li>Practice empathy by trying to understand the motivations or circumstances of others.</li><li>Use positive self-talk to redirect your thoughts towards more constructive attitudes.</li></ul>",
                "0.11 to 0.20": "<ul><li>Practice reframing techniques to view the situation from a different, more neutral perspective.</li><li>Engage in a brief physical activity, like a short walk, to shift your focus and energy.</li><li>Use journaling to explore the source of your contempt and gain insight into your reactions.</li><li>Practice gratitude by listing positive aspects of your life or the situation at hand.</li><li>Seek out information or experiences that challenge your contemptuous views.</li></ul>",
                "0.21 to 0.30": "<ul><li>Engage in perspective-taking exercises to develop a more nuanced view of the situation or person.</li><li>Practice assertive communication to express your concerns or disagreements respectfully.</li><li>Use cognitive restructuring techniques to challenge and reframe contemptuous thoughts.</li><li>Engage in a compassion-focused meditation or visualization exercise.</li><li>Seek feedback from a trusted friend or mentor to gain a different perspective on your contemptuous feelings.</li></ul>",
                "0.31 to 0.40": "<ul><li>Work with a therapist to explore the root causes of your contemptuous attitudes.</li><li>Practice conflict resolution skills to address issues constructively rather than with contempt.</li><li>Engage in regular mindfulness meditation to increase overall emotional regulation.</li><li>Implement specific strategies for managing contempt in various personal and professional situations.</li><li>Participate in diversity and inclusion training to broaden your perspectives and reduce biases.</li></ul>",
                "0.41 to 0.50": "<ul><li>Seek professional help from a therapist specializing in cognitive-behavioral therapy (CBT) to address contemptuous thought patterns.</li><li>Engage in empathy-building exercises, such as volunteering or participating in community service.</li><li>Practice active listening techniques to improve understanding and reduce knee-jerk contemptuous reactions.</li><li>Implement a daily reflection practice to examine and challenge your judgments and biases.</li><li>Consider joining a support group or workshop focused on emotional intelligence and interpersonal skills.</li></ul>",
                "0.51 to 0.60": "<ul><li>Work with a mental health professional to develop a comprehensive plan for managing contempt and improving relationships.</li><li>Engage in intensive empathy training or compassion-focused therapy.</li><li>Practice advanced cognitive restructuring techniques to address deeply ingrained contemptuous attitudes.</li><li>Implement significant lifestyle changes to reduce exposure to triggers that foster contempt.</li><li>Participate in intensive interpersonal skills training or group therapy focused on building positive relationships.</li></ul>",
                "0.61 to 0.70": "<ul><li>Seek specialized therapy, such as dialectical behavior therapy (DBT), to address intense contempt and improve emotional regulation.</li><li>Engage in intensive self-reflection and personal growth work to understand the root causes of your contempt.</li><li>Practice radical acceptance techniques to reduce suffering caused by holding onto contemptuous attitudes.</li><li>Implement major changes in your social circle or work environment if they consistently reinforce contemptuous behaviors.</li><li>Consider medication options in consultation with a psychiatrist if contempt is significantly impacting your relationships and daily functioning.</li></ul>",
                "0.71 to 0.80": "<ul><li>Work closely with a mental health team to develop a tailored treatment plan for severe contempt issues.</li><li>Engage in intensive individual and group therapy sessions to address deep-seated contempt and its impacts.</li><li>Implement comprehensive lifestyle changes to foster a more compassionate and understanding worldview.</li><li>Participate in intensive retreats or workshops focused on personal transformation and emotional healing.</li><li>Practice extreme self-awareness and self-regulation techniques to catch and redirect contemptuous thoughts and behaviors.</li></ul>",
                "0.81 to 0.90": "<ul><li>Seek intensive outpatient programs specifically designed for severe interpersonal issues and emotional regulation.</li><li>Work with a team of mental health professionals to manage therapy, potential medication, and other interventions effectively.</li><li>Implement major life changes, potentially including career shifts or relocation, to break patterns that reinforce extreme contempt.</li><li>Engage in intensive trauma-focused therapies if past experiences contribute to current contemptuous attitudes.</li><li>Participate in long-term, intensive group therapy or support groups for individuals dealing with severe interpersonal issues.</li></ul>",
                "0.91 to 0.99": "<ul><li>Seek immediate professional help, including potential inpatient treatment, for extreme contempt that severely impairs relationships and daily functioning.</li><li>Engage in intensive, multi-modal therapy approaches combining individual, group, and specialized treatments for comprehensive intervention.</li><li>Implement a detailed safety and management plan developed with mental health professionals to navigate intense contempt episodes.</li><li>Consider temporary separation from triggering environments or relationships while undergoing intensive treatment.</li><li>Focus on moment-to-moment coping strategies, breaking down contempt management into small, manageable steps with constant professional support and monitoring.</li></ul>"
            }
        }
        return recommendations.get(emotion, {}).get(intensity_level,
                                                    "<ul><li>Work on understanding and managing this emotion with professional guidance.</li></ul>")