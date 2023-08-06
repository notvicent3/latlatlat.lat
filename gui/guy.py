import tkinter as tk
from tkinter import ttk, Menu, Text, Scrollbar

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LATLATLAT.LAT")

        # Menú
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Área de texto para mostrar resultados
        self.text_area = Text(self.root, wrap="word", width=50, height=15)
        scroll_bar = Scrollbar(self.root, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=scroll_bar.set)
        self.text_area.pack(padx=10, pady=10)
        scroll_bar.pack(side="right", fill="y")

    def run(self):
        self.root.mainloop()

    def update_text(self, new_text):
        self.text_area.insert(tk.END, new_text)
