from flask import Flask, render_template, request


import Declaraciones
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/cal", methods=["GET", "POST"])
def calculadora():
    if request.method == "POST":
        # Validar la entrada de los conjuntos y la operación
        if not request.form.get("ConjuntoA"):
            return render_template("apology.html", x="A")
        if not request.form.get("ConjuntoB"):
            return render_template("apology.html", x="B")
        if not request.form.get("ConjuntoC"):
            return render_template("apology.html", x="C")
        if not request.form.get("operacion"):
            return render_template("apology.html", x="Operación")


        # Obtener los conjuntos y la ecuación desde el formulario
        str1 = request.form.get("ConjuntoA")
        str2 = request.form.get("ConjuntoB")
        str3 = request.form.get("ConjuntoC")
        ecuacion = request.form.get("operacion")

        # Validar la sintaxis de los conjuntos
        if not Declaraciones.verificacion(str1) or not Declaraciones.verificacion(str2) or not Declaraciones.verificacion(str3):
            return render_template("apology.html", x=" ")

        # Crear los conjuntos a partir de la entrada
        Conjunto_A = set(Declaraciones.CrearConjunto(str1))
        Conjunto_B = set(Declaraciones.CrearConjunto(str2))
        Conjunto_C = set(Declaraciones.CrearConjunto(str3))

        # Calcular el conjunto universal como la unión de los tres conjuntos
        Conjunto_U = Conjunto_A | Conjunto_B | Conjunto_C

        print(Conjunto_A)
        print(Conjunto_B)
        print(Conjunto_C)
        print(Conjunto_U)
        # Evaluar la ecuación en términos de los conjuntos
        try:
            resultado = eval(ecuacion, {"A": Conjunto_A, "B": Conjunto_B, "C": Conjunto_C})
        except Exception as e:
            return f"Error al evaluar la ecuación: {e}"

        # Crear el diagrama de Venn
        plt.figure(figsize=(15, 15))
        
        # Asegúrate de que los conjuntos no estén vacíos
        if Conjunto_A or Conjunto_B or Conjunto_C:
            v = venn3([Conjunto_A, Conjunto_B, Conjunto_C], ('Conjunto A', 'Conjunto B', 'Conjunto C'))

            # Configurar las etiquetas de los conjuntos solo si existen
            if Conjunto_A:
                label_A = v.get_label_by_id('100')
                if label_A is not None:
                    label_A.set_text('\n'.join(map(str, Conjunto_A)))
            if Conjunto_B:
                label_B = v.get_label_by_id('010')
                if label_B is not None:
                    label_B.set_text('\n'.join(map(str, Conjunto_B)))
            if Conjunto_C:
                label_C = v.get_label_by_id('001')
                if label_C is not None:
                    label_C.set_text('\n'.join(map(str, Conjunto_C)))

            # Mostrar los elementos de las intersecciones
            label_AB = v.get_label_by_id('110')
            if label_AB is not None:
                label_AB.set_text('\n'.join(map(str, Conjunto_A & Conjunto_B)))  # A & B

            label_AC = v.get_label_by_id('101')
            if label_AC is not None:
                label_AC.set_text('\n'.join(map(str, Conjunto_A & Conjunto_C)))  # A & C

            label_BC = v.get_label_by_id('011')
            if label_BC is not None:
                label_BC.set_text('\n'.join(map(str, Conjunto_B & Conjunto_C)))  # B & C

            # Mostrar el resultado en el centro
            label_ABC = v.get_label_by_id('111')
            if label_ABC is not None:
                label_ABC.set_text('\n'.join(map(str, resultado)))  # A & B & C
        
        img_path = os.path.join('static', 'venn_diagram.png')
        plt.title('Diagrama de Venn')
        plt.savefig(img_path)
        plt.close()

        # Devuelve la ruta de la imagen correcta sin comillas
        return render_template("Diagrama.html", resultado=resultado, img_path=img_path, Conjunto_A=Conjunto_A, Conjunto_B=Conjunto_B, Conjunto_C=Conjunto_C, Conjunto_U=Conjunto_U, ecuacion=ecuacion)
    else:
        return render_template("Calculadora.html")
