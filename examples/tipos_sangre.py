
import sys
sys.path.append("../modules/frecuencias")
import frecuencias as fr


carros = ["A","A","A","A","A","O","O","O","O","O","O","O","O","O","B",
        "B","B","B","B","B","B","AB","AB","AB","AB"]

nuevoDato = fr(carros)
print("Poblacion es de: ", nuevoDato.poblacion())
print("Dato tabla", nuevoDato.infoData())
print("Dato frecuencia", nuevoDato.infoFrecu())
print("Frecuencia relativa porcentual", nuevoDato.frecuenciaRelativa())
print("Frecuencia relativa", nuevoDato.frecuenciaRelativaPorcen())

