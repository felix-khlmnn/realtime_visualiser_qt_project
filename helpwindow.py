# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget

from ui_helpwindow import Ui_helpWindow

class HelpWindow(QWidget, Ui_helpWindow):
    def __init__(self):
        super(HelpWindow, self).__init__()
        self.setupUi(self)  # Setup the UI
