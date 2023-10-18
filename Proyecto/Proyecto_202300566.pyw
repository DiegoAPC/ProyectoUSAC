from tkinter import *
import tkinter as tk
from tkinter import messagebox
import re
import hashlib
import os


programa=Tk()
programa.title("INICIAR SESIÓN")
programa.geometry("800x800") 

#Ventana Inicio registro de estudiantes
def ventanaRes():
    ventana2 = tk.Toplevel()
    ventana2.title("REGISTRO DE SESIÓN DE ESTUDIANTES")
    ventana2.geometry("500x600")
    lbl1 = Label(ventana2, text="REGISTRAR CUENTA", fg ="black")
    lbl1.place(relx=0.25, rely=0.02, relwidth=0.5, relheight = 0.1)
    lbl2 = Label(ventana2, text="NOMBRE", fg ="black") 
    lbl2.place(x=50, y=70, width=100, height = 40)
    lbl3 = Label(ventana2, text="APELLIDO", fg ="black")
    lbl3.place(x=50, y=120, width=100, height = 40)
    lbl4 = Label(ventana2, text="DPI", fg ="black") 
    lbl4.place(x=35, y=170, width=100, height = 40)
    lbl5 = Label(ventana2, text="FECHA DE NACIMIENTO", fg ="black")
    lbl5.place(x=63, y=220, width=150, height = 40)
    lbl6 = Label(ventana2, text="TELÉFONO", fg ="black") 
    lbl6.place(x=50, y=270, width=100, height = 40)
    lbl7 = Label(ventana2, text="NOMBRE DE USUARIO", fg ="black")
    lbl7.place(x=58, y=320, width=150, height = 40)
    lbl8 = Label(ventana2, text="DIRECCIÓN DE CORREO ELECTRÓNICO", fg ="black") 
    lbl8.place(x=60, y=370, width=230, height = 40)
    lbl9 = Label(ventana2, text="CONTRASEÑA", fg ="black")
    lbl9.place(x=60, y=420, width=100, height = 40)
    lbl10 = Label(ventana2, text="CONFIRMACIÓN DE CONTRASEÑA", fg ="black")
    lbl10.place(x=65, y=470, width=200, height = 40)

    #Registro de datos del usuario
    Nombre = StringVar()
    Apellido = StringVar()
    DPI = StringVar()
    FechaNacimiento = StringVar()
    Telefono = StringVar()
    Nombreusuario = StringVar()
    Correo = StringVar()
    Contraseña = StringVar()
    Confirmacioncontraseña = StringVar()
    
    #Acción de almacenar los datos
    def EnviarDatos():
        Nombre_dato = Nombre.get()
        Apellido_dato = Apellido.get()
        DPI_dato = DPI.get()
        FechaNacimiento_dato = FechaNacimiento.get()
        Telefono_dato = Telefono.get()
        Nombreusuario_dato = Nombreusuario.get()
        Correo_dato = Correo.get()
        Contraseña_dato = str(Contraseña.get())
        Confirmacioncontraseña_dato = str(Confirmacioncontraseña.get())
        
        #Verificar que los campos tengan datos a registrar
        if not Nombre_dato or not Apellido_dato or not DPI_dato or not FechaNacimiento_dato or not Telefono_dato or not Nombreusuario_dato or not Correo_dato or not Contraseña_dato or not Confirmacioncontraseña_dato:
            messagebox.showinfo("DATOS INCOMPLETOS", "Ingrese todos los datos solicitados")
            return
    
        # Detectar que que el usuario no este ya incluido en la base de datos
        if usuarioexistente(Nombreusuario_dato):
            messagebox.showinfo("ERROR", "El nombre de usuario ya está en uso")
            return

        # Detectar que la contraseña y la confirmación de contraseña sean iguales
        if Contraseña_dato != Confirmacioncontraseña_dato:
            messagebox.showinfo("ERROR", "La contraseña y su confirmación no son iguales")
            return
        
        # Detectar que la contraseña tenga 1 digito, 1 simbolo y 8 caracteres minimo
        if not re.search(r"[A-Z]", Contraseña_dato) or \
            not re.search(r"\d", Contraseña_dato) or \
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", Contraseña_dato) or \
            len(Contraseña_dato) < 8:
            messagebox.showinfo("ERROR", "La contraseña debe contener; 8 caracteres, 1 mayuscula, 1 digito y 1 simbolo")
            return

        #Encriptar la contraseña antes de almacenarla en el archivo txt
        contracodificada = hashlib.sha256(Contraseña_dato.encode()).hexdigest()

        #Guardar Información en archivo de texto
        newfile = open("DatosUsuarios.txt", "a")
        newfile.write(Nombre_dato)
        newfile.write(",")
        newfile.write(Apellido_dato)
        newfile.write(",")
        newfile.write(DPI_dato)
        newfile.write(",")
        newfile.write(FechaNacimiento_dato)
        newfile.write(",")
        newfile.write(Telefono_dato)
        newfile.write(",")
        newfile.write(Nombreusuario_dato)
        newfile.write(",")
        newfile.write(Correo_dato)
        newfile.write(",")
        newfile.write(contracodificada)
        newfile.write(",")
        newfile.write("Estudiante")
        newfile.write("\n")
        newfile.close()

        #Guardar Usuario y contraseña para ingresar
        newfile = open("UsuariosReg.txt", "a")
        newfile.write(Nombreusuario_dato)
        newfile.write(",")
        newfile.write(Contraseña_dato)
        newfile.write(",")
        newfile.write("Estudiante")
        newfile.write("\n")
        newfile.close()

        #Vaciar el contenido de las cajas de texto
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt5.delete(0, END)
        txt6.delete(0, END)
        txt7.delete(0, END)
        txt8.delete(0, END)
        txt9.delete(0, END)


        
    #Cajas de texto de datos
    txt1 = Entry(ventana2, textvariable=Nombre)#Nombre
    txt1.config(font=("Arial",10),justify=tk.CENTER)
    txt1.place(x=300, y=70, width=175, height = 35)
    txt2 = Entry(ventana2, textvariable=Apellido)#Apellido
    txt2.config(font=("Arial",10),justify=tk.CENTER)
    txt2.place(x=300, y=120, width=175, height = 35)
    txt3 = Entry(ventana2, textvariable=DPI)#DPI
    txt3.config(font=("Arial",10),justify=tk.CENTER)
    txt3.place(x=300, y=170, width=175, height = 35)
    txt4 = Entry(ventana2, textvariable=FechaNacimiento)#Fecha de nacimiento
    txt4.config(font=("Arial",10),justify=tk.CENTER)
    txt4.place(x=300, y=220, width=175, height = 35)
    txt5 = Entry(ventana2, textvariable=Telefono)#télefono
    txt5.config(font=("Arial",10),justify=tk.CENTER)
    txt5.place(x=300, y=270, width=175, height = 35)
    txt6 = Entry(ventana2, textvariable=Nombreusuario)#Nombre de usuario
    txt6.config(font=("Arial",10),justify=tk.CENTER)
    txt6.place(x=300, y=320, width=175, height = 35)
    txt7 = Entry(ventana2, textvariable=Correo)#Correo electronico
    txt7.config(font=("Arial",10),justify=tk.CENTER)
    txt7.place(x=300, y=370, width=175, height = 35)
    txt8 = Entry(ventana2, textvariable=Contraseña, show="*")#Contraseña
    txt8.config(font=("Arial",10),justify=tk.CENTER)
    txt8.place(x=300, y=420, width=175, height = 35)
    txt9 = Entry(ventana2, textvariable=Confirmacioncontraseña, show="*")#Confirmar contraseña
    txt9.config(font=("Arial",10),justify=tk.CENTER)
    txt9.place(x=300, y=470, width=175, height = 35)

    btn1 = Button(ventana2, text="CONFIRMAR", bg = "black", fg = "white", command=EnviarDatos) #BOTÓN CONFIRMAR
    btn1.place(x=275, y=550, width=175, height = 30 )
    btn2 = Button(ventana2, text="REGRESAR", bg = "black", fg = "white", command=ventana2.destroy) #BOTÓN CERRAR VENTANA #BOTÓN CONFIRMAR
    btn2.place(x=65, y=550, width=175, height = 30 )
     


