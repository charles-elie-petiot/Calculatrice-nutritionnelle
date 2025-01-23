import tkinter as tk
from tkinter import ttk


def create_window(width=1080, height=720):
    root = tk.Tk()
    root.title("Calculatrice nutritionnelle")
    root.geometry(f"{width}x{height}")

    # === Frames principales ===
    frame_animal = tk.Frame(root, bg='gray', bd=5, relief="ridge")
    frame_croquettes = tk.Frame(root, bg='gray', bd=5, relief="ridge")
    frame_resultats = tk.Frame(root, bg='gray', bd=5, relief="ridge")

    frame_animal.grid(row=0, column=0, columnspan=2, sticky="nsew")
    frame_croquettes.grid(row=1, column=0, sticky="nsew")
    frame_resultats.grid(row=1, column=1, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=2)
    root.grid_columnconfigure(1, weight=1)

    tk.Label(frame_croquettes, text='Mes croquettes', bg='gray', fg='white', font=("Arial", 12, "bold")).pack(side="top", pady=10)
    tk.Label(frame_resultats, text='Mes résultats', bg='gray', fg='white', font=("Arial", 12, "bold")).pack(side="top", pady=10)

    # === Frame "animal" ===
    frame_etat_corporel = tk.Frame(frame_animal, bg='gray', bd=5, relief="ridge")
    frame_races = tk.Frame(frame_animal, bg='gray', bd=5, relief="ridge")
    frame_age = tk.Frame(frame_animal, bg='gray', bd=5, relief="ridge")
    frame_activité = tk.Frame(frame_animal, bg='gray', bd=5, relief="ridge")
    frame_stérilisé = tk.Frame(frame_animal, bg='gray', bd=5, relief="ridge")

    frame_etat_corporel.grid(row=1, column=0, rowspan=2, sticky="nsew")
    frame_activité.grid(row=3, column=0, rowspan=2, sticky="nsew")
    frame_races.grid(row=2, column=1, sticky="nsew")
    frame_age.grid(row=3, column=1, sticky="nsew")
    frame_stérilisé.grid(row=4, column=1, sticky="nsew")

    frame_animal.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)
    frame_animal.grid_columnconfigure([0, 1], weight=1)
    

    # === Frame "État corporel" ===
    tk.Label(frame_etat_corporel, text="État corporel:", bg='gray', fg='white', font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
    label_poids = tk.Label(frame_etat_corporel, text="Poids sélectionné : Parfait", bg='gray', fg='white', font=("Arial", 10))
    label_poids.grid(row=1, column=0, sticky="w", pady=5)

    slider_poids = tk.Scale(frame_etat_corporel, from_=1, to=5, orient="horizontal", length=200, command=lambda value: update_label_poids(value, label_poids), showvalue=False)
    slider_poids.set(3)
    slider_poids.grid(row=2, column=0, pady=5)

    # === Frame "Activité" ===
    tk.Label(frame_activité, text="Activité:", bg='gray', fg='white', font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
    label_activité = tk.Label(frame_activité, text="Activité sélectionnée : Neutre", bg='gray', fg='white', font=("Arial", 10))
    label_activité.grid(row=1, column=0, sticky="w", pady=5)

    slider_activité = tk.Scale(frame_activité, from_=1, to=5, orient="horizontal", length=200, command=lambda value: update_label_activité(value, label_activité), showvalue=False)
    slider_activité.set(3)
    slider_activité.grid(row=2, column=0, pady=5)

    # === Frame "Races" ===
    tk.Label(frame_races, text="Type de race:", bg='gray', fg='white', font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
    type_animal_var = tk.StringVar(value="Choisir...")
    type_animal_menu = tk.OptionMenu(frame_races, type_animal_var, "Autre", "Retriever", "Husky", "Boxer", "Doberman", "Lévrier")
    type_animal_menu.grid(row=1, column=0, sticky="nsew", pady=10)

    # === Frame "Âge" ===
    tk.Label(frame_age, text="Stade de vie:", bg='gray', fg='white', font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
    type_animal_age = tk.StringVar(value="Choisir...")
    type_animal_menu = tk.OptionMenu(frame_age, type_animal_age, "Adulte", "Sénior", "Sevrage", "Croissance (début)", "Croissance (fin)", "Gestante", "En lactation")
    type_animal_menu.grid(row=1, column=0, sticky="nsew", pady=10)

    # === Frame "Stérilisé" ===
    option_var = tk.BooleanVar(value=False)
    checkbox = tk.Checkbutton(frame_stérilisé, text="Stérilisé", variable=option_var, font=("Arial", 12))
    checkbox.grid(row=0, column=0, pady=10)

    root.mainloop()


def update_label_poids(value, label_poids):
    categories_poid = {1: 'Maigre', 2: "Un peu maigre", 3: "Parfait", 4: "Un peu gros", 5: "Obèse"}
    label_poids.config(text=f"Poids sélectionné : {categories_poid[int(value)]}")


def update_label_activité(value, label_activité):
    categories_activité = {1: 'Très calme', 2: "Calme", 3: "Neutre", 4: "Actif", 5: "Très actif"}
    label_activité.config(text=f"Activité sélectionnée : {categories_activité[int(value)]}")


create_window()