from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Clase que permite el analisis de los logs/registros de comandos de una base de datos SQL
class Analisis:
    # Variable de la clase Analisis para iniciar el archivo.
    def __init__(self, nombrearchivo="db_audit_30DAY.csv"):
        self.nombre_archivo = nombrearchivo

    # Funcion de lectura del archivo y generacion del dataframe
    # El verbose proporciona mensajes sobre el estado del sistema al usuario cuando esta activado
    def lectura(self, verbose="false"):
        if verbose == "false":
            try:
                df = pd.read_csv(self.nombre_archivo)
                return df
            except:
                return
        else:
            try:
                df = pd.read_csv(self.nombre_archivo)
                print("Lectura completa.")
                return df
            except:
                print("Error en la lectura del archivo: ", self.nombre_archivo)

    # Resumen de la cantidad de elementos por columna en el dataframe
    def contenido(self, archivo):
        return print(archivo.nunique(axis=0))

    # Estadistica basica sobre la cantidad de tipos de comandos SQL en el dataframe
    def estadistica_comandos(self, archivo):
        tipos_comandos = []
        for el in archivo["Type"]:
            if el not in tipos_comandos:
                tipos_comandos.append(el)
        cant_comandos = np.zeros(len(tipos_comandos), dtype=int)
        for el in archivo["Type"]:
            for i in range(len(tipos_comandos)):
                if el == tipos_comandos[i]:
                    cant_comandos[i] += 1
        porcentajes = []
        for el in cant_comandos:
            porcentajes.append(round(el / cant_comandos.sum(), 5))
        for i in range(len(porcentajes)):
            print("El comando {} tiene un {}% de presencia en el dataframe.".format(tipos_comandos[i], porcentajes[i]))

    # Grafica basica de la duracion de ejecucion de comandos en el tiempo que fue ejecutado
    def grafica_duracion_comandos(self, archivo):
        # archivo['Time'] = archivo['Time'].map(lambda x: datetime.strptime(str(x), '%Y/%m/%d %H:%M:%S.%f'))
        x = archivo['Time'][:5]
        y = archivo['Duration'][:5]
        plt.plot(x, y)
        plt.gcf().autofmt_xdate()
        plt.show()


# Programa principal
if __name__ == '__main__':
    prueba = Analisis()
    frame = prueba.lectura()
    prueba.contenido(frame)
    prueba.estadistica_comandos(frame)
    prueba.grafica_duracion_comandos(frame)
