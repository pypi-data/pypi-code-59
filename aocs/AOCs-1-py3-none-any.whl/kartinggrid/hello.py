
def hello():
    return "Hello World"

if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()
    label = tk.Label(text=hello())
    label.pack()
    window.mainloop()
