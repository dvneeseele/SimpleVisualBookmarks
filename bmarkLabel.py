#############################################################################
# dvneeseele
#############################################################################

import os
import sys
import sqlite3
import json

from PyQt5 import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class bookmarkLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setOpenExternalLinks(True)

        # hardcoded link for testing purposes
        # can't use QPixmap since apparently you can't have an image and text.
        self.setText('<a href="https://www.google.com"><img src="G:/Dev/Projects/SimpleVisualBookmarks/test.png" width=200 height=200></img></a>')

