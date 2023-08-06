from .openai_integration import OpenAIIntegration

class AnalisisTexto:
    def __init__(self):
        self.openai = OpenAIIntegration()

    def interpretar_comentario(self, comentario):
        prompt = f"Interpretación del siguiente comentario: {comentario}"
        return self.openai.generate_text(prompt)
