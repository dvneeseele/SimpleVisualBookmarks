#############################################################################
# dvneeseele
#############################################################################

import os
import sys

from page import CatagoryPage
from dirtree_sql import directories
from flat_organization import Catagories, tagsList

from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QHBoxLayout, QMainWindow, QTabBar, QMenuBar, QSplitter, QWidget, QGridLayout, QTreeView, QStackedWidget, QAction, QToolBar)



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

        self.vertSplitter = QSplitter(self.centralWidget)
        self.vertSplitter.setOrientation(Qt.Vertical)
        self.vertSplitter.setStretchFactor(0, 25)
        self.vertSplitter.setStretchFactor(1, 75)


        # self.sidebar = QTreeView(self.splitter)
        # self.sidebar.setObjectName('sidebartree')
        # self.sidebar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        #self.sidebar = directories()
        self.sidebar = Catagories()
        self.sidebar.setObjectName('sidebartree')
        #self.splitter.addWidget(self.sidebar)

        self.bookmarksStack = QStackedWidget()

        #testwidget = QWidget()

        testwidget = CatagoryPage()
        testwidget.setObjectName('testpage')


        tagsPanel = tagsList()
        tagsPanel.setObjectName('tagsPanel')



        self.bookmarksStack.addWidget(testwidget)

        self.bookmarksStack.setObjectName("bookmarkstack")



        self.vertSplitter.addWidget(self.sidebar)
        self.vertSplitter.addWidget(tagsPanel)
        self.vertSplitter.addWidget(self.splitter)

        #self.splitter.addWidget(self.vertSplitter)
        self.splitter.addWidget(self.bookmarksStack)


        self.splitter.setSizes([50, 650, 100])
        #self.vertSplitter.setSizes([50, 650, 50])




        self.boxLayout = QHBoxLayout()
        self.boxLayout.addWidget(self.vertSplitter)
        self.boxLayout.addWidget(self.splitter)



        self.centralWidget.setLayout(self.boxLayout)
        MainWindow.setCentralWidget(self.centralWidget)


        MainWindow.show()
