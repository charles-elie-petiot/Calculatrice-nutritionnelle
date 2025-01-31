import tkinter as tk
from tkinter import ttk

def create_frame_croquettes(root):
    frame = ttk.LabelFrame(root, text="Croquettes")
    frame.grid(row=0, column=0, columnspan =2, padx=10, pady=10, sticky="nsew")

    ttk.Label(frame, text="Prot (%)").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_proteines = ttk.Entry(frame)
    entry_proteines.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame, text="MG (Lipides %)").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_lipides = ttk.Entry(frame)
    entry_lipides.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    
    ttk.Label(frame, text="Cellulose Brute (%)").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_cb = ttk.Entry(frame)
    entry_cb.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame, text="Matières minérales").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    entry_minerals = ttk.Entry(frame)
    entry_minerals.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame, text="Humidité (%)").grid(row=0, column=2, padx=5, pady=5, sticky="w")
    options_humidite = ["RC, Hill's, Proplan, ...", "alim indus", "Frolic like", "Autre"]
    combo_humidite = ttk.Combobox(frame, values=options_humidite, state="readonly")
    combo_humidite.grid(row=0, column=3, padx=5, pady=5, sticky="w")
    combo_humidite.current(0)
    entry_humidite = ttk.Entry(frame, state="normal")
    entry_humidite.insert(0, 8.5)
    entry_humidite.config(state="disabled")

    humidite = {
        "RC, Hill's, Proplan, ..." : 8.5,
        "alim indus": 9,
        "Frolic like": 12,
    }

    def handle_humidite_change(event):
        selected_option = combo_humidite.get()
        if selected_option == "Autre":
            entry_humidite.config(state="normal")
        else:
            entry_humidite.config(state="normal")
            entry_humidite.delete(0, tk.END)
            entry_humidite.insert(0, humidite[selected_option])
            entry_humidite.config(state="disabled")



    combo_humidite.bind("<<ComboboxSelected>>", handle_humidite_change)

    entry_humidite.grid(row=1, column=3, padx=5, pady=5, sticky="w")
    label_ena = ttk.Label(frame, text="ENA (%)")
    label_ena.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="w")

    label_der = ttk.Label(frame, text="DER :")
    label_der.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="w")

    return {
        "entry_proteines": entry_proteines,
        "entry_lipides": entry_lipides,
        "entry_humidite": entry_humidite,
        "entry_cb": entry_cb,
        "entry_minerals": entry_minerals,
        "label_ena": label_ena,
        "label_der": label_der,
    }
