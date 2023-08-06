from .openai_integration import OpenAIIntegration

class Interaccion:
   def __init__(self):
        self.openai = OpenAIIntegration()

    def respuesta_chatbot(self, pregunta_usuario):
        prompt = f"Usuario: {pregunta_usuario}\nAsistente:"
        return self.openai.generate_text(prompt)

    def respuesta_chatbot_contextual(self, conversacion_previa, pregunta_usuario):
        prompt = f"{conversacion_previa}\nUsuario: {pregunta_usuario}\nAsistente:"
        return self.openai.generate_text(prompt)

