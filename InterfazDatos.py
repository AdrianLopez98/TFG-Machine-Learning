from tkinter import *


pantalla2=Tk()
pantalla2.title("Rellene los datos")

#etiquetas
longitud=Label(pantalla2,text="Longitud",)
latitud=Label(pantalla2,text="Latitud")
media_años=Label(pantalla2,text="Antigüedad")
habitaciones=Label(pantalla2,text="Habitaciones")
baños=Label(pantalla2,text="Baños")
poblacion=Label(pantalla2,text="Población")
habitaciones=Label(pantalla2,text="Habitaciones")
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
Tpoblacion=Entry(pantalla2)
Thabitaciones=Entry(pantalla2)
Tmetros=Entry(pantalla2)
Tsalario=Entry(pantalla2)
Tprecio=Entry(pantalla2)

var=StringVar=(pantalla2)

lista=["NEAR BAY", "<1H OCEAN", "INLAND", "NEAR OCEAN"]
Cproximidad=OptionMenu(pantalla2,var,*lista)

longitud.place(x=50, y=50)
latitud.place(x=50, y=100)
Tlongitud.place(x=200, y=50)
Tlatitud.place(x=200, y=100)
media_años.place(x=50, y=150)
habitaciones.place(x=50, y=200)
Tmedia_años.place(x=200, y=150)
Thabitaciones.place(x=200, y=200)
baños.place(x=50, y=250)
poblacion.place(x=50, y=300)
Tbaños.place(x=200, y=250)
Tpoblacion.place(x=200, y=300)
habitaciones.place(x=50, y=350)
metros.place(x=50, y=400)
Thabitaciones.place(x=200, y=350)
Tmetros.place(x=200, y=400)
salario.place(x=50, y=450)
precio.place(x=50, y=500)
Tsalario.place(x=200, y=450)
Tprecio.place(x=200, y=500)
proximidad.place(x=50,y=550)
Cproximidad.place(x=200,y=550)


pantalla2.configure(width=900,height=700)
pantalla2.mainloop()

