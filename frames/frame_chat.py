import tkinter as tk
from tkinter import ttk

def create_frame_chat(root):
    frame = ttk.LabelFrame(root, text="Animal")
    frame.grid(row=1, column=0, rowspan=2,padx=10, pady=10, sticky="nsew")

    ttk.Label(frame, text="Poids idéal (kg)").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_poids = ttk.Entry(frame)
    entry_poids.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame, text="Chat d'intérieur").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    var = tk.IntVar()
    var.set(1)
    combo_activite = tk.Checkbutton(frame, text='', variable=var)
    combo_activite.grid(row=1, column=1, padx=0, pady=5, sticky="w")

    ttk.Label(frame, text="Race").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    combo_race = ttk.Combobox(frame, values=["Sphinx", "Autres"])
    combo_race.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    combo_race.current(1)

    ttk.Label(frame, text="Stérilisé").grid(row=4, column=0, padx=5, pady=5, sticky="w")
    var_ste = tk.IntVar()
    var_ste.set(1)
    sterilise= tk.Checkbutton(frame, text='', variable=var_ste)
    sterilise.grid(row=4, column=1, padx=0, pady=5, sticky="w")

    return {
        "entry_poids": entry_poids,
        "combo_activite": var,
        "combo_race": combo_race,
        "entry_physio": var_ste,
    }