#Abrir la ventana con vista de administrador
def ventanadmin():
    root = tk.Tk()
    root.state("zoomed")  # Maximizar la ventana en Windows
    root.grid_rowconfigure(0, weight=1, uniform="rows_g1")
    root.grid_rowconfigure(1, weight=5, uniform="rows_g1")
    root.grid_columnconfigure(0, weight=1, uniform="columnag1")
    root.grid_columnconfigure(1, weight=1, uniform="columnag1")
    root.grid_columnconfigure(2, weight=1, uniform="columnag1")
    root.grid_columnconfigure(3, weight=1, uniform="columnag1")

    fm1 = tk.Frame(root, bg="blue")
    fm1.grid(row=0, column=0, columnspan=4, sticky="nsew")

    fm2 = tk.Frame(root, bg="#BDBDBD")
    fm2.grid(row=1, column=0, sticky="nsew")

    fm3 = tk.Frame(root)
    fm3.grid(row=1, column=1, sticky="nsew")

    fm4 = tk.Frame(root, bg="#BDBDBD")
    fm4.grid(row=1, column=2, sticky="nsew")

    fm5 = tk.Frame(root)
    fm5.grid(row=1, column=3, sticky="nsew")

    USER_dato = USER.get()

    tk.Label(
        fm1, text="ADMINISTRADOR: " + USER_dato, bg="blue", fg="white", font=("Arial", 32)
    ).pack(expand=True)

    btncerrar = Button(fm1, text="Cerrar Sesión", bg = "black", fg = "white", command=root.destroy) #BOTÓN CERRAR VENTANA #BOTÓN CONFIRMAR
    btncerrar.place(x=20, y=20, width=175, height = 30 )


    lbl1 = tk.Label(fm2, text="REGISTRAR CATEDRÁTICO", fg="white", bg="black", font=("Arial", 14))
    lbl1.place(x=30, y=100, width=400, height=50)
    lbl2 = tk.Label(fm2, text="NOMBRE Y APELLIDO", font=("Arial", 12))
    lbl2.place(x=90, y=200, width=300, height=20)
    lbl3 = tk.Label(fm2, text="DPI", font=("Arial", 12))
    lbl3.place(x=180, y=300, width=100, height=20)
    lbl4 = tk.Label(fm2, text="CONTRASEÑA", font=("Arial", 12))
    lbl4.place(x=150, y=400, width=150, height=20)
    lbl5 = tk.Label(fm2, text="CONFIRMACIÓN DE CONTRASEÑA", font=("Arial", 12))
    lbl5.place(x=90, y=500, width=300, height=20)


    lbl6 = tk.Label(fm3, text="CREAR NUEVOS CURSOS", fg="white", bg='black', font=("Arial", 14))
    lbl6.place(x=30, y=100, width=400, height=50)
    lbl7 = tk.Label(fm3, text="Nombre del curso", fg="black", font=("Arial", 12))
    lbl7.place(x=30, y=170, width=400, height=30)
    lbl8 = tk.Label(fm3, text="Asignar costo", fg="black", font=("Arial", 12))
    lbl8.place(x=30, y=270, width=400, height=30)
    lbl9 = tk.Label(fm3, text="Asignar horario", fg="black", font=("Arial", 12))
    lbl9.place(x=30, y=370, width=400, height=30)
    lbl10 = tk.Label(fm3, text="Asignar código", fg="black", font=("Arial", 12))
    lbl10.place(x=30, y=470, width=400, height=30)
    lbl11 = tk.Label(fm3, text="Asignar cupo", fg="black", font=("Arial", 12))
    lbl11.place(x=30, y=570, width=400, height=30)
    lbl12 = tk.Label(fm3, text="Asignar catedrático", fg="black", font=("Arial", 12))
    lbl12.place(x=30, y=670, width=400, height=30)
    

    lbl13 = tk.Label(fm4, text="CATEDRÁTICOS REGISTRADOS", fg="white", bg="black", font=("Arial", 14))
    lbl13.place(x=30, y=100, width=400, height=50)
    lbl14 = tk.Label(fm4, text="Y SUS CURSOS ASIGNADOS", fg="white", bg="black", font=("Arial", 14))
    lbl14.place(x=30, y=150, width=400, height=50)
    lbl15 = tk.Label(fm4, text="Eliminar curso:", fg="black", bg="#BDBDBD", font=("Arial", 14))
    lbl15.place(x=10, y=750, width=125, height=30)


    lbl16 = tk.Label(fm5, text="NOTAS DE LOS CURSOS", fg="white", bg="black", font=("Arial", 14))
    lbl16.place(x=30, y=100, width=400, height=50)
    lbl17 = tk.Label(fm5, text="Escriba el nombre del curso", fg="Black", font=("Arial", 12))
    lbl17.place(x=125, y=160, width=200, height=30)


    #Acción de almacenar los datos
    def EnviarDatosCat():
        Nombrecat_dato = txt10.get()
        #Apellidocat_dato = txt11.get()
        DPIcat_dato = txt12.get()
        Contraseñacat_dato = str(txt13.get())
        Confirmacioncontraseñacat_dato = str(txt14.get())
            

        #Verificar que los campos tengan datos a registrar
        if not Nombrecat_dato or not DPIcat_dato or not Contraseñacat_dato or not Confirmacioncontraseñacat_dato:
            messagebox.showinfo("DATOS INCOMPLETOS", "Ingrese su usuario y contraseña")
            return

        # Detectar que la contraseña y la confirmación de contraseña sean iguales
        if Contraseñacat_dato != Confirmacioncontraseñacat_dato:
            messagebox.showinfo("ERROR", "La contraseña y su confirmación no son iguales")
            return

        if not re.search(r'[A-Z]', Contraseñacat_dato) or \
            not re.search(r'\d', Contraseñacat_dato) or \
            not re.search(r'[!@#$%^&*(),.?":{}|<>]', Contraseñacat_dato) or \
            len(Contraseñacat_dato) < 8:
            messagebox.showinfo("ERROR", "La contraseña debe contener; 8 caracteres, 1 mayuscula, 1 digito y 1 simbolo")
            return

        #Encriptar la contraseña antes de almacenarla en el archivo txt
        contracodificada = hashlib.sha256(Contraseñacat_dato.encode()).hexdigest()

        #Guardar Información en archivo de texto
        newfile = open("DatosUsuarios.txt", "a")
        newfile.write(Nombrecat_dato)
        newfile.write(",")
        newfile.write(DPIcat_dato)
        newfile.write(",")
        newfile.write(contracodificada)
        newfile.write(",")
        newfile.write("Catedratico")
        newfile.write("\n")
        newfile.close()

        #Guardar Usuario y contraseña para ingresar
        newfile = open("UsuariosReg.txt", "a")
        newfile.write(DPIcat_dato)
        newfile.write(",")
        newfile.write(Contraseñacat_dato)
        newfile.write(",")
        newfile.write("Catedratico")
        newfile.write("\n")
        newfile.close()

        #Vaciar el contenido de las cajas de texto
        txt10.delete(0, END)
        txt12.delete(0, END)
        txt13.delete(0, END)
        txt14.delete(0, END)

    txt10 = tk.Entry(fm2, bg="white")#Nombre
    txt10.config(font=('Arial',10),justify=tk.CENTER)
    txt10.place(x=140, y=250, width=175, height = 35)
    txt12 = tk.Entry(fm2, bg="white")#DPI
    txt12.config(font=('Arial',10),justify=tk.CENTER)
    txt12.place(x=140, y=350, width=175, height = 35)
    txt13 = tk.Entry(fm2, bg="white", show="*")#Contraseña
    txt13.config(font=("Arial",10),justify=tk.CENTER)
    txt13.place(x=140, y=450, width=175, height = 35)
    txt14 = tk.Entry(fm2, bg="white", show="*")#Confirmar contraseña
    txt14.config(font=("Arial",10),justify=tk.CENTER)
    txt14.place(x=140, y=550, width=175, height = 35)

    btn1 = tk.Button(fm2, text="CONFIRMAR", bg = "black", fg = "white", command=EnviarDatosCat) #BOTÓN CONFIRMAR
    btn1.place(x=145, y=650, width=175, height = 30 )


    #Función para crear el archivo de texto con el nombre del curso
    def Crearcurso():
        NombreCurso_dato = txt15.get()
        Costocurso_dato = txt16.get()
        Horariocurso_dato = txt17.get()
        Codigocurso_dato = txt18.get()
        Cupocurso_dato = txt19.get()
        Catedraticocurso_dato = txt20.get()

        #Verificar que los campos tengan datos a registrar
        if not NombreCurso_dato or not Costocurso_dato or not Horariocurso_dato or not Codigocurso_dato or not Cupocurso_dato or not Catedraticocurso_dato:
            messagebox.showinfo("DATOS INCOMPLETOS", "Ingrese todos los datos")
            return

        # Detectar que que el catedrático este incluido en la base de datos
        if catedraticoExistente(Catedraticocurso_dato):
            messagebox.showinfo("ERROR", "El catedrático no esta registrado")
            return


        with open(NombreCurso_dato + ".txt", 'w') as archivo:
            pass
                
        #Guardar Información en archivo de texto
        newfile = open(NombreCurso_dato + ".txt", "a")
        newfile.write(NombreCurso_dato)
        newfile.write(",")
        newfile.write(Costocurso_dato)
        newfile.write(",")
        newfile.write(Horariocurso_dato)
        newfile.write(",")
        newfile.write(Codigocurso_dato)
        newfile.write(",")
        newfile.write(Cupocurso_dato)
        newfile.write(",")
        newfile.write(Catedraticocurso_dato)
        newfile.write("\n")
        newfile.close()

        #Guardar Información de cursos creados
        newfile = open("CursosExistentes.txt", "a")
        newfile.write(NombreCurso_dato)
        newfile.write("\n")
        newfile.close()

        #Guardar Información de cursos y sus catedraticos
        newfile = open("CursosCatedraticos.txt", "a")
        newfile.write(NombreCurso_dato)
        newfile.write(",")
        newfile.write(Catedraticocurso_dato)
        newfile.write("\n")
        newfile.close()


        #Vaciar el contenido de las cajas de texto
        txt15.delete(0, END)
        txt16.delete(0, END)
        txt17.delete(0, END)
        txt18.delete(0, END)
        txt19.delete(0, END)
        txt20.delete(0, END)


        
    #Funcion para poner la ventana donde se editaran los datos de los cursos existentes
    def ventanaDatosCursos():
        VentanaEditarCursos = tk.Toplevel()
        VentanaEditarCursos.title("EDITAR DATOS DE LOS CURSOS")
        VentanaEditarCursos.geometry("500x800")

        def Vercurso():
            NombreCurso_dato1 = txt1.get()
            with open(NombreCurso_dato1 + ".txt", "r") as archivo:
                contenido = archivo.readline().strip()
                txt1a.delete(1.0, tk.END)  # Borra cualquier contenido previo
                txt1a.insert(tk.END, contenido)

        def EditarCosto():
            NombreCurso_dato1 = txt1.get()
            Costocurso_dato1 = txt2.get()
            with open(NombreCurso_dato1 + ".txt", "r") as archivo:
                lineas = archivo.readlines() # Leer todas las líneas del archivo

 
            Linea = lineas[0].strip() # Modificar la primera línea
            datos = Linea.split(",")
            datos[1] = Costocurso_dato1
            lineas[0] = ",".join(datos) + "\n"

            # Escribir todas las líneas, incluida la primera modificada
            with open(NombreCurso_dato1 + ".txt", "w") as archivo:
                archivo.writelines(lineas)

            txt2.delete(0, tk.END)

        def EditarHorario():
            Horariocurso_dato1= txt3.get()
            NombreCurso_dato1 = txt1.get()
            with open(NombreCurso_dato1 + ".txt", "r") as archivo:
                lineas = archivo.readlines() # Leer todas las líneas del archivo

 
            Linea = lineas[0].strip() # Modificar la primera línea
            datos = Linea.split(",")
            datos[2] = Horariocurso_dato1
            lineas[0] = ",".join(datos) + "\n"

            # Escribir todas las líneas, incluida la primera modificada
            with open(NombreCurso_dato1 + ".txt", "w") as archivo:
                archivo.writelines(lineas)

            txt3.delete(0, tk.END)

        def EditarCodigo():
            Codigocurso_dato1 = txt4.get()
            NombreCurso_dato1 = txt1.get()
            with open(NombreCurso_dato1 + ".txt", "r") as archivo:
                lineas = archivo.readlines() # Leer todas las líneas del archivo

 
            Linea = lineas[0].strip() # Modificar la primera línea
            datos = Linea.split(",")
            datos[3] = Codigocurso_dato1
            lineas[0] = ",".join(datos) + "\n"

            # Escribir todas las líneas, incluida la primera modificada
            with open(NombreCurso_dato1 + ".txt", "w") as archivo:
                archivo.writelines(lineas)

            txt4.delete(0, tk.END)

        def EditarCupo():
            Cupocurso_dato1 = txt5.get()
            NombreCurso_dato1 = txt1.get()
            with open(NombreCurso_dato1 + ".txt", "r") as archivo:
                lineas = archivo.readlines() # Leer todas las líneas del archivo

 
            Linea = lineas[0].strip() # Modificar la primera línea
            datos = Linea.split(",")
            datos[4] = Cupocurso_dato1
            lineas[0] = ','.join(datos) + '\n'

            # Escribir todas las líneas, incluida la primera modificada
            with open(NombreCurso_dato1 + ".txt", "w") as archivo:
                archivo.writelines(lineas)

            txt5.delete(0, tk.END)

        def EditarCat():
            Catedraticocurso_dato1 = txt6.get()
            NombreCurso_dato1 = txt1.get()

            # Detectar que que el catedrático este incluido en la base de datos
            if catedraticoExistente(Catedraticocurso_dato1):
                messagebox.showinfo("ERROR", "El catedrático no esta registrado")
                return

            with open(NombreCurso_dato1 + ".txt", "r") as archivo:
                lineas = archivo.readlines() # Leer todas las líneas del archivo

 
            Linea = lineas[0].strip() # Modificar la primera línea
            datos = Linea.split(",")
            datos[5] = Catedraticocurso_dato1
            lineas[0] = ",".join(datos) + "\n"

            # Escribir todas las líneas, incluida la primera modificada
            with open(NombreCurso_dato1 + ".txt", "w") as archivo:
                archivo.writelines(lineas)

            txt6.delete(0, tk.END)

        #Etiquetas
        lbl1 = Label(VentanaEditarCursos, text="Escriba el nombre del curso correctamente", fg ="black")
        lbl1.config(font=("Arial",10))
        lbl1.place(x=130, y=50, width=250, height = 35)
        lbl2 = Label(VentanaEditarCursos, text="Datos actuales", fg ="black")
        lbl2.place(x=160, y=150, width=175, height = 35)
        lbl3 = Label(VentanaEditarCursos, text="Nuevo Costo", fg ="black")
        lbl3.place(x=160, y=250, width=175, height = 35)
        lbl4 = Label(VentanaEditarCursos, text="Nuevo Horario", fg ="black")
        lbl4.place(x=160, y=350, width=175, height = 35)
        lbl5 = Label(VentanaEditarCursos, text="Nuevo código", fg ="black")
        lbl5.place(x=160, y=450, width=175, height = 35)
        lbl6 = Label(VentanaEditarCursos, text="Nuevo cupo", fg ="black")
        lbl6.place(x=160, y=550, width=175, height = 35)
        lbl7 = Label(VentanaEditarCursos, text="Nuevo catedrático", fg ="black")
        lbl7.place(x=160, y=650, width=175, height = 35)

        txt1a = Text(VentanaEditarCursos, bg="White")
        txt1a.config(font=('Arial',14))
        txt1a.place(x=70, y=180, width=350, height = 70)

        #Entrada de los datos
        txt1 = Entry(VentanaEditarCursos, bg="White")#Nombre del curso
        txt1.config(font=("Arial",10),justify=tk.CENTER)
        txt1.place(x=70, y=100, width=175, height = 35)
        txt2 = Entry(VentanaEditarCursos, bg="White")#Costo del curso
        txt2.config(font=("Arial",10),justify=tk.CENTER)
        txt2.place(x=70, y=300, width=175, height = 35)
        txt3 = Entry(VentanaEditarCursos, bg="White")#Horario del curso
        txt3.config(font=("Arial",10),justify=tk.CENTER)
        txt3.place(x=70, y=400, width=175, height = 35)
        txt4 = Entry(VentanaEditarCursos, bg="White")#Código del curso
        txt4.config(font=("Arial",10),justify=tk.CENTER)
        txt4.place(x=70, y=500, width=175, height = 35)
        txt5 = Entry(VentanaEditarCursos, bg="White")#Cupo del curso
        txt5.config(font=("Arial",10),justify=tk.CENTER)
        txt5.place(x=70, y=600, width=175, height = 35)
        txt6 = Entry(VentanaEditarCursos, bg="White")#Catedrático del curso
        txt6.config(font=("Arial",10),justify=tk.CENTER)
        txt6.place(x=70, y=700, width=175, height = 35)

        btn1 = Button(VentanaEditarCursos, text="CONFIRMAR", bg = "black", fg = "white", command=Vercurso) #BOTÓN CONFIRMAR
        btn1.place(x=250, y=100, width=175, height = 30 )
        btn2 = Button(VentanaEditarCursos, text="Editar", bg = "black", fg = "white", command=EditarCosto) #BOTÓN CONFIRMAR
        btn2.place(x=250, y=300, width=175, height = 30 )
        btn3 = Button(VentanaEditarCursos, text="Editar", bg = "black", fg = "white", command=EditarHorario) #BOTÓN CONFIRMAR
        btn3.place(x=250, y=400, width=175, height = 30 )
        btn4 = Button(VentanaEditarCursos, text="Editar", bg = "black", fg = "white", command=EditarCodigo) #BOTÓN CONFIRMAR
        btn4.place(x=250, y=500, width=175, height = 30 )
        btn5 = Button(VentanaEditarCursos, text="Editar", bg = "black", fg = "white", command=EditarCupo) #BOTÓN CONFIRMAR
        btn5.place(x=250, y=600, width=175, height = 30 )
        btn6 = Button(VentanaEditarCursos, text="Editar", bg = "black", fg = "white", command=EditarCat) #BOTÓN CONFIRMAR
        btn6.place(x=250, y=700, width=175, height = 30 )



    #Funciones y botones para la creación de cursos
    txt15 = tk.Entry(fm3)#Nombre del curso
    txt15.config(font=("Arial",10),justify=tk.CENTER)
    txt15.place(x=140, y=220, width=175, height = 35)
    txt16 = tk.Entry(fm3)#Costo del curso
    txt16.config(font=("Arial",10),justify=tk.CENTER)
    txt16.place(x=140, y=320, width=175, height = 35)
    txt17 = tk.Entry(fm3)#Horario del curso
    txt17.config(font=("Arial",10),justify=tk.CENTER)
    txt17.place(x=140, y=420, width=175, height = 35)
    txt18 = tk.Entry(fm3)#Código del curso
    txt18.config(font=("Arial",10),justify=tk.CENTER)
    txt18.place(x=140, y=520, width=175, height = 35)
    txt19 = tk.Entry(fm3)#Cupo del curso
    txt19.config(font=("Arial",10),justify=tk.CENTER)
    txt19.place(x=140, y=620, width=175, height = 35)
    txt20 = tk.Entry(fm3)#Catedrático del curso
    txt20.config(font=("Arial",10),justify=tk.CENTER)
    txt20.place(x=140, y=720, width=175, height = 35)
    btn2 = tk.Button(fm3, text="CONFIRMAR", bg = "black", fg = "white", command=Crearcurso) #BOTÓN CONFIRMAR
    btn2.place(x=260, y=775, width=175, height = 30 )
    btn2b = tk.Button(fm3, text="Editar Curso", bg = "black", fg = "white", command=ventanaDatosCursos) #BOTÓN CONFIRMAR
    btn2b.place(x=50, y=775, width=175, height = 30 )


    # Función para imprimir los datos de los cursos en el cuadro
    def Vercursos():
        with open("CursosCatedraticos.txt", "r") as archivo:
            contenido = archivo.read()
            txt21.delete(1.0, tk.END)  # Borra cualquier contenido previo
            txt21.insert(tk.END, contenido)

    #Función para limpiar la caja
    def Limpiarcaja():
        txt21.delete(1.0, tk.END)

    # Función para borrar el archivo txt del curso y texto relacionado en otros txt
    def Eliminarcurso():
        Cursoeliminar_dato = txt20b.get()

        nombrecurso = os.path.join(Cursoeliminar_dato + ".txt")
        if os.path.exists(nombrecurso):
            os.remove(nombrecurso)
        else: 
            messagebox.showinfo("ERROR", "Nombre del curso no encontrado")

        with open("CursosCatedraticos.txt", "r+") as archivo:
            lineas = archivo.readlines() # Leer todas las líneas del archivo

            # ver todas las líneas y escribir las lineas sin el curso eliminado
            for linea in lineas:
                # Obtener el nombre registrado del curso
                nombrecurso = linea.split(",")[0].strip()

                # Ver si el nombre del curso es igual al que se desea eliminar
                if nombrecurso != Cursoeliminar_dato:

                    # Escribir todas las líneas, menos el curso eliminado
                    with open("CursosCatedraticos.txt", "w") as archivo:
                        archivo.writelines(linea)
                

        with open("CursosExistentes.txt", "r+") as archivo:
            lineas = archivo.readlines() # Leer todas las líneas del archivo

            # ver todas las líneas y escribir las lineas sin el curso eliminado
            for linea in lineas:
                # Obtener el nombre registrado del curso
                nombrecurso = linea.strip()

                # Ver si el nombre del curso es igual al que se desea eliminar
                if nombrecurso != Cursoeliminar_dato:
                    
                    # Escribir todas las líneas, menos el curso eliminado
                    with open("CursosExistentes.txt", "w") as archivo:
                        archivo.writelines(linea)

        #Limpiar en entry una vez hecho todo
        txt20b.delete(0, tk.END)
        #Mensaje de error su no esta en archivo o curso
        messagebox.showinfo("HECHO", "El curso ha sido eliminado correctamente")

    # botones y caja de texto 
    txt21 = tk.Text(fm4, bg="White")
    txt21.config(font=("Arial",14))
    txt21.pack(fill=tk.BOTH, expand=True, padx=(10, 10), pady=(250, 175))
    btn3 = tk.Button(fm4, text="Ver cursos y catedráticos", bg = "black", fg = "white", command=Vercursos) #BOTÓN ver datos de cursos
    btn3.config(font=("Arial",12))
    btn3.place(x=30, y=700, width=225, height = 30 )
    btn4 = tk.Button(fm4, text="Limpiar contenido", bg = "black", fg = "white", command=Limpiarcaja) #BOTÓN para limpiar la caja de texto
    btn4.config(font=("Arial",12))
    btn4.place(x=270, y=700, width=175, height = 30 )

    txt20b = tk.Entry(fm4)#Ingresar el nombre del curso a eliminar
    txt20b.config(font=("Arial",10),justify=tk.CENTER)
    txt20b.place(x=150, y=750, width=150, height = 30)
    btn4b = tk.Button(fm4, text='Eliminar', bg = "black", fg = "white", command=Eliminarcurso) #BOTÓN para eliminar curso existente
    btn4b.config(font=("Arial",12))
    btn4b.place(x=320, y=750, width=130, height = 30 )


    # Función para buscar el curso y mostrar las notas
    def Buscarcurso():
        NombreCurso_dato2 = txt23.get()

        with open(NombreCurso_dato2 + ".txt", "r") as archivo:
            contenido = archivo.read()
            txt22.delete(1.0, tk.END)  # Borra cualquier contenido previo
            txt22.insert(tk.END, contenido)

    # Función para limpiar la caja de texto
    def Limpiarcaja():
        txt22.delete(1.0, tk.END)

    # Caja de texto para mostrar resultados
    txt22 = tk.Text(fm5, bg="White")
    txt22.config(font=("Arial", 14))
    txt22.pack(fill=tk.BOTH, expand=True, padx=(10, 10), pady=(300, 300))

    # Entrada y botones
    txt23 = tk.Entry(fm5, bg="white")
    txt23.config(font=("Arial", 10), justify=tk.CENTER)
    txt23.place(x=140, y=200, width=175, height=35)
    btn5 = tk.Button(fm5, text="CONFIRMAR", bg="black", fg="white", command=Buscarcurso)
    btn5.config(font=("Arial", 12))
    btn5.place(x=140, y=250, width=175, height=30)
    btn6 = tk.Button(fm5, text="Limpiar contenido", bg="black", fg="white", command=Limpiarcaja)
    btn6.config(font=("Arial", 12))
    btn6.place(x=140, y=600, width=175, height=30)


