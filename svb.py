#############################################################################
# dvneeseele
#############################################################################

import os
import sys
import sqlite3
import json

from bmarkLabel import bookmarkLabel
from svb_ui import VisualBookmarksUI
from dirtree import directories

from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QMenu, QMessageBox
from PyQt5.QtCore import *








class VisualBookmarksApp(VisualBookmarksUI):
    def __init__(self):
        super().__init__()


        self.mainWindow = QMainWindow()
        self.mainWindow.setAcceptDrops(True)

        self.setupUI(self.mainWindow)


        # menubar functions



        # Toolbar functions



        #self.mainWindow.closeEvent = self.closeEvent

        #call load function
        self.dbLoad()






    def dbLoad(self):

        if os.path.exists('svb.sqlite'):

            conn = sqlite3.connect('svb.sqlite')
            cursor = conn.cursor()
        else:
            dbFileErrorMsg = QMessageBox.question(self.mainWindow, 'Error - Database Not Found', 'svb.sqlite db file was not found in the current directory press ok and a new one will be created.', QMessageBox.Ok, QMessageBox.Cancel)

            if dbFileErrorMsg == QMessageBox.Ok:
                conn = sqlite3.connect('svb.sqlite')
                cursor = conn.cursor()


                foldersTable = "CREATE TABLE IF NOT EXISTS dirs(id TEXT PRIMARY KEY, name TEXT, parentid TEXT, tags TEXT)"

                cursor.execute(foldersTable)
                conn.close()

            else:
                sys.exit()

        # Query to get the treewidget nodes to be loaded

        # Another Query to get the corresponding table for the treewidgetitem

        
        conn = sqlite3.connect('svb.sqlite')
        cursor = conn.cursor()

        everything = "SELECT * FROM dirs"

        result = cursor.execute(everything)


        for row, data in enumerate(result):
            pass






        # for row_num, row_data in enumerate(res):
        #     self.watchListTable.insertRow(row_num)
        #     for column_number, column_data in enumerate(row_data):
        #         item = str(column_data)
        #         if column_number == 0:
        #             self.tableLabel = QLabel()
        #             self.tableLabel.setScaledContents(True)
        #             pixmap = QPixmap()
        #             pixmap.loadFromData(column_data)
        #             self.tableLabel.setPixmap(pixmap)

        #             self.watchListTable.setCellWidget(row_num, column_number, self.tableLabel)
        #         else:
        #             self.watchListTable.setItem(row_num, column_number, QTableWidgetItem(column_data))
        #     self.watchListTable.verticalHeader().setDefaultSectionSize(140)
        #     self.watchListTable.horizontalHeader().setDefaultSectionSize(120)


        # conn.close()