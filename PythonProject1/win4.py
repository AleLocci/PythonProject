from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

a = True

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("Signals")
window.resize(1400, 1300)

label = QLabel("Click")
button = QPushButton("Greet")

def greet(a):
    if a:
        a= False
        label.setText("1")
    else:
        a= True
        label.setText("2")


button.clicked.connect(greet)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
