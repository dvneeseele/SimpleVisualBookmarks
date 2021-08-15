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



class catagoryItem(QListWidgetItem):
    def __init__(self, id='', name=''):
        super().__init__()

        self.itemId = id
        self.title = name

        self.setText(self.title)
    
    def getItemId(self):
        return self.itemId

    def getTitle(self):
        return self.title






class Catagories(QListWidget):
    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setMouseTracking(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.catagoryMenu)

        self.itemChanged.connect(self.change)



    def change(self):
        print(self.currentItem().text())

        new = self.currentItem()

        #alter = "ALTER TABLE {} RENAME TO {}".format(new.getItemId(), new.text())
        # find table with same id in dirs and change the name entry.
        update = "UPDATE dirs SET name = '{}' WHERE id = '{}' ".format(new.text(), new.getItemId())

        conn = sqlite3.connect('svb.sqlite')
        cursor = conn.cursor()

        cursor.execute(update)

        conn.commit()
        conn.close()

    def catagoryMenu(self, event):
        self.catagoryContextMenu = QMenu()

        addCatagory = self.catagoryContextMenu.addAction('Add Catagory')
        deleteCatagory = self.catagoryContextMenu.addAction('Delete Catagory')
        renameCatagory = self.catagoryContextMenu.addAction('Rename Catagory')

        action = self.catagoryContextMenu.exec_(self.mapToGlobal(event))

        if action == addCatagory:

            randomstr = ''.join(choice(string.ascii_uppercase + string.digits) for t in range(32))

            catagory = catagoryItem(randomstr, "Test Text.....")
            #catagory.setText(0, "Test Text.....")
            self.addItem(catagory)

            conn = sqlite3.connect('svb.sqlite')
            cursor = conn.cursor()



            addtuple = (catagory.getItemId(), catagory.text())

            cursor.execute("INSERT INTO dirs (id, name) VALUES (?, ?)", addtuple)
            cursor.execute("CREATE TABLE IF NOT EXISTS [{}] (url TEXT PRIMARY KEY, title TEXT, image BLOB, tags TEXT)".format(catagory.getItemId()))

            conn.commit()
            conn.close()

        if action == deleteCatagory:
            selection = self.currentItem()
            print(selection)
            self.takeItem(self.row(selection))

            # drop table

            conn = sqlite3.connect('svb.sqlite')
            cursor = conn.cursor()

            cursor.execute("DELETE FROM dirs WHERE id = '{}'".format(selection.getItemId()))
            cursor.execute("DROP TABLE [{}]".format(selection.getItemId()))
            
            conn.commit()
            conn.close()


        if action == renameCatagory:
            selection = self.currentItem()
            selection.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
            self.editItem(selection)

    

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Catagories()
#     window.show()
#     sys.exit(app.exec_())