# 🌐 OHLC.py Multi - Layer/Chain/Task/Agent/Network  @kerberosai 5:55am 08/06/2023

from core import CoreModule
from gui import GUI
from plugins import PluginManager
from data_management import DataManager
from automl import AutoML

# Importando tus módulos originales
from labrar import Labrar
from sembrar import Sembrar
from regar import Regar
from cosechar import Cosechar
from almacenar import Almacenar
from transportar import Transportar
from procesar import Procesar
from productofinal import ProductoFinal

class CMS_IA:
    def __init__(self):
        self.core = CoreModule()
        self.gui = GUI()
        self.plugins = PluginManager()
        self.data_manager = DataManager()
        self.automl = AutoML()

        # Tus módulos originales
        self.labrar = Labrar()
        self.sembrar = Sembrar()
        self.regar = Regar()
        self.cosecha = Cosechar()
        self.almacenar = Almacenar()
        self.transportar = Transportar()
        self.procesar = Procesar()
        self.productoFinal = ProductoFinal()

    def run(self):
        # Inicia la interfaz gráfica
        self.gui.launch()
        
        # Despliega módulos y plugins según la configuración del usuario
        user_config = self.gui.get_user_config()
        
        # Despliega una red de agentes autonómoms
        agentes = self.labrar.despliega_agentes()

        # Establece un flujo de información constante entre los agentes
        datos_recogidos = self.sembrar.recoger_datos(agentes)
        
        # Procesa los datos 
        datos_procesados = self.regar.procesar_datos(datos_recogidos)
        
        # Transportar datos
        datos_a_almacenar = self.cosecha.transportar(datos_procesados)
        self.transportar.transportar_datos(datos_a_almacenar)

        # Almacenamiento
        granero = self.almacenar.granero(datos_a_almacenar)

        # Si el usuario desea, ejecuta AutoML
        if user_config.use_automl:
            model = self.automl.train(granero)
            results = model.predict(granero)
            self.productoFinal.mostrar(results)
        else:
            # Muestra en la webapp
            self.productoFinal.mostrar(granero)

if __name__ == "__main__":
    app = CMS_IA()
    app.run()
