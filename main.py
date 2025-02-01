import tkinter as tk
from tkinter import ttk
from chien import calculateur_chien
from chat import calculateur_chat



def main():

    def ouvrir_chien():
        accueil.destroy()
        calculateur_chien()

    def ouvrir_chat():
        accueil.destroy()
        calculateur_chat()

    accueil = tk.Tk()
    accueil.title("Calculateur nutritionnel")
    accueil.geometry(f'200x150+800+300')


    chien = tk.Button(accueil, text="Chien", command=ouvrir_chien)
    chien.pack(padx=20, pady=20)
    chat = tk.Button(accueil, text="Chat", command=ouvrir_chat)
    chat.pack(padx=20, pady=20)

    accueil.mainloop()


main()