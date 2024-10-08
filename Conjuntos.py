import re 
import Declaraciones

# verificar si no es un caracter
def verificacion(str):

    for i in str:
        if i.isalpha():
            return False
    
    return True

def CrearConjuntos(str):
    """ con expreciones regulares logramos evitar problemas de convercion del str obtenido desde la 
    interfaz eliminando espacios (" ") de y "," de mas """
    str2 = re.sub(r"(,*)(?:\s+)", " ", str).replace(","," ").split(" ")

    intConjunto = []
    for i in str2:
        try:
            intConjunto.append(int(i))
        except:
            continue

    return intConjunto

# Python ya tiene funciones que ya establecen y aplican la ley de los conjuntos
def InterseccionConjuntos(Con1,Con2):
    Con1 = set(Con1)
    Con2 = set(Con2)
    return Con1 & Con2  

def UnionDeconjuntos(Con1,Con2):
    Con1 = set(Con1)
    Con2 = set(Con2)
    return Con1 | Con2

def  DiferenciaConjuntos(Con1,Con2):
    Con1 = set(Con1)
    Con2 = set(Con2)
    return Con1 - Con2

def DisyuncionConjuntos(Con1,Con2):
    Con1 = set(Con1)
    Con2 = set(Con2)
    return Con1.isdisjoint(Con2)

def ComSubConjuntos(Con1,Con2):
    Con1 = set(Con1)
    Con2 = set(Con2)
    return Con1.issubset(Con2)

def Operacion(str,Con1,Con2):

    Pasar1 = verificacion(Con1)
    Pasar2 = verificacion(Con2)

    if Pasar1 == False and Pasar2 == False:
        print("datos NO ingresados correctos")
        return []

    Declaraciones.con1 = CrearConjuntos(Con1)
    Declaraciones.con2 = CrearConjuntos(Con2)

    

    strLista = []
    
    for i in str:
        strLista.append(i)

    for i in range(0,len(strLista)):

        if strLista[i] == "U":
            if strLista[i-1] == "A" and strLista[i+1] == "B":
                Declaraciones.ConjuntoD = UnionDeconjuntos(Declaraciones.con1,Declaraciones.con2)

Operacion("AUB","1,2,3,45","10,9,2,3,45")

print(Declaraciones.con1)
print(Declaraciones.con2)
print(Declaraciones.ConjuntoD)

