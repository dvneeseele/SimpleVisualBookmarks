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
            #"childid" : self.childId,
            "name" : self.itemName,
            "tags" : self.tagList
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


    # def setItemId(self, id):
    #     self.itemId = id

    # def set











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

        # this needs to connect to a function that records the new text and updates the json/sqlite storage.
        #self.itemChanged.connect(self.entryEdited)
        #self.itemEntered.connect(lambda: print('dissss'))

        self.currentItemChanged.connect(self.switchedItem)
        

    def switchedItem(self):
        newId = self.currentItem().getItemId()
        newName = self.currentItem().getItemName()

        if self.currentItem().parent() != None:
            parentid = self.currentItem().parent()

            print("Pointer", parentid)
            print("Parent Id :", parentid.getParentId(), "end")

        print("ID :" ,newId)
        print("Name :", newName)



    def keyPressEvent(self, event):
        # print(event.text())
        # print(event.key())

        kp = event.key()

        if kp == Qt.Key_Space:
            # print("fuck")
            current = self.currentItem()

            # self.closePersistentEditor(current)
            #self.closeit()
            print("THISSSS" ,current.text(self.currentColumn()))
            parent_node = current.parent().getParentId()
            print("Parent Node :", parent_node)
        else:
            pass


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


                create_table = 'CREATE TABLE IF NOT EXISTS {} (url TEXT PRIMARY KEY, title TEXT, image BLOB, tags TEXT )'.format(str(newroot.getItemId()))

                cursor.execute(create_table)

                conn.commit()
                conn.close()

            else:
                child_id = ''.join(choice(string.ascii_uppercase + string.digits) for t in range(32))

                #print("parent parameter", current.getItemId())

                childNode = TreeItem(child_id, "test child name here", current.getItemId(), "tag1, tag2")
                #print("props :", childNode.props())
                current.addChild(childNode)




                conn = sqlite3.connect('svb.sqlite')
                cursor = conn.cursor()

                child_tuple = (child_id, childNode.getItemName(), childNode.getParentId(), "tag, misc, testing")

                cursor.execute("INSERT INTO dirs (id, name, parentid, tags) VALUES (?, ?, ?, ?)", child_tuple)

                create_table = 'CREATE TABLE IF NOT EXISTS {} (url TEXT PRIMARY KEY, title TEXT, image BLOB, tags TEXT )'.format(childNode.getItemId())

                cursor.execute(create_table)

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
                if not self.currentIndex().parent().isValid():
                    current.removeChild(current)
                    conn = sqlite3.connect('svb.sqlite')
                    cursor = conn.cursor()

                    cursor.execute("DROP TABLE".format(current.getItemId()))

            except Exception:
                print(Exception)


        if action == renameFolder:
            self.entryEdited()
            # current = self.currentItem()
            # currentcol = self.currentIndex()            
            # current.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
            # self.editItem(current, currentcol.column())


    def closeit(self):
        current = self.currentItem()
        self.closePersistentEditor(current)
        


    def entryEdited(self):
        current = self.currentItem()
        name = current.getItemName()
        itm_id = current.getItemId()
        #print(itm_id)
        #print(name)

        #conn = sqlite3.connect('svb.sqlite')
        #cursor = conn.cursor()

        #update_tuple = (current.getItemId(), )

        #cursor.execute("SELECT * WHERE id CONTAINS {}".format(current.getItemId()))

        #cursor.execute("UPDATE ? SET name = ?")

        currentcol = self.currentIndex()            
        current.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
        self.editItem(current, currentcol.column())

        print("new item text :", self.currentItem().text(0))

        # self.openPersistentEditor(current, self.currentColumn())
        # current.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)


        #alter_str = 'ALTER TABLE {} RENAME TO {}'.format(itm_id, )

        #self.openPersistentEditor(current)



