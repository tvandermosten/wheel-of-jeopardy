from PyQt5 import QtGui, QtWidgets
from ui.game import Ui_game

class GameChoiceWindow(QtWidgets.QMainWindow, Ui_gameChoice):
    def __init__(self, parent):
        super(GameChoiceWindow, self).__init__(parent)
        self.setupUi(self)