#Abrir la ventana con vista de catedratico
def ventanacat():
    root = tk.Tk()
    root.state("zoomed")  # Maximizar la ventana en Windows
    root.grid_rowconfigure(0, weight=1, uniform="rows_g1")
    root.grid_rowconfigure(1, weight=5, uniform="rows_g1")
    root.grid_columnconfigure(0, weight=1, uniform="columnag1")
    root.grid_columnconfigure(1, weight=1, uniform="columnag1")
    root.grid_columnconfigure(2, weight=1, uniform="columnag1")

    fm0 = tk.Frame(root, bg="blue")
    fm0.grid(row=0, column=0, columnspan=3, sticky="nsew")

    fm1 = tk.Frame(root, bg="#9AB9BA")
    fm1.grid(row=1, column=0, sticky="nsew")

    fm2 = tk.Frame(root)
    fm2.grid(row=1, column=1, sticky="nsew")

    fm3 = tk.Frame(root, bg="#9AB9BA")
    fm3.grid(row=1, column=2, sticky="nsew")

    btncerrar1 = Button(fm0, text="Cerrar Sesión", bg = "black", fg = "white", command=root.destroy) #BOTÓN CERRAR VENTANA #BOTÓN CONFIRMAR
    btncerrar1.place(x=20, y=20, width=175, height = 30 )

    def Vercurso():
        NombreCurso_dato1 = txt1.get()
        with open(NombreCurso_dato1 + ".txt", "r") as archivo:
            contenido = archivo.readline().strip()
            txt1a.delete(1.0, tk.END)  # Borra cualquier contenido previo
            txt1a.insert(tk.END, contenido)

    def EditarCosto():
        NombreCurso_dato1 = txt1.get()
        Costocurso_dato1 = txt2.get()
        with open(NombreCurso_dato1 + ".txt", "r") as archivo:
            lineas = archivo.readlines() # Leer todas las líneas del archivo


        Linea = lineas[0].strip() # Modificar la primera línea
        datos = Linea.split(",")
        datos[1] = Costocurso_dato1
        lineas[0] = ",".join(datos) + "\n"

        # Escribir todas las líneas, incluida la primera modificada
        with open(NombreCurso_dato1 + ".txt", "w") as archivo:
            archivo.writelines(lineas)

        txt2.delete(0, tk.END)

    def EditarHorario():
        Horariocurso_dato1= txt3.get()
        NombreCurso_dato1 = txt1.get()
        with open(NombreCurso_dato1 + ".txt", "r") as archivo:
            lineas = archivo.readlines() # Leer todas las líneas del archivo


        Linea = lineas[0].strip() # Modificar la primera línea
        datos = Linea.split(",")
        datos[2] = Horariocurso_dato1
        lineas[0] = ",".join(datos) + "\n"

        # Escribir todas las líneas, incluida la primera modificada
        with open(NombreCurso_dato1 + ".txt", "w") as archivo:
            archivo.writelines(lineas)

        txt3.delete(0, tk.END)

    def EditarCodigo():
        Codigocurso_dato1 = txt4.get()
        NombreCurso_dato1 = txt1.get()
        with open(NombreCurso_dato1 + ".txt", "r") as archivo:
            lineas = archivo.readlines() # Leer todas las líneas del archivo


        Linea = lineas[0].strip() # Modificar la primera línea
        datos = Linea.split(",")
        datos[3] = Codigocurso_dato1
        lineas[0] = ",".join(datos) + "\n"

        # Escribir todas las líneas, incluida la primera modificada
        with open(NombreCurso_dato1 + ".txt", "w") as archivo:
            archivo.writelines(lineas)

        txt4.delete(0, tk.END)

    def EditarCupo():
        Cupocurso_dato1 = txt5.get()
        NombreCurso_dato1 = txt1.get()
        with open(NombreCurso_dato1 + ".txt", "r") as archivo:
            lineas = archivo.readlines() # Leer todas las líneas del archivo


        Linea = lineas[0].strip() # Modificar la primera línea
        datos = Linea.split(",")
        datos[4] = Cupocurso_dato1
        lineas[0] = ",".join(datos) + "\n"

        # Escribir todas las líneas, incluida la primera modificada
        with open(NombreCurso_dato1 + ".txt", "w") as archivo:
            archivo.writelines(lineas)

        txt5.delete(0, tk.END)

    # Función para mostrar los cursos de un catedratico en especifico
    def MisCursos():

        with open("DatosUsuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) <= 5 and USER_dato == datos[1]:
                    Nombrecate = datos[0] 
        print(Nombrecate)

        with open("CursosCatedraticos.txt", "r") as archivo:
            for linea in archivo:
                datos2 = linea.strip().split(",")
                if "Alexander Perez" == datos2[1]:
                    cursoscate = datos2[0] 
        print(cursoscate)



    #traer el nombre del usuario para presentarlo
    USER_dato = USER.get()
    with open("DatosUsuarios.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) <= 5 and USER_dato == datos[1]:
                Nombre = datos[0] 
    #Etiquetas
    lbl0 = tk.Label(fm0, text="Catedratico: " + Nombre, fg ="black", bg="blue")
    lbl0.config(font=("Arial",30))
    lbl0.place(x=620, y=50, width=700, height = 35)
    lbl1 = tk.Label(fm1, text="Escriba el nombre del curso correctamente", fg ="black", bg="#9AB9BA")
    lbl1.config(font=("Arial",10))
    lbl1.place(x=190, y=200, width=250, height = 35)
    lbl2 = tk.Label(fm1, text="Datos actuales", fg ="black", bg="#9AB9BA")
    lbl2.place(x=220, y=300, width=175, height = 35)
    lbl3 = tk.Label(fm1, text="Nuevo Costo", fg ="black", bg="#9AB9BA")
    lbl3.place(x=220, y=430, width=175, height = 35)
    lbl4 = tk.Label(fm1, text="Nuevo Horario", fg ="black", bg="#9AB9BA")
    lbl4.place(x=220, y=530, width=175, height = 35)
    lbl5 = tk.Label(fm1, text="Nuevo código", fg ="black", bg="#9AB9BA")
    lbl5.place(x=220, y=630, width=175, height = 35)
    lbl6 = tk.Label(fm1, text="Nuevo cupo", fg ="black", bg="#9AB9BA")
    lbl6.place(x=220, y=730, width=175, height = 35)

    #Parte para ver lso cursos asignados del catedratico
    lbl7 = tk.Label(fm1, text="Mis cursos", fg ="black", bg="#9AB9BA")
    lbl7.config(font=("Arial",14))
    lbl7.place(x=220, y=25, width=175, height = 35)
    txt2b = Text(fm1, bg="White") #Cuadro para mostrar cursos especificos
    txt2b.config(font=("Arial",14))
    txt2b.place(x=50, y=100, width=350, height = 70)
    btn6 = tk.Button(fm1, text="Ver", bg = "black", fg = "white", command=MisCursos) #BOTÓN CONFIRMAR
    btn6.place(x=420, y=100, width=175, height = 70 )

    #Caja de texto para ver datos de curso
    txt1a = Text(fm1, bg="White")
    txt1a.config(font=("Arial",14))
    txt1a.place(x=50, y=350, width=550, height = 70)

    #Entrada de los datos
    txt1 = tk.Entry(fm1, bg="white")#Nombre del curso
    txt1.config(font=("Arial",10),justify=tk.CENTER)
    txt1.place(x=130, y=250, width=175, height = 35)
    txt2 = tk.Entry(fm1, bg="white")#Costo del curso
    txt2.config(font=("Arial",10),justify=tk.CENTER)
    txt2.place(x=130, y=480, width=175, height = 35)
    txt3 = tk.Entry(fm1, bg="white")#Horario del curso
    txt3.config(font=("Arial",10),justify=tk.CENTER)
    txt3.place(x=130, y=580, width=175, height = 35)
    txt4 = tk.Entry(fm1, bg="white")#Código del curso
    txt4.config(font=("Arial",10),justify=tk.CENTER)
    txt4.place(x=130, y=680, width=175, height = 35)
    txt5 = tk.Entry(fm1, bg="white")#Cupo del curso
    txt5.config(font=("Arial",10),justify=tk.CENTER)
    txt5.place(x=130, y=780, width=175, height = 35)


    btn1 = tk.Button(fm1, text="CONFIRMAR", bg = "black", fg = "white", command=Vercurso) #BOTÓN CONFIRMAR
    btn1.place(x=310, y=250, width=175, height = 30 )
    btn2 = tk.Button(fm1, text="Editar", bg = "black", fg = "white", command=EditarCosto) #BOTÓN CONFIRMAR
    btn2.place(x=310, y=480, width=175, height = 30 )
    btn3 = tk.Button(fm1, text="Editar", bg = "black", fg = "white", command=EditarHorario) #BOTÓN CONFIRMAR
    btn3.place(x=310, y=580, width=175, height = 30 )
    btn4 = tk.Button(fm1, text="Editar", bg = "black", fg = "white", command=EditarCodigo) #BOTÓN CONFIRMAR
    btn4.place(x=310, y=680, width=175, height = 30 )
    btn5 = tk.Button(fm1, text="Editar", bg = "black", fg = "white", command=EditarCupo) #BOTÓN CONFIRMAR
    btn5.place(x=310, y=780, width=175, height = 30 )



    lbl18 = tk.Label(fm3, text="NOTAS DE LOS CURSOS", fg="white", bg="black", font=("Arial", 14))
    lbl18.place(x=120, y=50, width=400, height=50)
    lbl19 = tk.Label(fm3, text="Escriba el nombre del curso", fg="black", bg="#9AB9BA", font=("Arial", 12))
    lbl19.place(x=210, y=110, width=200, height=30)
    lbl20 = tk.Label(fm3, text="Editar / Introducir notas", fg="black", bg="#9AB9BA", font=("Arial", 12))
    lbl20.place(x=210, y=600, width=200, height=30)
    lbl21 = tk.Label(fm3, text="Usuario del estudiante", fg="black", bg="#9AB9BA", font=("Arial", 12))
    lbl21.place(x=25, y=650, width=180, height=30)
    lbl22 = tk.Label(fm3, text="Asignar nota", fg="black", bg="#9AB9BA", font=("Arial", 12))
    lbl22.place(x=30, y=700, width=100, height=30)



    def Editarnota():
        editarnota_dato = txt25.get()
        estudianteusuario_dato = txt24.get()
        NombreCurso_dato1 = txt23.get()

        with open(NombreCurso_dato1 + ".txt", "r") as archivo:
            lineas = archivo.readlines() # Leer todas las líneas del archivo
            
            for i in range(len(lineas)):
                Linea = lineas[i].strip() # Modificar la primera línea
                dato = Linea.split(",")
                if dato[2] == estudianteusuario_dato:
                    dato[3] = editarnota_dato
                    lineas[i] = ",".join(dato) + "\n"

        # Escribir todas las líneas, incluida la primera modificada
        with open(NombreCurso_dato1 + ".txt", "w") as archivo:
            archivo.writelines(lineas)

        txt24.delete(0, END)
        txt25.delete(0, END)

 

    # Función para buscar el curso y mostrar las notas
    def Buscarcurso():
        NombreCurso_dato2 = txt23.get()

        with open(NombreCurso_dato2 + ".txt", "r") as archivo:
            contenido = archivo.read()
            txt22.delete(1.0, tk.END)  # Borra cualquier contenido previo
            txt22.insert(tk.END, contenido)

    # Función para limpiar la caja de texto
    def Limpiarcaja():
        txt22.delete(1.0, tk.END)

    # Caja de texto para mostrar resultados
    txt22 = tk.Text(fm3, bg="White")
    txt22.config(font=("Arial", 14))
    txt22.pack(fill=tk.BOTH, expand=True, padx=(10, 10), pady=(250, 350))

    # Entrada y botones
    txt23 = tk.Entry(fm3, bg="white")
    txt23.config(font=("Arial", 10), justify=tk.CENTER)
    txt23.place(x=220, y=150, width=175, height=35)
    btn6 = tk.Button(fm3, text="CONFIRMAR O ACTUALIZAR", bg="black", fg="white", command=Buscarcurso)
    btn6.config(font=("Arial", 12))
    btn6.place(x=190, y=200, width=250, height=30)
    btn7 = tk.Button(fm3, text="Limpiar contenido", bg="black", fg="white", command=Limpiarcaja)
    btn7.config(font=('Arial', 12))
    btn7.place(x=220, y=550, width=175, height=30)

    txt24 = tk.Entry(fm3, bg="white") # Usuario del estudiante
    txt24.config(font=("Arial", 10), justify=tk.CENTER)
    txt24.place(x=220, y=650, width=175, height=35)
    txt25 = tk.Entry(fm3, bg="white") # Futura nota del estudiante
    txt25.config(font=("Arial", 10), justify=tk.CENTER)
    txt25.place(x=220, y=700, width=175, height=35)
    btn8 = tk.Button(fm3, text="Editar", bg="black", fg="white", command=Editarnota)
    btn8.config(font=("Arial", 12))
    btn8.place(x=450, y=650, width=100, height=50)





#Abrir la ventana con vista de estudiante
def ventanaest():

    root = tk.Tk()
    root.state("zoomed") 
    root.title("Ventana con Grid y Frames")

    # Configurar las filas y columnas
    root.columnconfigure(0, weight=2)  
    root.columnconfigure(1, weight=1)  
    root.rowconfigure(0, weight=1)     
    root.rowconfigure(1, weight=4)   
    root.rowconfigure(2, weight=1)     

    # Crear Frames
    fm0 = tk.Frame(root, bg="blue")
    fm1 = tk.Frame(root, bg="#9AB9BA")
    fm2 = tk.Frame(root, bg="#86C6C8")
    fm3 = tk.Frame(root, bg="#2B5A5B")
    # Colocar los Frames en la ventana
    fm0.grid(row=0, column=0, columnspan=2, sticky="nsew") 
    fm1.grid(row=1, column=0, columnspan=1, sticky="nsew")  
    fm2.grid(row=1, column=1, columnspan=1, rowspan=2, sticky="nsew")  
    fm3.grid(row=2, column=0, columnspan=2, sticky="nsew")

    btncerrar3 = Button(fm0, text="Cerrar Sesión", bg = "black", fg = "white", command=root.destroy) #BOTÓN CERRAR VENTANA #BOTÓN CONFIRMAR
    btncerrar3.place(x=20, y=20, width=175, height = 30 )

    USER_dato = USER.get()
    with open("DatosUsuarios.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) >= 6 and USER_dato == datos[5]:
                Nombre = datos[0] + " " + datos[1]
                Nombre2 = datos[0]
        

    lbl1f = tk.Label(fm0, text="ESTUDIANTE: " + Nombre, fg="black", bg="blue", font=("Arial", 26))
    lbl1f.place(x=600, y=60, width=700, height=50)

    lbl2f = tk.Label(fm1, text="Cursos", fg="black", bg="#9AB9BA", font=("Arial", 16))
    lbl2f.place(x=450, y=30, width=200, height=50)

    lbl3f = tk.Label(fm2, text="Asignar cursos", fg="black", bg="#86C6C8", font=("Arial", 16))
    lbl3f.place(x=230, y=30, width=200, height=50)

    lbl4f = tk.Label(fm3, text="Cursos aprobados", fg="black", bg="#2B5A5B", font=("Arial", 16))
    lbl4f.place(x=30, y=30, width=200, height=50)
    
    # CONTENIDO PARA EJEMPLIFICAR LA ASIGNACIÓN A UNA CLASE (SIN AUTOMATIZAR NINGUN PROCESO)
    
    def asignarcurso():


        with open("DatosUsuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) >= 6 and USER_dato == datos[5]:
                    DatosEstu = datos[0] + "," + datos[5] + "," + "100"


        with open("CursoPrueba1.txt", "r") as archivo:
            lineas = archivo.readlines()
            ultimalinea = lineas[-1]
            datos = ultimalinea.strip().split(",")
            cupoest = int(datos[4]) - 1
        asignacion = DatosEstu + "," + str(cupoest)

        abrirdoc = open("CursoPrueba1.txt", "a")
        abrirdoc.write("\n")
        abrirdoc.write(asignacion)
        abrirdoc.close()

    lbl5f = tk.Label(fm2, text="CursoPrueba1", fg="black", bg="white", font=("Arial", 12))
    lbl5f.place(x=230, y=100, width=200, height=50)
    btn1b = tk.Button(fm2, text="Asignar", bg = "black", fg = "white", command=asignarcurso)#BOTÓN asignar curso
    btn1b.place(x=230, y=200, width=175, height = 50)





#Buscar coincidencia de usuario en la base de datos
def confirmaruser():
    USER_dato = USER.get()
    CONT_dato = CONT.get()

    #Verificar que los campos de usuario y contraseña tengan datos a comprobar
    if not USER_dato or not CONT_dato:
        messagebox.showinfo("DATOS INCOMPLETOS", "Ingrese su usuario y contraseña")
        return

    #Catalogar el inicio de sesión para redireccionar a su respectiva ventana
    with open("UsuariosReg.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if USER_dato == datos[0] and CONT_dato == datos[1]:

                if "Estudiante" in linea:       #Catalogar el usuario de tipo estudiante
                    ventanaest()
                elif "Catedratico" in linea:    #Catalogar el usuario de tipo catedratico
                    ventanacat()
                else:                           #Catalogar el usuario de tipo administrador
                   ventanadmin()
                break
        else:
            messagebox.showinfo("DATOS NO ENCONTRADOS", "Usuario o Contraseña incorrectos")


    #Vaciar el contenido de las cajas de texto
    txt1.delete(0, END)
    txt2.delete(0, END)

#Función que revisará la existencia de un nombre de usuario repetido o existente
def usuarioexistente(usuario):
    with open("UsuariosReg.txt", "r") as archivo:
        for linea in archivo:
            datosuser = linea.strip().split(",") 
            if usuario == datosuser[0]:
                return True
    return False

#Función que revisará la existencia de catedrático para el curso
def catedraticoExistente(catedratico):
    with open("DatosUsuarios.txt", "r") as archivo:
        for linea in archivo:
            datoscat = linea.strip().split(",")
            if catedratico == datoscat[0] and (len(datoscat) >= 4 and datoscat[3].strip() == "Catedratico"):
                return False          
    return True

#Se declaran las variables de tipo string (cadenas de texto)
USER = StringVar()
CONT = StringVar()


#Primera ventana de inicio se sesiones
lbl1 = Label(programa, text="INICIAR SESIÓN", fg ="black") #ETIQUETA
lbl1.config(font=("Arial",16))
lbl1.place(relx=0.25, rely=0.10, relwidth=0.5, relheight = 0.1)
lbl2 = Label(programa, text="USUARIO", fg ="black")
lbl2.config(font=("Arial",10)) 
lbl2.place(relx=0.25, rely=0.20, relwidth=0.5, relheight = 0.1)
lbl3 = Label(programa, text="CONTRASEÑA", fg ="black")
lbl3.config(font=("Arial",10))
lbl3.place(relx=0.25, rely=0.40, relwidth=0.5, relheight = 0.1)
txt1 = Entry(programa, textvariable=USER)
txt1.config(font=("Arial",14),justify=tk.CENTER) 
txt1.place(relx=0.25, rely=0.30, relwidth=0.5, relheight = 0.1)
txt2 = Entry(programa, textvariable=CONT, show="*")
txt2.config(font=("Arial",14),justify=tk.CENTER)
txt2.place(relx=0.25, rely=0.50, relwidth=0.5, relheight = 0.1)
btn1 = Button(programa, text="CONFIRMAR", bg = "black", fg = "white", command=confirmaruser) #BOTÓN CONFIRMAR
btn1.place(relx=0.35, rely=0.65, relwidth=0.3, relheight = 0.08 )

lbl4 = Label(programa, text="REGISTRARSE COMO ESTUDIANTE", fg ="black")#ETIQUETA
lbl4.config(font=('Arial',12))
lbl4.place(relx=0.25, rely=0.75, relwidth=0.5, relheight = 0.05)

btn4 = Button(programa, text="REGISTRARSE", bg = "black", fg = "white", command=ventanaRes)#BOTÓN REGISTRAR ESTUDIANTES
btn4.place(relx=0.35, rely=0.83, relwidth=0.3, relheight = 0.08)



programa.mainloop()