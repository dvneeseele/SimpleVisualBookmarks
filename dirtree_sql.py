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
    def __init__(self, id='', name='', parent_string='', tags=''):
        super().__init__()

        self.parentId = parent_string
        self.itemId= id
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

    def getItemId(self):
        return self.itemId

    def getItemName(self):
        return self.itemName

    def getTags(self):
        return self.tagList










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
        addRootFolder = self.dirContextMenu.addAction('Add Root Folder')
        deleteFolder = self.dirContextMenu.addAction('Delete Folder')
        renameFolder = self.dirContextMenu.addAction('Rename Folder')

        action = self.dirContextMenu.exec_(self.mapToGlobal(event))

        if action == addFolder:
            current = self.currentItem()

            if not self.currentIndex().parent().isValid() and not self.currentIndex().isValid():

                randomstr = ''.join(choice(string.ascii_uppercase + string.digits) for t in range(32))

                newroot = TreeItem(randomstr, "TestName", "",  "tag1, tag2")
                newroot.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                print(newroot.getParentId())
                self.addTopLevelItem(newroot)

                conn = sqlite3.connect('svb.sqlite')
                cursor = conn.cursor()

                insert_tuple = (newroot.getItemId() , newroot.getItemName(), newroot.getParentId(), newroot.getTags())

                cursor.execute("INSERT INTO dirs (id, name, parentid, tags) VALUES (?, ? ,?, ?)", insert_tuple)
                conn.commit()
                conn.close()

            else:
                child_id = ''.join(choice(string.ascii_uppercase + string.digits) for t in range(32))

                childNode = TreeItem(child_id, "test child name here", current.getItemId(), "tag1, tag2")
                current.addChild(childNode)

                conn = sqlite3.connect('svb.sqlite')
                cursor = conn.cursor()

                child_tuple = (child_id, childNode.getItemName(), childNode.getParentId(), "tag, misc, testing")

                cursor.execute("INSERT INTO dirs (id, name, parentid, tags) VALUES (?, ?, ?, ?)", child_tuple)
                conn.commit()
                conn.close()


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



