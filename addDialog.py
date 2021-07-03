#############################################################################
# dvneeseele
#############################################################################

import os
import sys
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QApplication, QTreeView, QTreeWidget, QTreeWidgetItem, QWidget, QListWidget, QVBoxLayout, QPushButton


class addBookmarksDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.folders = QTreeWidget()
        self.folders.setMouseTracking(True)

        childDirectory = QTreeWidgetItem(self.folders)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = addBookmarksDialog()
    window.show()
    sys.exit(app.exec_())