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

        # hardcoded link for testing purposes
        self.setText("<a href=\"https://www.google.com/\">google</a>")
        self.setTextFormat(Qt.RichText)
        self.textInteractionFlags(Qt.TextBrowserInteraction)
        self.setOpenExternalLinks(True)

        # hardcode for testing
        #self.setPixmap(QPixmap("./image.jpg"))


    def setPixmap(self, image):
        return super().setPixmap(image)






