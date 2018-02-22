import sys

from views.servent import outside
from PyQt5.QtWidgets import QApplication, QMainWindow
from client import c

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = outside.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    if c.hasconnect == False:
        ui.connectFailed()
    sys.exit(app.exec_())