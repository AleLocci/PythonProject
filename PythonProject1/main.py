import  tkinter as  tk

def greet_user():
    label.config(text="Hello world!")

root = tk.Tk()

root.title("My first Tkinder ")
root.geometry("350x200")
label= tk.Label(root, text="Click")
label.pack(pady=20)
button = tk.Button(root, text="Grreet", command ="greet_user")
button.pack(pady=10)

root.mainloop()