import schedule
import time
from .labrar import Labrar

class Programar:
    def __init__(self):
        self.labrar = Labrar()

    def tarea(self):
        # Suponiendo que queremos hacer scraping de un sitio específico cada día
        self.labrar.despliega_agentes("https://ejemplo.com")

    def iniciar_programacion(self):
        schedule.every().day.at("10:00").do(self.tarea)

        while True:
            schedule.run_pending()
            time.sleep(1)
