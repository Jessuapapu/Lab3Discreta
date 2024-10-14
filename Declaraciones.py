import re
#clase de Conjuntos
import re


def CrearConjunto(cadena: str):
    """
    Utiliza expresiones regulares para limpiar la cadena de entrada,
    eliminando espacios y comas adicionales. Convierte los elementos válidos a enteros
    y los guarda en el atributo 'Conjunto' del objeto.
    """
    # Limpiar la cadena, eliminar espacios y comas adicionales, y dividir en elementos
    elementos_limpios = re.sub(r"(,*)(?:\s+)", " ", cadena).replace(",", " ").split()
    
    # Convertir a enteros y crear un conjunto
    conjunto = set(int(elemento) for elemento in elementos_limpios if elemento.isdigit())
    
    return conjunto

def verificacion(str):

    for i in str:
        if i.isalpha():
            return False
    
    return True


def evaluar_ecuacion(ecuacion, conjunto1, conjunto2, conjunto3):
    # Mapear los nombres de los conjuntos a variables A, B, C
    A = conjunto1
    B = conjunto2
    C = conjunto3

    # Evaluar la expresión usando eval (precaución con su uso en un entorno real)
    try:
        resultado = eval(ecuacion)
    except Exception as e:
        resultado = f"Error en la ecuación: {str(e)}"

    return resultado

