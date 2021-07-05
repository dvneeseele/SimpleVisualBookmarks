#############################################################################
# dvneeseele
#############################################################################

import os
import sys
import json
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QTreeWidget ,QAbstractItemView, QTreeWidgetItem, QMenu


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
            current.addChild(addSubDir)
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
