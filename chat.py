import tkinter as tk
from tkinter import ttk
from frames.frame_croquettes import create_frame_croquettes
from frames.frame_chat import create_frame_chat
from frames.frame_resultat_chat import create_frame_resultats_chat

def calculateur_chat():

    def calculate(entries):
        # Récupérer les valeurs des champs
        poids = float(entries['entry_poids'].get())
        activite = float(entries['combo_activite'].get())
        race = entries["combo_race"].get()
        physio = float(entries["entry_physio"].get())

        proteines = float(entries['entry_proteines'].get())
        lipides = float(entries['entry_lipides'].get())
        humidite = float(entries['entry_humidite'].get())
        cb = float(entries['entry_cb'].get())
        minerals = float(entries['entry_minerals'].get())
        humidite = float(entries['entry_humidite'].get())

        ena = 100 - proteines - lipides - cb - minerals - humidite
        entries['label_ena'].config(text=f"ENA: {ena:.2f} %")

        if activite == 1.0 and physio == 1.0:
            be = poids * 60 *0.8
        elif activite == 1.0 or physio==1.0:
            be = poids*60
        else:
            be = poids*70

        entries['label_be'].config(text=f"BE: {be:.2f} Kcal")

        besoin_proteines = int(6*poids)
        # Afficher les résultats
        entries['label_besoin_prot'].config(text=f"Besoins en protéines: {besoin_proteines:.2f} g")

        der = 3.5*proteines + 3.5*ena+ 8.5*lipides
        entries["label_der"].config(text=f"DER: {der:.2f} Kcal/100 g")


        quantite = int(be*100 / der)

        entries["label_quantite"].config(text=f"Quantité de croquettes : {quantite}g")

    # Fenêtre principale
    root = tk.Tk()
    root.title("Calculateur Nutritionnel")
    root.geometry(f'665x400+1600+300')

    # Créer les frames et récupérer les widgets
    entries = {}
    entries.update(create_frame_croquettes(root))
    entries.update(create_frame_chat(root))
    entries.update(create_frame_resultats_chat(root))

    # Bouton de calcul
    btn_calculer = ttk.Button(root, text="Calculer", command=lambda: calculate(entries))
    btn_calculer.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop() 
