import tkinter as tk

class Widget():
    def __init__(self, dash, label_text, **kwargs):
        self.dash = dash
        self.label = tk.Label(self.dash.root, text=label_text)

    
class WidgetScale(Widget):
    def __init__(self, dash, label_text, categories, **kwargs):
        super().__init__(dash, label_text)
        self.label_text = label_text
        self.categories = categories
        self.widget = tk.Scale(self.dash.root, from_=kwargs.get("from_"), to=kwargs.get("to"), orient=kwargs.get("orient"), showvalue=False, command=lambda value: self.change_value(value))
        self.widget.set(3)
        self.widget.pack(pady=5)
        self.value = kwargs.get("variable")
        self.label = tk.Label(self.dash.root, font=("Arial", 10))
        self.label.pack(ipady=5)

    def change_value(self, value):
        self.label.config(text=f"{self.label_text}: {self.categories[int(value)]}")
        self.value = value

    def get_value(self):
        return self.value
    

class WidgetOption(Widget):
    def __init__(self, dash, label_text, options, **kwargs):
        super().__init__(dash, label_text)
        self.options = options
        self.variable = kwargs.get("variable")
        self.widget = tk.OptionMenu(self.dash.root, self.variable, *self.options)
        self.widget.pack(pady=5)

    def get_value(self):
        return self.variable.get()
    
class WidgetEntry(Widget):
    def __init__(self, dash, label_text, **kwargs):
        super().__init__(dash, label_text)
        self.variable = kwargs.get("variable")
        self.widget = tk.Entry(self.dash.root, textvariable=self.variable, validate="key")
        self.widget.pack(pady=5)
        self.label = tk.Label(self.dash.root, font=("Arial", 10))
        self.label.pack(ipady=5)

        self.widget.config(validate="key", validatecommand=(self.dash.root.register(self.validate_input), "%S"))

    def validate_input(self, char):
        if char.isdigit() or char == "":
            return True
        else:
            return False
        
    def get_value(self):
        return self.variable.get()
    
class WidgetCheckButton(Widget):
    def __init__(self, dash, label_text, **kwargs):
        super().__init__(dash, label_text)
        self.variable = kwargs.get("variable")
        self.widget = tk.Checkbutton(self.dash.root, text=label_text, variable=self.variable)
        self.widget.pack(pady=5)

    def get_value(self):
        return self.variable.get()
    
class WidgetButton(Widget):
    def __init__(self, dash, label_text, **kwargs):
        super().__init__(dash, label_text)
        self.widget = tk.Button(self.dash.root, command=self.on_click)
        self.widget.pack(pady=5)
        self.label.pack(pady=5)

    def on_click(self):
        self.dash.calculate()

