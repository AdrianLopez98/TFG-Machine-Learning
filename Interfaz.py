from tkinter import *
import csv
import RedNeuronal as RN


def login():

    with open("bbdd.csv","r") as f:
        leido=csv.reader(f)
        flag=False
        print(nombre2.get())
        for row in leido:
            if nombre2.get() in row:
                flag=True


def register():
    with open("bbdd.csv","r+",newline="") as f:
        escritor=csv.writer(f)
        leido=csv.reader(f)
        flag=False
        for row in leido:
            if nombre2.get() in row:
                flag=True

        if flag==False:
            escritor.writerow([nombre2.get(),password2.get()])
        elif flag==True:
            print("Ya existe!!")

pantalla=Tk()
pantalla.title("Login")

nombre=Label(pantalla,text="Nombre")
password=Label(pantalla,text="Contraseña")

nombre2=Entry(pantalla)
password2=Entry(pantalla,show="*",relief="sunken")

login=Button(text="Login",command=login,relief="groove")
register=Button(text="Register",command=register,relief="groove")

imagen=PhotoImage(file="Imagenes/edificio.png")
imagen=imagen.subsample(3,3)
imagenposi=Label(pantalla,image=imagen,width=300,height=200)

nombre.place(x=50, y=50)
password.place(x=50, y=100)
nombre2.place(x=200, y=50)
password2.place(x=200, y=100)
login.place(x=200,y=200)
register.place(x=250,y=200)
imagenposi.place(x=100,y=300)
pantalla.configure(width=900,height=700)
pantalla.mainloop()

