#############################################################################
# dvneeseele
#############################################################################

import os
import sys

from PyQt5.QtWidgets import (QMainWindow, QTabBar, QMenuBar, QSplitter, QWidget, QGridLayout, QTreeView, QStackedWidget, QAction, QToolBar)



class VisualBookmarksUI(object):
    def __init__(self):
        super(VisualBookmarksUI).__init__()


    def setupUI(self, MainWindow):

        # menubar

        menubar = MainWindow.menuBar()

        self.mb_file = menubar.addMenu("File")
        self.mb_edit = menubar.addMenu("Edit")
        self.mb_view = menubar.addMenu("View")
        self.mb_help = menubar.addMenu("Help")


        # Toolbar

        self.toolbar = QToolBar(MainWindow)
        self.toolbar.setIconSize(QSize(40, 40))

        MainWindow.addToolBar(self.toolbar)



        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName('central')

        self.splitter = QSplitter(self.centralWidget)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setStretchFactor(0, 25)
        self.splitter.setStretchFactor(1, 75)


        self.sidebar = QTreeView(self.splitter)
        self.sidebar.setObjectName('sidebartree')
        self.sidebar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)


        