from tkinter import *
import pymysql

def login():

    db=pymysql.connect("localhost","root","","adrianlopez")
    cursor=db.cursor()
    cursor.execute("select * from usuarios")
    resultado=cursor.fetchall()

    esta=False
    for usuario in resultado:

        if (nombre2.get(),password2.get())==usuario:
            esta=True


    if esta==True:
        pantalla.quit()
        pantalla.destroy()
        import InterfazDatos
    else:
        from tkinter import messagebox
        messagebox.showwarning("Error", "Necesita registrarse en la base de datos")

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
        from tkinter import messagebox
        messagebox.showinfo("Registrado con éxito", "Se ha registrado satisfactoriamente en la base de datos")
    cursor2.close()
    db.close()





pantalla=Tk()
pantalla.title("House price prediction for California")

nombre=Label(pantalla,text="Nombre")
password=Label(pantalla,text="Contraseña")
leyenda=Label(pantalla,text="Usted va a trabajar con los datos de California")


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
leyenda.place(x=140,y=550)
pantalla.geometry("500x650-700-250")
pantalla.mainloop()




