from .openai_integration import OpenAIIntegration

class GeneracionContenido:
    def __init__(self):
        self.openai = OpenAIIntegration()

    def generar_resumen(self, data):
        prompt = f"Resumen de los datos recolectados: {data}"
        return self.openai.generate_text(prompt)
