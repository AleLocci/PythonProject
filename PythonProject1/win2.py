import sys
from PyQt6.QtWidgets import QApplication, QWidget

x=1
y=2

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("My PyQt6")
window.resize(1360,1250)
window.move(x,y)
window.show()
sys.exit(app.exec())
