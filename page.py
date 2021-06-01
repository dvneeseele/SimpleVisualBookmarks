
from bmarkLabel import bookmarkLabel
from PyQt5.QtWidgets import QWidget, QGridLayout



class CatagoryPage(QWidget):
    def __init__(self):
        super().__init__()


        self.grid = QGridLayout()

        # row 1
        self.grid.addWidget(bookmarkLabel(), 1, 1)
        self.grid.addWidget(bookmarkLabel(), 1, 2)
        self.grid.addWidget(bookmarkLabel(), 1, 3)

        # row 2
        self.grid.addWidget(bookmarkLabel(), 2, 1)
        self.grid.addWidget(bookmarkLabel(), 2, 2)
        self.grid.addWidget(bookmarkLabel(), 2, 3)

        self.setLayout(self.grid)

        


