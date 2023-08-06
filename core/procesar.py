import pandas as pd
from textblob import TextBlob  # Para análisis de sentimiento

class Procesar:
    def limpia_datos(self, data_frame):
        # Limpieza básica de datos usando pandas
        df_clean = data_frame.dropna()  # Elimina filas con valores NaN
        # Agrega más lógica de limpieza según sea necesario
        
        return df_clean
    
    def analisis_sentimiento(self, texto):
        analysis = TextBlob(texto)
        return analysis.sentiment.polarity
