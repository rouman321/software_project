import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from views.main import M_mainwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = M_mainwindow.M_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())