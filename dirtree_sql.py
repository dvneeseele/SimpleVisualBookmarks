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
from PyQt5.QtWidgets import QTreeWidget, QAbstractItemView, QTreeWidgetItem, QMenu, QApplication
from PyQt5.QtCore import *

class directories(QTreeWidget):
    def __init__(self):
        super().__init__()

        self.treedict = {}

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
        addRootFolder = self.dirContextMenu.addAction('Add Root Folder')
        deleteFolder = self.dirContextMenu.addAction('Delete Folder')
        renameFolder = self.dirContextMenu.addAction('Rename Folder')

        action = self.dirContextMenu.exec_(self.mapToGlobal(event))

        if action == addFolder:
            current = self.currentItem()
            #parentnode = current.parent()
            addSubDir = QTreeWidgetItem()
            addSubDir.setText(0, "Test...")

            if not self.currentIndex().parent().isValid():
                newroot = QTreeWidgetItem(self)
                newroot.setText(0, "This is a new root level directory")
                newroot.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)

                conn = sqlite3.connect('svb.sqlite')
                cursor = conn.cursor()

                randomstr = ''.join(choice(string.ascii_uppercase + string.digits) for t in range(32))
                print(randomstr)

                insert_tuple = (randomstr, "",  "tag1, tag2")

                cursor.execute("INSERT INTO dirs (id, name, parentid, tags) VALUES (?, ?, ?)", insert_tuple)
                conn.commit()
                conn.close()

            else:
                current.addChild(addSubDir)
                parent = current.parent().text()
                # update the json
                # if os.path.exists() then append the item to the json file with the filename of the QTreeWidgetItem.text()
                if os.path.exists("./treejson/{}.json".format(parent), 'w'):
                    # append to the existing json file
                    pass
                else:
                    pass
                    # parse skeleton json file add to it and do another with open to save it and close the read

        if action == addRootFolder:
            newroot = QTreeWidgetItem(self)
            newroot.setText(0, "New Root Folder")
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