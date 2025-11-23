"""import tkinter as tk

from PyQt5.QtWidgets.QWidget import window


def greet_user():
    print("Oi!")

root = tk.Tk()
root.title("Event-Driven Example")

button = tk.Button(root, text="Click Me", command=greet_user)
button.pack(padx=100, pady=100)
root.mainloop()#commando que starta o evento loop."""

###################################################
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

def greet_user():
    print("Oi")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Event")

button = QPushButton("Clic Me", window)
button.clicked.connect(greet_user)
button.move(100, 100)

window.show()
sys.exit(app.exec())


