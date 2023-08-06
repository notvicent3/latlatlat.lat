# 🌐 Leading Autonomous Technology ^4  @kerberosai 5:55am 08/06/2023

# 1. Diseño y Usabilidad
from gui import GUI

# 2. Capacidad de Procesamiento
from labrar import Labrar
from sembrar import Sembrar
from regar import Regar

# 3. Integración y Modularidad
from cosechar import Cosechar
from almacenar import Almacenar
from transportar import Transportar

# 4. Personalización y Aprendizaje Automático
from procesar import Procesar
from productofinal import ProductoFinal
from automl import AutoML

def main():
    # Inicialización de la GUI para Diseño y Usabilidad
    gui = GUI()
    user_config = gui.get_user_config()

    # Capacidad de Procesamiento
    labrar = Labrar()
    sembrar = Sembrar()
    regar = Regar()

    # Despliega una red de agentes autónomos para un propósito específico indicado por el usuario
    agentes = labrar.despliega_agentes()
    datos_recogidos = sembrar.recoger_datos(agentes)
    datos_procesados = regar.procesar_datos(datos_recogidos)

    # Integración y Modularidad
    cosecha = Cosechar()
    almacenar = Almacenar()
    transportar = Transportar()

    datos_a_almacenar = cosecha.transportar(datos_procesados)
    transportar.transportar_datos(datos_a_almacenar)
    granero = almacenar.granero(datos_a_almacenar)

    # Personalización y Aprendizaje Automático
    procesar = Procesar()
    productoFinal = ProductoFinal()
    automl = AutoML()

    if user_config.use_automl:
        model = automl.train(granero)
        results = model.predict(granero)
        productoFinal.mostrar(results)
    else:
        productoFinal.mostrar(granero)

    # Falta definir la función molino
    # molino(resultado)

if __name__ == "__main__":
    main()
