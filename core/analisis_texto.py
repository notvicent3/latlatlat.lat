from .openai_integration import OpenAIIntegration

class AnalisisTexto:
    def __init__(self):
        self.openai = OpenAIIntegration()

    def interpretar_comentario(self, comentario):
        prompt = f"Interpretación del siguiente comentario: {comentario}"
        return self.openai.generate_text(prompt)
        
    def categorizar_comentario(self, comentario):
        prompt = f"Categoriza el siguiente comentario: {comentario}"
        return self.openai.generate_text(prompt)
    
    def analizar_sentimiento(self, comentario):
        prompt = f"Analiza el sentimiento del siguiente comentario: {comentario}"
        return self.openai.generate_text(prompt)
