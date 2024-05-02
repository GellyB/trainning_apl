from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QTreeWidgetItem
from classes.post_connect import *
from classes.login_window import _curs_tab

def main():

    app = QtWidgets.QApplication([])
    QtGui.QFontDatabase.addApplicationFont(fr'C:\Users\kazim\Downloads\arcadeclassic\ARCADECLASSIC.TTF')
    firstly = _curs_tab(app)

    app.exec_()

if  __name__=="__main__":
    main()

