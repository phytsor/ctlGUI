import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Ui_mainwindow

str = 'Hello World'
print(str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
