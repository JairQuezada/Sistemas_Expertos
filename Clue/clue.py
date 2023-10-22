import json
import random
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk  

x = 5
y = 0
respuestas_correctas = 0

def inicializar_juego():
    global informacion, informacion2, personajes, personajes2, asesino, locaciones, escena_crimen, armas, arma_homicida, testimonios
    global testimonio1, testimonio2, testimonio3, testimonio4, testimonios, sospechoso, lugar, arma, locaciones2, armas2,final_resultado
    informacion = cargar_base_de_datos('clue_base_de_datos.json')
    informacion2 = cargar_base_de_datos('clue_base_de_datos.json')

    personajes = informacion['evidencia'][0]['personajes']
    asesino = random.choice(list(personajes.keys()))
    informacion["evidencia"][0]["personajes"][asesino] = True

    locaciones = informacion['evidencia'][1]['locaciones']
    escena_crimen = random.choice(list(locaciones.keys()))
    informacion["evidencia"][1]["locaciones"][escena_crimen] = True

    armas = informacion['evidencia'][2]['armas']
    arma_homicida = random.choice(list(armas.keys()))
    informacion["evidencia"][2]["armas"][arma_homicida] = True

    testimonios = {}
    personajes2 = informacion2['evidencia'][0]['personajes']
    locaciones2 = informacion2['evidencia'][1]['locaciones']
    armas2 = informacion2['evidencia'][2]['armas']

    sospechoso = asesino + " no se presentó a hacer testimonio"
    testimonios[asesino] = 5
    lugar = "Nadie recuerda haber estado en " + escena_crimen
    testimonios[escena_crimen] = 6
    arma = "Nadie recuerda haber visto o usado el/la " + arma_homicida
    testimonios[arma_homicida] = 7
    final_resultado=asesino+" es el asesino y uso "+arma_homicida+" en la/el "+escena_crimen

    del informacion2["evidencia"][0]["personajes"][asesino]
    del informacion2["evidencia"][1]["locaciones"][escena_crimen]
    del informacion2["evidencia"][2]["armas"][arma_homicida]

    testimonio1= alazar_borrar_personaje(1)+" estaba en "+alazar_borrar_locacion(1)+" usando "+alazar_borrar_arma(1)
    testimonio2= alazar_borrar_personaje(2)+" estaba en "+alazar_borrar_locacion(2)+" usando "+alazar_borrar_arma(2)
    testimonio3= alazar_borrar_personaje(3)+" estaba en "+alazar_borrar_locacion(3)+" usando "+alazar_borrar_arma(3)
    testimonio4= alazar_borrar_personaje(4)+" estaba en "+alazar_borrar_locacion(4)+" usando "+alazar_borrar_arma(4)

def elegir_testimonio(buscar,tipo):
    global respuestas_correctas
    equivocado="No deduciste correctamente"
    correcto="Deduciste correctamente"
    if tipo == 0:
        if buscar == 1:
            return testimonio1
        if buscar == 2:
            return testimonio2
        if buscar == 3:
            return testimonio3
        if buscar == 4:
            return testimonio4
        if buscar == 5:
            return sospechoso
        if buscar == 6:
            return lugar
        if buscar == 7:
            return arma
    else:
        if buscar in (1,2,3,4):
            return equivocado
        if buscar in (5,6,7):
            respuestas_correctas=respuestas_correctas+1
            return correcto

