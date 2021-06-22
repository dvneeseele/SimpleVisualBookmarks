#############################################################################
# dvneeseele
#############################################################################

import os
import sys
from PyQt5.Qt import QApplication, QClipboard 
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QPushButton


app = QApplication(sys.argv)

c = QApplication.clipboard()


print(c.text())

