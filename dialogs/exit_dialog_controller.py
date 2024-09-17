from PySide6.QtWidgets import QDialog
from dialogs.ui.dialog_exit_with_background_option import Ui_Dialog_ExitWithBackgroundOption

class ExitDialogController(QDialog):
    """
    Controller class for the exit dialog with background option.

    This class manages the user interface and logic for the exit dialog,
    allowing users to choose between minimizing the application or exiting it.

    Attributes:
        ui (Ui_Dialog_ExitWithBackgroundOption): The user interface for the dialog.
    """

    def __init__(self, parent=None):
        """
        Initialize the ExitDialogController.

        Args:
            parent (QWidget, optional): The parent widget for this dialog. Defaults to None.
        """
        super().__init__(parent)
        self.ui = Ui_Dialog_ExitWithBackgroundOption()
        self.ui.setupUi(self)

        # Set default selection to "Minimize"
        self.ui.radioButton_Minimize.setChecked(True)

    def get_selected_action(self):
        """
        Get the user's selected action from the dialog.

        This method checks which radio button is selected and returns the corresponding action.

        Returns:
            str: The selected action. Can be "minimize", "exit", or None if no valid selection is made.
        """
        if self.ui.radioButton_Minimize.isChecked():
            return "minimize"
        elif self.ui.radioButton_Exit.isChecked():
            return "exit"
        else:
            # This case should theoretically never occur as one radio button should always be checked,
            # but it's included for robustness
            return None