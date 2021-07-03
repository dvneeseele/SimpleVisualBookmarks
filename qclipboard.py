#############################################################################
# dvneeseele
#############################################################################

import os
import sys
#from PyQt5.Qt import QApllication, QClipboard 
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QWidget, QListWidget, QVBoxLayout, QPushButton



class clipboardGrabber(QWidget):
    def __init__(self):
        super().__init__()


        systemclipboard = QApplication.clipboard()

        self.urllist = []

        self.clipboardURL = QListWidget()
        self.clipboardURL.setSelectionModel(QAbstractItemView.ExtendedSelection)

        self.tags = QListWidget()
        self.tags.setSelectionModel(QAbstractItemView.ExtendedSelection)

        
