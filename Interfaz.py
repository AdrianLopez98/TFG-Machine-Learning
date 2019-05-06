from tkinter import *
import pymysql

def login():

    db=pymysql.connect("localhost","root","","adrianlopez")
    cursor=db.cursor()
    cursor.execute("select * from usuarios")
    resultado=cursor.fetchall()

    for usuario in resultado:

        if nombre2.get() and password2.get() in usuario:
            import InterfazDatos




    print(resultado)

    cursor.close()
    db.close()

def register():
    db = pymysql.connect("localhost","root","","adrianlopez")
    cursor = db.cursor()
    cursor2 = db.cursor()
    cursor.execute("select * from usuarios")
    resultado=cursor.fetchall()
    cursor.close()

    booleano=False

    nom=nombre2.get()
    pas=password2.get()
    for usuario in resultado:

        if nombre2.get() and password2.get() in usuario:
            booleano=True

    if booleano==False:
        cursor2.execute('insert into usuarios values("%s", "%s")' % \
                        (nom, pas))
        db.commit()
        print("insert hecho")
    print(resultado)
    cursor2.close()
    db.close()





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




