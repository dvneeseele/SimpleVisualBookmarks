#############################################################################
# dvneeseele
#############################################################################

import os
import sys
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QGridLayout, QHBoxLayout, QLineEdit, QListWidgetItem, QMenu, QTreeView, QTreeWidget, QTreeWidgetItem, QWidget, QListWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import *

class addBookmarksDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.folders = QTreeWidget()
        self.folders.setMouseTracking(True)
        self.folders.setHeaderHidden(True)
        self.folders.setDragEnabled(True)
        self.folders.setDragDropMode(QAbstractItemView.InternalMove)
        self.folders.setAcceptDrops(True)
        self.folders.setSelectionMode(QAbstractItemView.SingleSelection)
        self.folders.setContextMenuPolicy(Qt.CustomContextMenu)
        self.folders.customContextMenuRequested.connect(self.directoryMenu)

        self.folders.mouseDoubleClickEvent = self.set

        childDirectory = QTreeWidgetItem(self.folders)

        self.urls = QListWidget()
        self.urls.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        tags = QListWidget()
        tags.setSelectionMode(QAbstractItemView.ExtendedSelection)

        submitBtn = QPushButton("Submit")
        submitBtn.clicked.connect(self.submit)
        
        addTagBtn = QPushButton("Add New Tag")
        addTagBtn.clicked.connect(self.addtag)

        getClipboardBtn = QPushButton("Get Clipboard")
        getClipboardBtn.clicked.connect(self.getclipboard)


        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.folders, 0,1)
        layout.addWidget(tags, 0,3)
        layout.addWidget(self.urls, 0,2)
        layout.addWidget(submitBtn, 2, 1)
        layout.addWidget(getClipboardBtn, 2, 2)
        layout.addWidget(addTagBtn, 2, 3)

    def set(self, e):
        entry = self.folders.currentIndex()
        print(entry.data())
        e.accept()


    def submit(self):
        pass

    def addtag(self):
        pass

    def getclipboard(self):
        c = list(QApplication.clipboard().text().split('\n'))

        for i in c:
            urlitem = QListWidgetItem()
            urlitem.setText(i)
            self.urls.addItem(urlitem)


    def directoryMenu(self, event):
        self.dirContextMenu = QMenu()

        addFolder = self.dirContextMenu.addAction('Add Folder')
        deleteFolder = self.dirContextMenu.addAction('Delete Folder')
        renameFolder = self.dirContextMenu.addAction('Rename Folder')

        action = self.dirContextMenu.exec_(self.folders.mapToGlobal(event))

        if action == addFolder:
            current = self.folders.currentItem()
            addSubDir = QTreeWidgetItem()
            addSubDir.setText(0, "Test...")
            current.addChild(addSubDir)
        if action == deleteFolder:
            try:
                current = self.folders.currentItem()
                parent = current.parent()
                current.removeChild(current)
            except Exception:
                print(Exception)

        if action == renameFolder:
            current = self.folders.currentItem()
            current.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
            currentcol = self.folders.currentIndex()
            self.folders.editItem(current, currentcol.column())            


            # current = self.folders.currentItem()
            # currentcol = self.folders.currentIndex()
            # print(currentcol.column())
            # lineedit = QLineEdit()
            # self.folders.setItemWidget(current, currentcol.column() ,lineedit)

            # current = self.folders.currentItem()
            # current.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
            # current.setSelected(True)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = addBookmarksDialog()
    window.show()
    sys.exit(app.exec_())