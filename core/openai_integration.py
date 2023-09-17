import openai

class OpenAIIntegration:
    def __init__(self):
        # Configura la clave de API
        openai.api_key = "APIkey"
        
    def generate_text(self, prompt_text):
        # Asegúrate de no superar el límite de 8k tokens
        response = openai.Completion.create(
            model="gpt-3.5-turbo-16k",
            prompt=prompt_text,
            max_tokens=8000
        )
        return response.choices[0].text.strip()

    # Puedes añadir más métodos para otras funcionalidades relacionadas con OpenAI
