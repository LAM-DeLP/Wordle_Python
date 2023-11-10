import tkinter as tk
from config import datamanager as dm

class Wordle(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.title("Wordle")
        self.master.geometry("400x600")
        self.master.resizable(False,False)
        manager = dm.datamaneger()


if __name__ == "__main__":

    root = tk.Tk()
    app = Wordle(master = root)
    app.mainloop()