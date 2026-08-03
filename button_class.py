import tkinter as tk
from tkinter import ttk

class Button(ttk.Button):
    def __init__(self, frame, key, amount, values, labels, calculate, safety, formats):
        """
        A class for adjusting parameters using buttons
        """

        symbol = "↑" if amount > 0 else "↓"

        super().__init__(frame, text=symbol)

        self.key = key
        self.amount = amount
        self.values = values
        self.labels = labels
        self.calculate = calculate
        self.safety = safety
        self.formats = formats

        self.config(command=self.on_click)
        self.pack()

    def on_click(self):
        
        new_value = self.values[self.key] + self.amount

        new_value = self.safety(self.key, new_value, self.values)

        self.values[self.key] = new_value

        fmt = self.formats[self.key]
        self.labels[self.key].config(text=fmt.format(new_value))
        

        self.calculate()
