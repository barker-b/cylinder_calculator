import tkinter as tk
from tkinter import ttk

class Button(ttk.Button):
    def __init__(self, frame, key, amount, values, labels, calculate):
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

        self.config(command=self.on_click)
        self.pack()

    def on_click(self):
        new_value = self.values[self.key] + self.amount


        # Don't let values go below zero.
        if new_value < 0:
            new_value = 0

        # Don't let rod be greater than bore.
        if self.key == "rod" and new_value >= self.values["bore"]:
            new_value = self.values["bore"] - 0.25

        # Don't let bore be smaller than rod.
        if self.key == "bore" and new_value <= self.values["rod"]:
            new_value = self.values["rod"] + 0.5


        self.values[self.key] = new_value

        self.labels[self.key].config(
            text=f"{self.key.capitalize()}: {new_value}"
        )

        self.calculate()
