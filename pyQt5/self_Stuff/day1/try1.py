import sys
from PyQt5.QtWidgets import QLabel ,QWidget,QApplication

app=QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100,100,280,80)
meeage=QLabel('Hello World',parent=window)
meeage.move(110,20)

# ** The move() method sets the position of the helloMsg label within the window.
window.show()
sys.exit(app.exec_())#nally we can run the application's event loop using the exec() method of the QApplication instance. The exec() method starts the event loop, and sys.exit() ensures a clean exit of the application when it terminates