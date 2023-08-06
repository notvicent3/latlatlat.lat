from .openai_integration import OpenAIIntegration

class GeneracionContenido:
    def __init__(self):
        self.openai = OpenAIIntegration()

    def generar_resumen(self, data):
        prompt = f"Resumen de los datos recolectados: {data}"
        return self.openai.generate_text(prompt)

    def generar_informe(self, datos, tipo_informe):
        if tipo_informe == "resumen":
            prompt = f"Genera un resumen basado en los siguientes datos: {datos}"
        elif tipo_informe == "analisis":
            prompt = f"Realiza un análisis detallado de los siguientes datos: {datos}"
        else:
            prompt = f"Descripción de los siguientes datos: {datos}"
        
        return self.openai.generate_text(prompt)

