import math
from math import log

class SerieClase:

    def __init__(self,datosAnalizar):
        self.datosAnalizar = datosAnalizar
        self.poblacion = len(datosAnalizar)

        self.datoMayor = max(self.datosAnalizar)
        self.datoMenor = min(self.datosAnalizar)
        #rango seguiendo la formular de datoMayor - datosMenor
        self.rango = self.datoMayor - self.datoMenor

        #numero de clase con ley de Sturges h~ 1+3.32log N
        poblacion = len(self.datosAnalizar)
        logaritmoDeN = log(poblacion, 10)
        self.numeroClase = 0
        if int(1+3.322*logaritmoDeN) % 2 != 0:
            self.numeroClase = int(1+3.322*logaritmoDeN)
        else:
            self.numeroClase = int(1+3.322*logaritmoDeN)+1

        #ancho de clase con la formula C=R/h
        self.anchoClase = math.ceil(self.rango/self.numeroClase)

        # print("Dato Mayor: ",self.datoMayor)
        # print("Dato Menor: ",self.datoMenor)
        # print("RANGO: ", self.rango)
        # print("Poblacion: ",poblacion)
        # print("Numero de clase es: ", self.numeroClase)
        # print("Ancho de clase: ", self.anchoClase)

    def limiteInferiorAparente(self):
        limInfAparente = []
        valor = self.datoMenor
        while(valor <= self.datoMayor):
            limInfAparente.append(valor)
            valor+= self.anchoClase
        return limInfAparente

    def limiteSuperiorAparente(self):
        limSupAparente = []
        valor = self.datoMenor
        while(valor <= self.datoMayor):
            valor+= self.anchoClase
            limSupAparente.append(valor)
        return limSupAparente

    def limiteInferiorReales(self):
        limInfReal = []
        valor = self.datoMenor
        while(valor <= self.datoMayor):
            limInfReal.append(valor-0.5)
            valor+= self.anchoClase
        return limInfReal

    def limiteSuperiorReales(self):
        limSupReal = []
        valor = self.datoMenor
        while(valor <= self.datoMayor):
            valor+= self.anchoClase
            limSupReal.append(valor+0.5)
        return limSupReal

    #Marca de clase (LimiteInferior+LimiteSuperior)/2
    def marcaDeClase(self):
        marcaClase = []
        valor = self.datoMenor
        while(valor <= self.datoMayor):
            x=(valor+(valor+self.anchoClase))/2
            marcaClase.append(int(x))
            #print(valor,"+",valor+self.anchoClase, "/", 2)
            valor+= self.anchoClase
        return marcaClase

    #la cantidad de datos que aparecen dentro del rango
    def frecuenciaEntreClase(self):
        frecuenciaAlmacenada = []
        valores = self.datosAnalizar
        valores.sort()
        limite = self.datoMenor
        frecuCont = 0
        while(limite <= self.datoMayor):
            for i in valores:
                if i >= limite and i < limite + self.anchoClase:
                    frecuCont+=1;
            frecuenciaAlmacenada.append(frecuCont)
            frecuCont = 0
            limite += self.anchoClase
        return frecuenciaAlmacenada

    #frecuencia relativa
    def frecuenciaRelativa(self):
        frecuenciaRela = []
        valores = self.datosAnalizar
        valores.sort()
        limite = self.datoMenor
        frecuCont = 0
        while(limite <= self.datoMayor):
            for i in valores:
                if i >= limite and i < limite + self.anchoClase:
                    frecuCont+=1;
            frecuenciaRela.append(frecuCont/self.poblacion)
            frecuCont = 0
            limite += self.anchoClase
        return frecuenciaRela

    #frecuencia relativa porcentual
    def frecuenciaRelativaPorcent(self):
        frecuenciaRelaPorcent = []
        valores = self.datosAnalizar
        valores.sort()
        limite = self.datoMenor
        frecuCont = 0
        while(limite <= self.datoMayor):
            for i in valores:
                if i >= limite and i < limite + self.anchoClase:
                    frecuCont+=1;
            frecuenciaRelaPorcent.append((frecuCont/self.poblacion)*100)
            frecuCont = 0
            limite += self.anchoClase
        return frecuenciaRelaPorcent

    #frecuencia acumulada ascendente
    def frecuenciaAcumuladaAscendente(self):
        frecuenciaAcumulada = []
        valores = self.datosAnalizar
        valores.sort()
        limite = self.datoMenor
        frecuCont = 0
        while(limite <= self.datoMayor):
            for i in valores:
                if i >= limite and i < limite + self.anchoClase:
                    frecuCont+=1;
            frecuenciaAcumulada.append(frecuCont)
            limite += self.anchoClase
        return frecuenciaAcumulada

    #frecuencia acumulada ascendente relativa
    def frecuenciaAcumuladaAscendenteR(self):
        frecuenciaAcumuladaAscentR = []
        valores = self.datosAnalizar
        valores.sort()
        limite = self.datoMenor
        frecuCont = 0
        while(limite <= self.datoMayor):
            for i in valores:
                if i >= limite and i < limite + self.anchoClase:
                    frecuCont+=1;
            frecuenciaAcumuladaAscentR.append((frecuCont/self.poblacion))
            limite += self.anchoClase
        return frecuenciaAcumuladaAscentR
    #frecuencia absoluta acumulada porcentual
    def frecuenciaAcumuladaAscendentePorcent(self):
        frecuenciaAcumuladaAscentP = []
        valores = self.datosAnalizar
        valores.sort()
        limite = self.datoMenor
        frecuCont = 0
        while(limite <= self.datoMayor):
            for i in valores:
                if i >= limite and i < limite + self.anchoClase:
                    frecuCont+=1;
            frecuenciaAcumuladaAscentP.append((frecuCont/self.poblacion)*100)
            limite += self.anchoClase
        return frecuenciaAcumuladaAscentP

    def frecuenciaAcumuladaDescendente(self):
        frecuenciaAcumuladaD = []
        valores = self.datosAnalizar
        valores.sort()
        limite = self.datoMenor
        dMayor = self.poblacion
        frecuCont = 0

        while(limite <= self.datoMayor):
            for i in valores:
                if i >= limite and i < limite + self.anchoClase:
                    frecuCont+=1;

            frecuenciaAcumuladaD.append(dMayor)
            dMayor -= frecuCont;
            frecuCont = 0
            limite += self.anchoClase
        return frecuenciaAcumuladaD

    def frecuenciaAcumuladaDescendenteRelativa(self):
        frecuenciaAcumuladaDR = []
        valores = self.datosAnalizar
        valores.sort()
        limite = self.datoMenor
        dMayor = self.poblacion
        frecuCont = 0

        while(limite <= self.datoMayor):
            for i in valores:
                if i >= limite and i < limite + self.anchoClase:
                    frecuCont+=1;

            frecuenciaAcumuladaDR.append(dMayor/self.poblacion)
            dMayor -= frecuCont;
            frecuCont = 0
            limite += self.anchoClase
        return frecuenciaAcumuladaDR

    def frecuenciaAcumuladaDescendenteRelativaPorcentual(self):
        frecuenciaAcumuladaDRP = []
        valores = self.datosAnalizar
        valores.sort()
        limite = self.datoMenor
        dMayor = self.poblacion
        frecuCont = 0

        while(limite <= self.datoMayor):
            for i in valores:
                if i >= limite and i < limite + self.anchoClase:
                    frecuCont+=1;

            frecuenciaAcumuladaDRP.append((dMayor/self.poblacion)*100)
            dMayor -= frecuCont;
            frecuCont = 0
            limite += self.anchoClase
        return frecuenciaAcumuladaDRP