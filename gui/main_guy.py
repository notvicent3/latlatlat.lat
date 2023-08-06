
import tkinter as tk
from tkinter import ttk
from core.generacion_contenido import GeneracionContenido
from core.interaccion import Interaccion
from core.analisis_texto import AnalisisTexto

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LATLATLAT.LAT - Plataforma IA")

        self.generacion_contenido = GeneracionContenido()
        self.interaccion = Interaccion()
        self.analisis_texto = AnalisisTexto()
        
        self.setup_ui()

    def setup_ui(self):
        self.setup_chat_ui()
        self.setup_settings_ui()
        # Add other setup methods here for other UI sections

    def setup_chat_ui(self):
        chat_frame = ttk.LabelFrame(self.root, text="Chatbot")
        chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.chat_log = tk.Text(chat_frame, wrap='word', state='disabled')
        self.chat_log.pack(fill="both", expand=True, padx=10, pady=5)

        self.user_input = ttk.Entry(chat_frame)
        self.user_input.pack(fill="x", padx=10, pady=5)
        self.user_input.bind("<Return>", self.send_message)

        send_button = tk.Button(chat_frame, text="Enviar", command=self.send_message)
        send_button.pack(padx=10, pady=5)

    def setup_settings_ui(self):
        settings_frame = ttk.LabelFrame(self.root, text="Configuración")
        settings_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(settings_frame, text="Token máximo:").pack(anchor="w", padx=10, pady=5)
        self.token_limit = ttk.Spinbox(settings_frame, from_=1, to=8000)
        self.token_limit.pack(fill="x", padx=10, pady=5)
        self.token_limit.delete(0, 'end')
        self.token_limit.insert(0, 8000)  # valor predeterminado

        save_button = tk.Button(settings_frame, text="Guardar configuración", command=self.save_settings)
        save_button.pack(padx=10, pady=5)

    # Rest of the methods remain the same

if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()
