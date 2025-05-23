import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("pyqt5 window")
        label = QLabel("hello this for displaying the text")

        button = QPushButton("click me")
        button.clicked.connect(self.onButtonClick)  # Corrected method name
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        central = QWidget()
        central.setLayout(layout)

        self.setCentralWidget(central)

    def onButtonClick(self):
        print("Button clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
