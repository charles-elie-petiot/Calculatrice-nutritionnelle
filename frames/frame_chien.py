import tkinter as tk
from tkinter import ttk

def create_frame_chien(root):
    frame = ttk.LabelFrame(root, text="Animal")
    frame.grid(row=1, column=0, rowspan=2,padx=10, pady=10, sticky="nsew")

    ttk.Label(frame, text="Poids idéal (kg)").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_poids = ttk.Entry(frame)
    entry_poids.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame, text="Activité").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    combo_activite = ttk.Combobox(frame, values=["Sedentaire", "Calme", "Normal", "Actif"])
    combo_activite.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    combo_activite.current(2)

    ttk.Label(frame, text="Race").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    combo_race = ttk.Combobox(frame, values=["Races nordiques, Retriever", "Cocker, Beagle", "Levrier, Dogue allemand", "Autres"])
    combo_race.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    combo_race.current(0)

    ttk.Label(frame, text="Etat Physiologique").grid(row=3, column=0, padx=5, pady=5,sticky="w")
    combo_physio = ttk.Combobox(frame, values=["Adulte", "Agé", "Castré", "Fin de gestation", "Croissance (début)", "Croissance (fin)", "Valeur manuelle"])
    combo_physio.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    combo_physio.current(0)

    entry_physio = ttk.Entry(frame, state="normal")
    entry_physio.insert(0, 1)
    entry_physio.config(state="disabled")

    physio = {
        "Adulte": 1,
        "Agé": 0.8, 
        "Castré": 0.8, 
        "Fin de gestation": 1.4, 
        "Croissance (début)": 2, 
        "Croissance (fin)": 1.3,
    }

    def handle_physio_change(event):
        selected_option = combo_physio.get()
        if selected_option == "Valeur manuelle":
            entry_physio.config(state="normal")
        else:
            entry_physio.config(state="normal")
            entry_physio.delete(0, tk.END)
            entry_physio.insert(0, physio[selected_option])
            entry_physio.config(state="disabled")



    combo_physio.bind("<<ComboboxSelected>>", handle_physio_change)

    entry_physio.grid(row=4, column=1, padx=5, pady=5, sticky="w")


    return {
        "entry_poids": entry_poids,
        "combo_activite": combo_activite,
        "combo_race": combo_race,
        "entry_physio": entry_physio
    }
