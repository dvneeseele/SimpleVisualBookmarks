
from bmarkLabel import bookmarkLabel
from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QWidget, QGridLayout
from PyQt5.QtCore import Qt


# class CatagoryPage(QWidget):
#     def __init__(self):
#         super().__init__()


#         self.grid = QGridLayout()

#         # row 1
#         self.grid.addWidget(bookmarkLabel(), 1, 1)
#         self.grid.addWidget(bookmarkLabel(), 1, 2)
#         self.grid.addWidget(bookmarkLabel(), 1, 3)

#         # row 2
#         self.grid.addWidget(bookmarkLabel(), 2, 1)
#         self.grid.addWidget(bookmarkLabel(), 2, 2)
#         self.grid.addWidget(bookmarkLabel(), 2, 3)

#         self.setLayout(self.grid)


class CatagoryPage(QTableWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName('catagory-content-table')

        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFont(QFont('Arial', 14))
        self.setWordWrap(False)
        
        self.setColumnCount(4)
        self.verticalHeader().setDefaultSectionSize(140)
        self.horizontalHeader().setDefaultSectionSize(120)


