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

     def setup_ui(self):
        # ... [código previo para el chatbot]

        # Marco para Generación de Contenido
        content_frame = ttk.LabelFrame(self.root, text="Generación de Contenido")
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.content_type = ttk.Combobox(content_frame, values=["Resumen", "Análisis", "Descripción"])
        self.content_type.pack(fill="x", padx=10, pady=5)
        self.content_type.set("Selecciona el tipo de contenido")

        self.data_input = Text(content_frame, wrap='word')
        self.data_input.pack(fill="both", expand=True, padx=10, pady=5)

        generate_button = Button(content_frame, text="Generar", command=self.generate_content)
        generate_button.pack(padx=10, pady=5)

        self.generated_content = Text(content_frame, wrap='word', state='disabled')
        self.generated_content.pack(fill="both", expand=True, padx=10, pady=5)

    def generate_content(self):
        data = self.data_input.get("1.0", "end-1c")
        content_type = self.content_type.get()

        generated_text = self.generacion_contenido.generar_informe(data, content_type)

        self.generated_content.configure(state='normal')
        self.generated_content.delete("1.0", "end")
        self.generated_content.insert("1.0", generated_text)
        self.generated_content.configure(state='disabled')

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

 # Puedes agregar más elementos y marcos para las otras funcionalidades

if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()
