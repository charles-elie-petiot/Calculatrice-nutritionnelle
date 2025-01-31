import tkinter as tk
from tkinter import ttk

def create_frame_resultats(root):
    frame = ttk.LabelFrame(root, text="Résultats")
    frame.grid(row=1, column=1,rowspan=2, padx=10, pady=10, sticky="nsew")

    label_bee = ttk.Label(frame, text="BEE: ")
    label_bee.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    label_be = ttk.Label(frame, text="BE: ")
    label_be.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    ttk.Label(frame, text="").grid(row=4, column=0)  # Ajoute un espace vide


    label_besoin_prot = ttk.Label(frame, text="Besoins en protéines: ")
    label_besoin_prot.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    label_quantite = ttk.Label(frame, text="Quantité de croquettes :")
    label_quantite.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    return {
        "label_be": label_be,
        "label_bee": label_bee,
        "label_besoin_prot": label_besoin_prot,
        "label_quantite": label_quantite
    }
