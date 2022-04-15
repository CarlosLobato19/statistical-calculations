import math
from math import log

class SerieAgrupada:

    def __init__(self,datosDescritor):
        self.datosDescritor = datosDescritor
        self.poblacion_number = len(datosDescritor)
        self.tablaDeFrecuencias = {}

        for dato in datosDescritor:
            if self.tablaDeFrecuencias.get(dato) != None:
                self.tablaDeFrecuencias[dato] +=1
            else:
                self.tablaDeFrecuencias[dato] = 1

    #retorna la info del tipo de dato
    def infoData(self):
        datoFrecu = list(self.tablaDeFrecuencias.keys())
        return datoFrecu

    #retorna info de la frecuencia del dato
    def infoFrecu(self):
        datoInfo = list(self.tablaDeFrecuencias.values())

        return datoInfo

    #retorna el N(poblacion) de una serie de datos
    def poblacion(self):
        return len(self.datosDescritor)

    def frecuenciaRelativa(self):
        datoFrecuencia =  list(self.tablaDeFrecuencias.values())
        frecuenciaRelativa = []
        for i in datoFrecuencia:
            calculando = (i/self.poblacion_number)
            frecuenciaRelativa.append(calculando)
        return frecuenciaRelativa

    #retorna la frecuencia relativa porcentual
    def frecuenciaRelativaPorcen(self):
        datoFRelativa = list(self.tablaDeFrecuencias.values())
        frecuenciaRelaPorcent = []
        for i in datoFRelativa:
            calculando = (i/self.poblacion_number) * 100
            frecuenciaRelaPorcent.append(round(calculando))
        return frecuenciaRelaPorcent





