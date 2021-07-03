#############################################################################
# dvneeseele
#############################################################################

import os
import sys
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QGridLayout, QHBoxLayout, QMenu, QTreeView, QTreeWidget, QTreeWidgetItem, QWidget, QListWidget, QVBoxLayout, QPushButton


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

        childDirectory = QTreeWidgetItem(self.folders)

        urls = QListWidget()
        urls.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
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
        layout.addWidget(tags, 0,2)
        layout.addWidget(urls, 0,3)
        layout.addWidget(submitBtn, 2, 1)
        layout.addWidget(getClipboardBtn, 2, 2)
        layout.addWidget(addTagBtn, 2, 3)



    def submit(self):
        pass

    def addtag(self):
        pass

    def getclipboard(self):
        pass


    def directoryMenu(self, event):
        self.dirContextMenu = QMenu()

        addFolder = self.dirContextMenu.addAction('Add Folder')
        deleteFolder = self.dirContextMenu.addAction('Delete Folder')
        renameFolder = self.dirContextMenu.addAction('Delete Folder')

        action = self.directoryMenu.exec_(self.folders.mapToGlobal(event))

        if action == addFolder:
            pass
        if action == deleteFolder:
            pass
        if action == renameFolder:
            pass

        






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = addBookmarksDialog()
    window.show()
    sys.exit(app.exec_())