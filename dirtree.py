#############################################################################
# dvneeseele
#############################################################################

import os
import sys
import json
from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QTreeWidget, QAbstractItemView, QTreeWidgetItem, QMenu, QApplication
from PyQt5.QtCore import *

class directories(QTreeWidget):
    def __init__(self):
        super().__init__()

        self.setMouseTracking(True)
        self.setHeaderHidden(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setAcceptDrops(True)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.directoryMenu)

    def directoryMenu(self, event):
        self.dirContextMenu = QMenu()

        addFolder = self.dirContextMenu.addAction('Add Folder')
        deleteFolder = self.dirContextMenu.addAction('Delete Folder')
        renameFolder = self.dirContextMenu.addAction('Rename Folder')

        action = self.dirContextMenu.exec_(self.mapToGlobal(event))

        if action == addFolder:
            current = self.currentItem()
            addSubDir = QTreeWidgetItem()
            addSubDir.setText(0, "Test...")
            try:
                current.addChild(addSubDir)
            except Exception:
                newroot = QTreeWidgetItem(self)
                newroot.setText(0, "This is a new root level directory")
                newroot.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)

        if action == deleteFolder:
            try:
                current = self.currentItem()
                parent = current.parent()
                current.removeChild(current)
            except Exception:
                print(Exception)

        if action == renameFolder:
            current = self.currentItem()
            current.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
            currentcol = self.currentIndex()
            self.editItem(current, currentcol.column())



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = directories()
#     window.show()
#     sys.exit(app.exec_())