from tkinter import *

def prepa():

    import RedNeuronal
    rn=RedNeuronal
    rn.escribir()



def reset():

    Tprecio.delete(0,len(Tprecio.get()))
    Tlongitud.delete(0,len(Tlongitud.get()))
    Tlatitud.delete(0,len(Tlatitud.get()))
    Tmedia_años.delete(0,len(Tmedia_años.get()))
    Tsalario.delete(0,len(Tsalario.get()))
    Thabitaciones.delete(0,len(Thabitaciones.get()))
    Tbaños.delete(0,len(Tbaños.get()))
    Tmetros.delete(0,len(Tmetros.get()))


def mostrarr():

    import RedNeuronal
    rn = RedNeuronal
    rn.mostrar()


pantalla2=Tk()
pantalla2.title("Rellene los datos")

#etiquetas
longitud=Label(pantalla2,text="Longitud (mirar mapa, eje x)",)
latitud=Label(pantalla2,text="Latitud (mirar mapa, eje y)")
media_años=Label(pantalla2,text="Antigüedad")
habitaciones=Label(pantalla2,text="Habitaciones")
baños=Label(pantalla2,text="Baños")
metros=Label(pantalla2,text="Metros cuadrados")
salario=Label(pantalla2,text="Salario medio")
precio=Label(pantalla2,text="Precio")
proximidad=Label(pantalla2,text="Proximidad")

#componentes

Tlongitud=Entry(pantalla2)
Tlatitud=Entry(pantalla2)
Tmedia_años=Entry(pantalla2)
Thabitaciones=Entry(pantalla2)
Tbaños=Entry(pantalla2)
Tmetros=Entry(pantalla2)
Tsalario=Entry(pantalla2)
Tprecio=Entry(pantalla2)

var=StringVar(pantalla2)

lista=["NEAR BAY", "<1H OCEAN", "INLAND", "NEAR OCEAN"]
Cproximidad=OptionMenu(pantalla2,var,*lista)

#botones
Bboton=Button(pantalla2,text="Hacer prediccion",command=prepa)
BbotonReset=Button(pantalla2,text="Resetear",command=reset)
BbotonMapa=Button(pantalla2,text="Mapa",command=mostrarr)


longitud.place(x=50, y=50)
latitud.place(x=50, y=100)
Tlongitud.place(x=220, y=50)
Tlatitud.place(x=220, y=100)
media_años.place(x=50, y=150)
habitaciones.place(x=50, y=200)
Tmedia_años.place(x=220, y=150)
Thabitaciones.place(x=220, y=200)
baños.place(x=50, y=250)
Tbaños.place(x=220, y=250)
metros.place(x=50, y=300)
Tmetros.place(x=220, y=300)
salario.place(x=50, y=350)
Tsalario.place(x=220, y=350)
proximidad.place(x=50,y=400)
Cproximidad.place(x=220,y=400)

precio.place(x=350, y=500)
Tprecio.place(x=400, y=500)

Bboton.place(x=100,y=500)
BbotonReset.place(x=100,y=550)
BbotonMapa.place(x=100,y=600)




pantalla2.geometry("900x700-500-250")
pantalla2.mainloop()



