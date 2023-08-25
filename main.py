import os
import sys


from qgis.core import*
from qgis.gui import*
from qgis.utils import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import* 

from .interfaz import Ui_mainWindow

class main_interfaz(QMainWindow):
    def __init__(self):
        QMainWindow.__init(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

