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


class TreeItem(QTreeWidgetItem):
    def __init__(self, parent_string='', child_string='', name='', tags=''):
        super().__init__()

        self.parentId = parent_string
        self.childId = child_string
        self.itemName = name
        self.setText(0 ,self.itemName)
        self.tagList = tags

    def props(self):
        properties = {
            "parentid" : self.parentId,
            "childid" : self.childId,
            "name" : self.itemName,
            "tags" : self.tags
        }
        return properties


    def getParentId(self):
        return self.parentId

    def getChildId(self):
        return self.childId

    def getItemName(self):
        return self.itemName

    def getTags(self):
        return self.tagList










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

            if not self.currentIndex().parent().isValid() and not self.currentIndex().isValid():

                randomstr = ''.join(choice(string.ascii_uppercase + string.digits) for t in range(32))
                #print(randomstr)                

                newroot = TreeItem(randomstr, "", "TestName", "tag1, tag2")
                #newroot.setText(0 ,"okaythen")
                newroot.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                print(newroot.getParentId())
                self.addTopLevelItem(newroot)
                #newroot = QTreeWidgetItem(self)
                #newroot.setText(0, "This is a new root level directory")
                #newroot.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)

                conn = sqlite3.connect('svb.sqlite')
                cursor = conn.cursor()




                insert_tuple = (randomstr, newroot.text(0),"",  "tag1, tag2")

                cursor.execute("INSERT INTO dirs (id, name, parentid, tags) VALUES (?, ? ,?, ?)", insert_tuple)
                conn.commit()
                conn.close()

            else:
                current.addChild(addSubDir)
                #parent = current.parent().text()
                # update the json
                # if os.path.exists() then append the item to the json file with the filename of the QTreeWidgetItem.text()

                conn = sqlite3.connect('svb.sqlite')
                cursor = conn.cursor()

                child_id_str = ''.join(choice(string.ascii_uppercase + string.digits) for t in range(32))

                child_tuple = (child_id_str, addSubDir.text(0), "", "tag, misc, testing")

                cursor.execute("INSERT INTO dirs (id, name, parentid, tags) VALUES (?, ?, ?, ?)", child_tuple)

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