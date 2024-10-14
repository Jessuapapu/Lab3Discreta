from flask import Flask, render_template, request, url_for
import Declaraciones
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import io
import os
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
        return render_template("index.html")


@app.route("/cal", methods=["GET","POST"])
def calculadora():
        if (request.method == "POST"):
                if not request.form.get("ConjuntoA"):
                        return render_template("apology.html",x="A")
                if not request.form.get("ConjuntoB"):
                        return render_template("apology.html",x="B")
                if not request.form.get("ConjuntoC"):
                        return render_template("apology.html",x="C")
                if not request.form.get("operacion"):
                        return render_template("apology.html",x="Operacion")

                str1 = request.form.get("ConjuntoA")
                str2 = request.form.get("ConjuntoB")
                str3 = request.form.get("ConjuntoC")
                Ecuacion = request.form.get("operacion")
                
                print(str1)
                
                if not Declaraciones.verificacion(str1) or not Declaraciones.verificacion(str2) or not Declaraciones.verificacion(str3):
                    return render_template("apology.html",x=" ")

                Conjunto_A = Declaraciones.CrearConjunto(str(str1))
                Conjunto_B = Declaraciones.CrearConjunto(str(str2))
                Conjunto_C = Declaraciones.CrearConjunto(str(str3))

                print(Conjunto_A)
                print(Conjunto_B)
                print(Conjunto_C)
                # Guardar el diagrama en un archivo temporal
                #si ya se hizo el archivo se borra si no se crea
                img_path = os.path.join('static', 'venn_diagram.png')

                # Verificar si el archivo existe y eliminarlo
                if os.path.exists(img_path):
                        try:
                                os.remove(img_path)
                                print("Archivo eliminado:", img_path)
                        except Exception as e:
                                print("Error al eliminar el archivo:", e)

               
                 # Crear el diagrama de Venn
                plt.figure(figsize=(8, 8))
                v = venn3([Conjunto_A, Conjunto_B, Conjunto_C], ('Conjunto A', 'Conjunto B', 'Conjunto C'))

                
                # Actualizar las etiquetas de forma segura
                labels = {
                '100': f'A: {len(Conjunto_A)}',
                '010': f'B: {len(Conjunto_B)}',
                '001': f'C: {len(Conjunto_C)}',
                '110': f'A ∩ B: {len(Conjunto_A & Conjunto_B)}',
                '101': f'A ∩ C: {len(Conjunto_A & Conjunto_C)}',
                '011': f'B ∩ C: {len(Conjunto_B & Conjunto_C)}',
                '111': f'A ∩ B ∩ C: {len(Conjunto_A & Conjunto_B & Conjunto_C)}'
                }


                # Guardar el diagrama
                img_path = os.path.join('static', 'venn_diagram.png')
                plt.savefig(img_path)
                plt.close()
                        
                return render_template("Diagrama.html",img_path=img_path)
        else:
                return render_template("Calculadora.html")
