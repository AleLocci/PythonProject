from PyQt6.QtWidgets import  QApplication, QMainWindow
import sys

from win2 import window

app= QApplication(sys.argv)
window= QMainWindow()

window.setWindowTitle("PyQt6")
window.resize(1400,1260)
window.show()
sys.exit(app.exec())