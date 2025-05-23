import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('PyQt5 App')
        self.resize(400,300)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Mainwindow()
    window.show()
    sys.exit(app.exec_())