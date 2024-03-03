import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Circle

class MiInterfazUnica:
    def _init_(self, master):
        """
        Inicia una interfaz gráfica con tres conjuntos y permite la interacción con ellos.

        :param master: El objeto principal de la interfaz gráfica.
        """
        self.master = master
        self.master.title("conjuntos error #6 ")

        # Elementos de la interfaz gráfica
        self.label_conjunto_a = ttk.Label(self.master, text="Grupo A:")
        self.label_conjunto_b = ttk.Label(self.master, text="Grupo B:")
        self.label_conjunto_c = ttk.Label(self.master, text="Grupo C:")

        self.entry_a = ttk.Entry(self.master)
        self.entry_b = ttk.Entry(self.master)
        self.entry_c = ttk.Entry(self.master)

        self.var_mostrar_a = tk.IntVar()
        self.var_mostrar_b = tk.IntVar()
        self.var_mostrar_c = tk.IntVar()

        self.checkbox_a = ttk.Checkbutton(self.master, text="Mostrar Grupo A", variable=self.var_mostrar_a, command=self.mostrar_interseccion)
        self.checkbox_b = ttk.Checkbutton(self.master, text="Mostrar Grupo B", variable=self.var_mostrar_b, command=self.mostrar_interseccion)
        self.checkbox_c = ttk.Checkbutton(self.master, text="Mostrar Grupo C", variable=self.var_mostrar_c, command=self.mostrar_interseccion)

        self.figura, self.eje = plt.subplots()

        self.lienzo = FigureCanvasTkAgg(self.figura, master=self.master)
        self.lienzo_widget = self.lienzo.get_tk_widget()
        self.lienzo_widget.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

        # Ubicar elementos en la cuadrícula con dirección "w"
        self.label_conjunto_a.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_a.grid(row=0, column=1, padx=10, pady=10)
        self.checkbox_a.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        self.label_conjunto_b.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_b.grid(row=1, column=1, padx=10, pady=10)
        self.checkbox_b.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        self.label_conjunto_c.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_c.grid(row=2, column=1, padx=10, pady=10)
        self.checkbox_c.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        # Mostrar la intersección y diferencias inicialmente
        self.mostrar_interseccion()

    def mostrar_interseccion(self):
        """
        Calcula y muestra la intersección y las diferencias entre los conjuntos seleccionados.
        Actualiza el gráfico en el lienzo con círculos de colores representando los conjuntos.
        """
        conjunto_a = set(self.entry_a.get().split())
        conjunto_b = set(self.entry_b.get().split())
        conjunto_c = set(self.entry_c.get().split())

        mostrar_a = self.var_mostrar_a.get()
        mostrar_b = self.var_mostrar_b.get()
        mostrar_c = self.var_mostrar_c.get()

        conjunto_combinado = set()

        if mostrar_a:
            conjunto_combinado.update(conjunto_a)

        if mostrar_b:
            conjunto_combinado.update(conjunto_b)

        if mostrar_c:
            conjunto_combinado.update(conjunto_c)

        conjunto_combinado = sorted(set(conjunto_combinado))

        interseccion = conjunto_a.intersection(conjunto_b, conjunto_c)
        diferencia_a_b = conjunto_a.difference(conjunto_b)
        diferencia_b_a = conjunto_b.difference(conjunto_a)
        diferencia_a_c = conjunto_a.difference(conjunto_c)
        diferencia_c_b = conjunto_c.difference(conjunto_b)

        resultado_interseccion = ", ".join(interseccion)
        resultado_diferencia_a_b = ", ".join(diferencia_a_b)
        resultado_diferencia_b_a = ", ".join(diferencia_b_a)
        resultado_diferencia_a_c = ", ".join(diferencia_a_c)
        resultado_diferencia_c_b = ", ".join(diferencia_c_b)

        resultado_label = ttk.Label(self.master, text=f"IINTERSECCION: {resultado_interseccion}\n"
                                                      f"Diferencia A - B: {resultado_diferencia_a_b}\n"

                                                      f"Diferencia B - A: {resultado_diferencia_b_a}\n"

                                                      f"Diferencia A - C: {resultado_diferencia_a_c}\n"

                                                      f"Diferencia C - B: {resultado_diferencia_c_b}")
        resultado_label.grid(row=3, column=0, columnspan=1, pady=3)

        colores = ['cyan', 'magenta', 'blue']
        self.dibujar_circulos(self.eje, conjunto_combinado, colores)
        self.lienzo.draw()

    def dibujar_circulos(self, eje, conjunto, colores):
        
        # círculos en un eje con colores diferentes .

        #El eje en el que se dibujarán los círculos.
        #El conjunto de elementos a representar.
        #La lista de colores para asignar a cada elemento del conjunto.
        
        eje.clear()
        eje.set_title("Conjuntos A, B, y C")
        eje.set_aspect('equal', adjustable='box')
        eje.axis('off')

        for idx, (elemento, color) in enumerate(zip(conjunto, colores)):
            x_posicion = 0.2 * (idx + 1)
            circulo = Circle((x_posicion, 0.5), 0.15, color=color, alpha=0.7)
            eje.add_patch(circulo)
            eje.text(x_posicion, 0.5, elemento, color='white', va='center', ha='center', fontsize=10)

if __name__ == "_main_":
    raiz = tk.Tk()
    app = MiInterfazUnica(raiz)
    raiz.mainloop()