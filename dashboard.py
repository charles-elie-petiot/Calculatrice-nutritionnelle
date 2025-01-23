import tkinter as tk
from widgets import WidgetScale, WidgetButton, WidgetOption, WidgetEntry, WidgetCheckButton

class Dashboard():
    def __init__(self, width=1080, height=720):
        self.root = tk.Tk()
        self.root.title("Calculatrice nutritionnelle")
        self.root.geometry(f"{width}x{height}")

        self.variables = {
             "EC": tk.IntVar(value=3),
             "Activite": tk.IntVar(value=3),
             "Race" : tk.StringVar(value="Choisir un type de race"),
             "Stade" : tk.StringVar(value="Choisir un stade de vie"),
             "Sterilise" : tk.IntVar(value=0),
             "PB": tk.StringVar(value=""),
             "MG": tk.StringVar(value=""),
             "CB": tk.StringVar(value=""),
             "MS": tk.StringVar(value=""),
             "ENA": tk.StringVar(value=""),
             }

        categories_poids = {1: 'Maigre', 2: "Un peu maigre", 3: "Parfait", 4: "Un peu gros", 5: "Obèse"}
        categories_activite = {1: 'Très calme', 2: "Calme", 3: "Neutre", 4: "Actif", 5: "Très actif"}
        options_races = ["Autre", "Retriever", "Husky", "Boxer", "Doberman", "Lévrier"]
        options_stade = ["Adulte", "Sénior", "Sevrage", "Croissance (début)", "Croissance (fin)", "Gestante", "En lactation"]

        self.widgets = [
            WidgetScale(self, "Etat Corporel", categories_poids, from_=1, to=5, orient="horizontal", variable=self.variables["EC"]),
            WidgetScale(self, "Activité", categories_activite, from_=1, to=5, orient="horizontal", variable=self.variables["Activite"]),
            WidgetOption(self, "Race", options_races, variable = self.variables['Race']),
            WidgetOption(self, "Stade", options_stade, variable = self.variables['Stade']),
            WidgetCheckButton(self, "Sterilise", variable = self.variables['Sterilise']),
            WidgetEntry(self, "PB", variable = self.variables['PB']),
            WidgetEntry(self, "MG", variable = self.variables['MG']),
            WidgetEntry(self, "CB", variable = self.variables['CB']),
            WidgetEntry(self, "MS", variable = self.variables['MS']),
            WidgetEntry(self, "ENA", variable = self.variables['ENA']),
            WidgetButton(self, 'Button')
        ]

    def calculate(self):
            for widget in self.widgets[:-1]:
                 print(widget.get_value())
dash = Dashboard()
dash.root.mainloop()