def cargar_base_de_datos(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data  

def buscar(sospechosos, revisar, tipo):
    if revisar in sospechosos:
        objetivo = revisar
        if objetivo in testimonios:
            print(elegir_testimonio(testimonios[objetivo], tipo))
        y = 1
    else:
        print("\nInsertar un valor válido\n")
        y = 0
    return y

def investigar_personaje():
    def on_sospechoso_select(sospechoso):
        response_label.config(text=elegir_testimonio(testimonios[sospechoso], 0),font=("Univers",11))
        window_pregunta.geometry("800x60")
        center_window2(window_pregunta)
        salir_button.pack()  # Show the "Salir" button
        for button in character_buttons:
            button.pack_forget()  # Hide the character selection buttons

    window_pregunta = tk.Toplevel(window)
    window_pregunta.title("Seleccionar Sospechoso")
    window_pregunta.geometry("250x270")
    window_pregunta.config(background="black")
    center_window2(window_pregunta)

    response_label = tk.Label(window_pregunta, text="",background='black',fg='white')
    response_label.pack()

    sospechosos = list(personajes.keys())
    character_buttons = []

    for sospechoso in sospechosos:
        button = tk.Button(window_pregunta, text=sospechoso, command=lambda s=sospechoso: on_sospechoso_select(s),font=("Star Jedi",11))
        character_buttons.append(button)

    for button in character_buttons:
        button.pack()

    salir_button = tk.Button(window_pregunta, text="Salir", command=window_pregunta.destroy,font=("Star Jedi",12))
    # Initially, hide the "Salir" button
    salir_button.pack_forget()
    
def investigar_locacion():
    def on_locacion_select(locacion):
        response_label.config(text=elegir_testimonio(testimonios[locacion], 0), font=("Univers", 11))
        window_pregunta.geometry("800x60")
        center_window2(window_pregunta)
        salir_button.pack()
        for button in location_buttons:
            button.pack_forget()

    window_pregunta = tk.Toplevel(window)
    window_pregunta.title("Seleccionar Locación")
    window_pregunta.geometry("450x270")
    window_pregunta.config(background="black")
    center_window2(window_pregunta)

    response_label = tk.Label(window_pregunta, text="",background='black',fg='white')
    response_label.pack()

    locacione = list(locaciones.keys())
    location_buttons = []

    for locacion in locacione:
        button = tk.Button(window_pregunta, text=locacion, command=lambda l=locacion: on_locacion_select(l), font=("Star Jedi", 11))
        location_buttons.append(button)

    for button in location_buttons:
        button.pack()

    salir_button = tk.Button(window_pregunta, text="Salir", command=window_pregunta.destroy, font=("Star Jedi", 12))
    salir_button.pack_forget()
     
def investigar_arma():
    def on_arma_select(arma):
        response_label.config(text=elegir_testimonio(testimonios[arma], 0), font=("Univers", 11))
        window_pregunta.geometry("800x60")
        center_window2(window_pregunta)
        salir_button.pack()
        for button in weapon_buttons:
            button.pack_forget()

    window_pregunta = tk.Toplevel(window)
    window_pregunta.title("Seleccionar Arma")
    window_pregunta.geometry("350x270")
    window_pregunta.config(background="black")
    center_window2(window_pregunta)

    response_label = tk.Label(window_pregunta, text="",background='black',fg='white')
    response_label.pack()

    armaa = list(armas.keys()) 
    weapon_buttons = []

    for arma in armaa:
        button = tk.Button(window_pregunta, text=arma, command=lambda a=arma: on_arma_select(a), font=("Star Jedi", 11))
        weapon_buttons.append(button)

    for button in weapon_buttons:
        button.pack()

    salir_button = tk.Button(window_pregunta, text="Salir", command=window_pregunta.destroy, font=("Star Jedi", 12))
    salir_button.pack_forget()   

def alazar_borrar_personaje(numero):
    borrar=random.choice(list(personajes2.keys()))
    del informacion2["evidencia"][0]["personajes"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_locacion(numero):
    borrar=random.choice(list(locaciones2.keys()))
    del informacion2["evidencia"][1]["locaciones"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_arma(numero):
    borrar=random.choice(list(armas2.keys()))
    del informacion2["evidencia"][2]["armas"][borrar]
    testimonios[borrar]=numero
    return borrar

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

def center_window2(window_pregunta):
    window_pregunta.update_idletasks()
    screen_width = window_pregunta.winfo_screenwidth()
    screen_height = window_pregunta.winfo_screenheight()
    window_width = window_pregunta.winfo_width()
    window_height = window_pregunta.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window_pregunta.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

def historia():
    canvas1.destroy()
    window.geometry("1280x720")

    center_window(window)

    canvas2.configure(background="black")
    canvas2.pack()
    def intro():
        canvas2.create_image(0, 0, anchor=tkinter.NW, image=imagen2,)
        canvas2.itemconfig(texto, text= "@",fill='#FFE81F', font=("Star Jedi Hollow", 100))
        canvas2.tag_raise(texto)
        canvas2.tag_lower(imagen2)
        window.after(4000, history)
    
    def history():
        canvas2.itemconfig(texto, text="En la instalación de clonación de Kamino, un asesinato ha\nconmocionado a los residentes y visitantes. Cada uno de los cinco\npersonajes principales tiene motivos para sospechar de los demás,\ny los jugadores asumen sus roles para investigar las habitaciones y\nrecopilar pistas que revelarán al asesino, el arma utilizada y\nla ubicación del crimen.", font = ("Univers",20),justify=tkinter.LEFT)
        window.after(5000, opciones,)


    window.after(4000, intro)
    texto = canvas2.create_text(640,360, text="A long time ago in a galaxy far,\nfar away....",fill='cyan', font=("Arial", 40))
    canvas2.tag_lower(imagen2)  # Envia la imagen al fondo
    
def opciones():
    canvas2.destroy()
    canvas3.pack()
    global x

    canvas3.create_image(0, 0, anchor=tkinter.NW, image=imagen3)

    def investigar_y_restar(opcion):  # Declarar x como una variable no local para que podamos modificarla.
        global x  # Use the global variable x
        if x > 0:
            if opcion == "personaje":
                x -= 1
                investigar_personaje()

            elif opcion == "arma":
                x -= 1
                investigar_arma()

            elif opcion == "lugar":
                x -= 1
                investigar_locacion()
        else:
            final()

    boton1 = tk.Button(canvas3, text="Personaje", command=lambda: investigar_y_restar("personaje"), font=("Star Jedi", 20))
    boton2 = tk.Button(canvas3, text="Arma", command=lambda: investigar_y_restar("arma"), font=("Star Jedi", 20))
    boton3 = tk.Button(canvas3, text="Lugar", command=lambda: investigar_y_restar("lugar"), font=("Star Jedi", 20))

    canvas3.create_window(182, 540, window=boton1)
    canvas3.create_window(620, 540, window=boton2)
    canvas3.create_window(1030, 540, window=boton3)
    
window = Tk()
window.title("Clue: Star Wars")
window.geometry("1200x511")


canvas1 = Canvas(window, width=1200, height=511)
canvas1.pack()

canvas2 = Canvas(window, width=1280, height=720)
canvas3 = Canvas(window, width=1280, height=720)
canvas4 = Canvas(window, width=1280, height=720)


bg = Image.open("kamino.jpg")
bg = bg.resize((1200,511))
imagen = ImageTk.PhotoImage(bg)

bg2 = Image.open("back.png")
bg2 = bg2.resize((1280, 720))
imagen2 = ImageTk.PhotoImage(bg2)

bg3 = Image.open("Kamino2.jpg")
bg3 = bg3.resize((1280, 720))
imagen3 = ImageTk.PhotoImage(bg3)

bg4 = Image.open("kamino3.jpg")
bg4 = bg4.resize((1280, 720))
imagen4 = ImageTk.PhotoImage(bg4)

canvas1.create_image(0, 0, anchor=tkinter.NW, image=imagen)
canvas1.create_text(600,100, text= "Bienvenido al Clue de:", font=("Star Jedi", 20))
canvas1.create_text(600,200, text= "@", font=("Star Jedi", 50))

iniciar = Button(canvas1, text="Iniciar", font=("Arial",14), command=historia)
canvas1.create_window(550, 300, anchor=tkinter.NW, window=iniciar)

salir = tk.Button(canvas1, text="Salir", font=("Arial",14),command=window.destroy)
canvas1.create_window(555, 350, anchor=tkinter.NW, window=salir)

inicializar_juego()
center_window(window)

def final():
    canvas3.destroy()
    canvas4.config(background='black')
    canvas4.create_image(0, 0, anchor=tkinter.NW, image=imagen4)
    canvas4.pack(fill="both", expand=True) 
    global y
    
    def mostrar_resultado():
        
        final_culpable = combo_culpable.get()
        final_lugar = combo_lugar.get()
        final_arma = combo_arma.get()

        combo_culpable.config(state="disabled")
        combo_lugar.config(state="disabled")
        combo_arma.config(state="disabled")

        global y

        resultado = final_resultado


        label_resultado.config(text=resultado)
        
        y=0
        while y==0:
            y=buscar(list(personajes.keys()),final_culpable,1)
    
        y=0
        while y==0:
            y=buscar(list(locaciones.keys()),final_lugar,1)
    
        y=0
        while y==0:
            y=buscar(list(armas.keys()),final_arma,1)

        label_resultado.config(text=final_resultado)
        label_respuestas_correctas.config(text="Deduciste "+str(respuestas_correctas)+" parte(s) del asesinato")
        if respuestas_correctas == 3:
            label_ganaste.config(text="Ganaste")
        else:
             label_ganaste.config(text="Perdiste")

    # Crear ComboBox para culpable
    combo_culpable = ttk.Combobox(canvas4, values=["obi-Wan Kenobi", "Padme Amidala", "Capitan Rex", "Anakin Skywalker", "Darth Maul"],font=("Star Jedi",11),width=40)
    combo_culpable.set("Selecciona un culpable")
    combo_culpable.pack()

    # Crear ComboBox para lugar
    combo_lugar = ttk.Combobox(canvas4, values=["Sala de Clonacion", "Sala de Reuniones del Consejo Jedi", "Habitacion de Pruebas Jedi", "Habitacion de Comunicacion Separatista", "Laboratorio de Investigacion Kaminoano"],font=("Star Jedi",11),width=40)
    combo_lugar.set("Selecciona el lugar del asesinato")
    combo_lugar.pack()

    # Crear ComboBox para arma
    combo_arma = ttk.Combobox(canvas4, values=["Sable de luz de Obi-Wan Kenobi", "Blaster de Padme Amidala", "Blaster de Clone Trooper", "Sable de luz de Anakin Skywalker", "Sith Holocron"],font=("Star Jedi",11),width=40)
    combo_arma.set("Selecciona el arma homicida")
    combo_arma.pack()

    # Crear botón de confirmación
    confirm_button = tk.Button(canvas4, text="Confirmar", command=mostrar_resultado, state="disabled")
    confirm_button.pack()

    # Etiqueta para mostrar el resultado
    label_resultado = tk.Label(canvas4, text="",font=("Star Jedi",11),justify=tkinter.CENTER)
    label_resultado.pack()

    label_respuestas_correctas = tk.Label(canvas4, text="",font=("Star Jedi",11),justify=tkinter.CENTER)
    label_respuestas_correctas.pack()
    

    label_ganaste = tk.Label(canvas4, text="",font=("Star Jedi",11),justify=tkinter.CENTER)
    label_ganaste.pack()
    

    # Vincular la función de verificación a los cambios en las ComboBox
    def verificar_selecciones():
        if combo_culpable.get() != "Selecciona un culpable" and combo_lugar.get() != "Selecciona el lugar del asesinato" and combo_arma.get() != "Selecciona el arma homicida":
         confirm_button.config(state="active")
        else:
            confirm_button.config(state="disabled")

    # Vincular la función verificar_selecciones a los cambios en las ComboBox
    combo_culpable.bind("<<ComboboxSelected>>", lambda event, cb=combo_culpable: verificar_selecciones())
    combo_lugar.bind("<<ComboboxSelected>>", lambda event, cb=combo_lugar: verificar_selecciones())
    combo_arma.bind("<<ComboboxSelected>>", lambda event, cb=combo_arma: verificar_selecciones())

window.mainloop()