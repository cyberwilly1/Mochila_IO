from tkinter import *
from .menu_problema import menu_problema
from .resultado import resultado

from .Solucion.Mochila import Mochila
from .Solucion.Item import Item


class ingreso_datos:
    def __init__(self,cant,cap):
        self.cant = cant
        self.cap = cap

        # Creacion de la ventana problema
        self.x=420
        self.y=250
        self.ventana = Tk()
        if(self.cant >=2 and self.cant<=7):
            self.x = self.x + (1*self.cant )
            self.y = self.y + (20*self.cant )
        else:
            self.x = self.x + (2*self.cant )
            self.y = self.y + (30*self.cant )

        self.x1=self.ventana.winfo_screenwidth()// 2 - self.x // 2
        self.y1=self.ventana.winfo_screenheight()// 2 - self.y // 2


        self.ventana.geometry(f'{self.x}x{self.y}+{self.x1}+{self.y1}')
        self.ventana.resizable(0,0)
        self.ventana.title("Asignacion caso mochila")
        self.ventana.config(bg="linen")
      

        #Llamada al menu problema
        menu_problema(self.ventana)   


        self.etiquetas_datos()

        # Creacion del marco matriz
        self.matriz_problema = Frame(self.ventana)
        self.genera_matriz()
        self.matriz_problema.pack()

        #Boton cancelar
        self.cancelar=Button(self.ventana, text="Cancelar",command=self.cancelar,bg="lavender")
        self.cancelar.pack(side=LEFT,padx=65,pady=15)
        

        #Boton correr
        # self.ok=Button(self.ventana, text="Correr",command=self.get_datos_tabla,bg="lavender")
        self.ok=Button(self.ventana, text="Correr",command=self.solucionar_problema,bg="lavender")
        self.ok.pack(side=RIGHT,padx=70,pady=15)


        self.ventana.mainloop()

# Creacion de la funcion que genera la matriz 
    def genera_matriz(self):
        self.matriz = []
        for r in range(0,self.cant):
            fila = []
            for c in range(0, 3):
                celda = Entry(self.matriz_problema, width=12)
                celda.grid(padx=5, pady=5, row=r, column=c)
                # celda.insert(0, '({}, {})'.format(r, c))
                celda.config(fg="white",    # letras
                            bg="skyblue",   # fondo
                            font=("Verdana",12))
                fila.append(celda)
            self.matriz.append(fila)

    
    def generar_ventana_solucion(self, soluciones, pesos, utilidad):
        print("self cantidad ",self.cant)
        resultado(self.cant, soluciones, pesos, utilidad)
        
    def get_datos_tabla(self):
        nombres = []
        pesos = []
        utilidades = []
        for fila in self.matriz:
            nombres.append(fila[0].get())
            pesos.append(int(fila[1].get()))
            utilidades.append(int(fila[2].get()))
        return nombres, pesos, utilidades

    def auto_completar(self):
        nom = ('producto 1', 'producto 2', 'producto 3')
        pe = ('12', '5', '7')
        uti = ('4', '2', '1')
        for i, fila in enumerate(self.matriz):
            fila[0].insert(0,nom[i])
            fila[1].insert(0,pe[i])
            fila[2].insert(0,uti[i])

    def solucionar_problema(self):
        self.auto_completar()
        nombres, pesos, utilidades = self.get_datos_tabla()
        items = []
        for n, p, u in zip(nombres, pesos, utilidades):
            items.append(Item(n, p, u))
        mochila = Mochila(self.cap, items)
        mochila.crear_etapas()
        mochila.resolver()
        soluciones = mochila.get_soluciones()
        pesos_sol = mochila.get_pesos_sol()
        utilidad_sol = mochila.get_utilidad_neta()

        self.generar_ventana_solucion(soluciones, pesos_sol, utilidad_sol)

#Creacion de otras Ventanas
    def cancelar(self):
        self.ventana.destroy()


    def etiquetas_datos(self):

        self.etq_capacidad=Label(self.ventana, text=f'Capacidad de la mochila : {self.cap}',bg="linen")
        self.etq_capacidad.pack(side=TOP)
        
        self.etq_cantidad=Label(self.ventana, text=f'Cantidad de articulos : {self.cant}',bg="linen")
        self.etq_cantidad.pack(side=TOP)

        self.etq_datos=Label(self.ventana, text="      Articulos                Peso                     Utilidad",bg="linen")
        self.etq_datos.pack(side=TOP)

    