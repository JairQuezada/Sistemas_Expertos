import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  

# Se crea nuestra base de datos
database = [
    {"name": "Betty", "human": True, "realeza": False, "magia": True, "mujer": True, "vuela": False,
     "elemental": False},
    {"name": "BMO", "human": False, "realeza": False, "magia": False, "mujer": False, "vuela": False,
     "elemental": False},
    {"name": "Finn", "human": True, "realeza": False, "magia": False, "mujer": False, "vuela": False,
     "elemental": False},
    {"name": "Princesa flama", "human": False, "realeza": True, "magia": True, "mujer": True, "vuela": True,
     "elemental": True},
    {"name": "Princesa Grumosa", "human": False, "realeza": True, "magia": True, "mujer": True, "vuela": True,
     "elemental": False},
    {"name": "Jake", "human": False, "realeza": False, "magia": True, "mujer": False, "vuela": False,
     "elemental": False},
    {"name": "Marceline", "human": True, "realeza": True, "magia": True, "mujer": True, "vuela": True,
     "elemental": False},
    {"name": "Dulce Princesa", "human": False, "realeza": True, "magia": True, "mujer": True, "vuela": False,
     "elemental": True},
    {"name": "Rey Helado", "human": True, "realeza": True, "magia": True, "mujer": False, "vuela": True,
     "elemental": False},
]

current_question = 0
result = None
character_probabilities = {}  # Probabilidades de personajes

def calculate_character_probabilities():
    for character in database:
        probability = 1.0
        for i in range(current_question):
            if character[properties[i]] == answers[i]:
                probability *= 0.8  # Aumentar o disminuir según la confianza en las respuestas anteriores
            else:
                probability *= 0.2
        character_probabilities[character["name"]] = probability

def show_question():
    global current_question
    if current_question < len(properties):
        if result:
            result.destroy()
        if current_question > 0:
            question_windows[current_question - 1].destroy()  # Cierra la ventana anterior
        question_window = tk.Toplevel(window)
        question_window.title("Question")
        question_windows.append(question_window)  # Agrega la ventana actual a la lista
        tk.Label(question_window, text=questions[current_question]).pack()
        tk.Button(question_window, text="Yes", command=lambda: on_button_click(True)).pack()
        tk.Button(question_window, text="No", command=lambda: on_button_click(False)).pack()
        current_question += 1

def show_character_image(character_name):
    character = next((char for char in database if char["name"] == character_name), None)
    
    if character:
        image_path = image_paths[database.index(character)]
        img = Image.open(image_path)
        img = img.resize((200, 300))  # Ajusta el tamaño de la imagen
        photo = ImageTk.PhotoImage(img)

        character_image = tk.Label(result, image=photo)
        character_image.image = photo
        character_image.grid(column=2, row=1, columnspan=3)  # Usa grid para organizar la imagen

def show_result():
    global result
    if result:
        result.destroy()

    # Cierra la ventana de pregunta actual si existe
    if question_windows:
        question_windows[-1].destroy()
        question_windows.pop()

    lienzo.destroy()
    update_button.place(x=250, y=2000) 

    sorted_characters = sorted(character_probabilities.items(), key=lambda x: x[1], reverse=True)
    result_text = f"Es probable que tu personaje sea {sorted_characters[0][0]}."
    
    result_label = tk.Label(window, text=result_text, font=("Arial", 14))
    result_label.grid(column=2, row=2)
    
    show_character_image(sorted_characters[0][0])
    
    exit_button = tk.Button(window, text="Salir", command=window.destroy)
    exit_button.grid(column=2, row=3)
    restart_button = tk.Button(window, text="Reiniciar", command=reset_program)
    restart_button.grid(column=2, row=4)

def on_button_click(answer):
    answers.append(answer)
    
    calculate_character_probabilities()
    
    if current_question < len(properties):
        show_question()
    else:
        show_result()

def reset_program():
    global current_question, result, answers, character_probabilities
    current_question = 0
    result = None
    answers = []
    character_probabilities = {}
    for window in question_windows:
        window.destroy()
    question_windows.clear()
    show_question()

    #Se centra la ventana para que aparezca en el centro de la pantalla
def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

#Se crea la ventana por media de Tk
window = Tk()
window.title("Akinator Fake")
window.minsize(width=560, height=800)

window.update_idletasks()
center_window(window)

result = None

# Se crea un lienzo
lienzo = Canvas(window, width=560, height=800)
lienzo.grid(column=0, row=0)

# Aqui se cargan las imagenes y se les cambia el tamaño para que esten del mismo tamaño
image_paths = [
    "Betty.png",
    "BMO.png",
    "finn.png",
    "FlamePrincess.png",
    "grumosa.png",
    "Jake.png",
    "Marceline.png",
    "Princess_Bubblegum.png",
    "rey.png",
]


images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize((100, 150)) 
    photo = ImageTk.PhotoImage(img)
    images.append(photo)
lienzo.create_text(280, 650, text = "            Bienvenido a Akinator Fake.\nPorfavor elija uno de los nueve personajes,\n        para que este programa lo adivine", font=("Arial", 14))

# Se acomodan las imagenes en una cuadricula 3x3
for i, img in enumerate(images):
    row, col = divmod(i, 3)  
    lienzo.create_image(col * 200 + 80, row * 200 + 100, image=img)

update_button = Button(window, text="Listo", font=("Arial, 14"), command=show_question)
update_button.place(x=250, y=700)  # Coloca el botón en las coordenadas (100, 100)

question_windows = []  # Lista para mantener las ventanas de pregunta abiertas

properties = ["human", "realeza", "magia", "mujer", "vuela", "elemental"]
questions = ["Tu personaje es humano?", "Tu personaje es parte de la realeza?",
             "Tu personaje puede hacer magia?", "Tu personaje forma parte del genero femenino?",
             "Puede tu personaje volar o flotar?", "Tu personaje es parte de los cuatro elementales?"]
answers = []

window.mainloop()