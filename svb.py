#############################################################################
# dvneeseele
#############################################################################

import os
import sys
import sqlite3
import json

from bmarkLabel import bookmarkLabel
from svb_ui import VisualBookmarksUI
from dirtree import directories

from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QMenu
from PyQt5.QtCore import *








class VisualBookmarksApp(VisualBookmarksUI):
    def __init__(self):
        super().__init__()


        self.mainWindow = QMainWindow()
        self.mainWindow.setAcceptDrops(True)

        self.setupUI(self.mainWindow)


        # menubar functions



        # Toolbar functions



        #self.mainWindow.closeEvent = self.closeEvent

        # call load function
        # self.dbLoad()

