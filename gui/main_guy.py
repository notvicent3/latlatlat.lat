import tkinter as tk
from tkinter import ttk, Text, Button, Label
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
        # Marco para el chatbot
        chat_frame = ttk.LabelFrame(self.root, text="Chatbot")
        chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.chat_log = Text(chat_frame, wrap='word', state='disabled')
        self.chat_log.pack(fill="both", expand=True, padx=10, pady=5)

        self.user_input = ttk.Entry(chat_frame)
        self.user_input.pack(fill="x", padx=10, pady=5)
        self.user_input.bind("<Return>", self.send_message)

        send_button = Button(chat_frame, text="Enviar", command=self.send_message)
        send_button.pack(padx=10, pady=5)

        # Puedes agregar más elementos y marcos para las otras funcionalidades

    def send_message(self, event=None):
        user_message = self.user_input.get()
        self.append_to_chat(f"Usuario: {user_message}")

        bot_response = self.interaccion.respuesta_chatbot(user_message)
        self.append_to_chat(f"Asistente: {bot_response}")

        self.user_input.delete(0, 'end')

    def append_to_chat(self, message):
        self.chat_log.configure(state='normal')
        self.chat_log.insert('end', message + '\n')
        self.chat_log.configure(state='disabled')
        self.chat_log.yview('end')

if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()
