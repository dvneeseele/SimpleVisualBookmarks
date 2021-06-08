#############################################################################
# dvneeseele
#############################################################################

import os
import sys
import sqlite3
import json

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QVBoxLayout


class bookmarkLabel(QWidget):
    def __init__(self):
        super().__init__()

        #self.setOpenExternalLinks(True)

        # hardcoded link for testing purposes
        # can't use QPixmap since apparently you can't have an image and text.
        #self.setText('<a href="https://www.google.com"><img src="G:/Dev/Projects/SimpleVisualBookmarks/test.png" width=200 height=200></img></a>')

        bookmarkTitle = QLabel('Test Title')

        bookmarkURL = QLabel('<a href="https://www.google.com">test link</a>')
        bookmarkURL.setOpenExternalLinks(True)

        bookmarkSnap = QLabel()
        bookmarkSnap.setScaledContents(True)
        snap = QPixmap('G:/Dev/Projects/SimpleVisualBookmarks/test.png')
        snap.scaled(120, 140, Qt.KeepAspectRatio, Qt.FastTransformation)
        bookmarkSnap.setPixmap(snap)
        

        layout = QVBoxLayout()
        layout.addWidget(bookmarkSnap)
        layout.addWidget(bookmarkTitle)
        layout.addWidget(bookmarkURL)
        self.setLayout(layout)

        # just for test purposes. Opens a new window with the QWidget
        #self.show()

    def getBookmarkTitle(self):
        return self.bookmarkTitle.text

    def getBookmarkURL(self):
        return self.bookmarkURL.text

    def getBookmarkSnap(self):
        # convert to bytearray for sqlite storage
        return self.bookmarkSnap


