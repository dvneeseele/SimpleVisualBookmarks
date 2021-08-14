#############################################################################
# dvneeseele
#############################################################################

import os
import sys
import sqlite3
import string
from random import choice
from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QTreeWidget, QAbstractItemView, QTreeWidgetItem, QMenu, QApplication
from PyQt5.QtCore import *


class Catagories(QListWidget):
    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setMouseTracking(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.catagoryMenu)


    def catagoryMenu(self, event):
        self.catagoryContextMenu = QMenu()

        addCatagory = self.catagoryContextMenu.addAction('Add Catagory')
        deleteCatagory = self.catagoryContextMenu.addAction('Delete Catagory')
        renameCatagory = self.catagoryContextMenu.addAction('Delete Catagory')

        action = self.catagoryContextMenu.exec_(self.mapToGlobal(event))

        if action == addCatagory:
            catagory = QListWidgetItem()
            catagory.setText("Test Text.....")
            self.addItem(catagory)

        if action == deleteCatagory:
            selection = self.currentItem()
            print(selection)
            self.takeItem(selection)

        if action == renameCatagory:
            selection = self.currentItem()
            self.editItem(selection)
            
        