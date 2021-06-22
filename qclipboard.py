#############################################################################
# dvneeseele
#############################################################################

import os
import sys
from PyQt5.Qt import QApllication, QClipboard 
from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout, QPushButton



class clipboardGrabber(QWidget):
    def __init__(self):
        super().__init__()


        qlist = QListWidget()

        clipboard = QClipboard()

        qlist.addItem()


