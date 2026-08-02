import tkinter as tk
from tkinter import ttk

class Button(ttk.Button):
    def __init__(self, frame, key, amount, values, labels, calculate):
        """
        frame: parent frame
        key: 'bore', 'rod', 'psi', 'flow'
        amount: how much to change the value
        values: your shared values dict
        labels: your shared labels dict
        calculate: your calculate() function
        """

        symbol = "↑" if amount > 0 else "↓"

        super().__init__(frame, text=symbol)

        self.key = key
        self.amount = amount
        self.values = values
        self.labels = labels
        self.calculate = calculate

        self.config(command=self.on_click)
        self.pack()

    def on_click(self):
        new_value = self.values[self.key] + self.amount

        self.values[self.key] = new_value

        self.labels[self.key].config(
            text=f"{self.key.capitalize()}: {new_value}"
        )

        self.calculate()
