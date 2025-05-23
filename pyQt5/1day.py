import sys
from PyQt5.QtWidgets  import QApplication, QWidget,QPushButton

# QApplication: This is the core of the PyQt application. It's needed for setting up the event loop, handling events, and managing GUI resources.
app=QApplication(sys.argv)

# QWidget: A QWidget is the base class for all GUI components (e.g., buttons, windows, etc.). You can use this to create custom windows or containers.
# window=QWidget()
# window.setWindowTitle('PyQt5 App')
# window.resize(500,500)

# button=QPushButton('click me')
# button.resize(100,100)
# button.move(100,100)
# button.show()

# window.show()

# exec_(): Starts the application's event loop. The event loop waits for user interactions (like button clicks) and processes the
# sys.exit(app.exec_())

window=QWidget()
window.setWindowTitle('click buttin App')


button=QPushButton('click me')
button.resize(100,100)
button.move(100,100)
window.resize(500,500)

window.show()
sys.exit(app.exec_())