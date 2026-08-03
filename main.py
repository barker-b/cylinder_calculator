import tkinter as tk
from tkinter import ttk
import calculator as calc
from button_class import Button
from cylinder_tab import build_cyl_tab
from motor_tab import build_motor_tab

root = tk.Tk()
root.title("Cylinder Calculator")
root.geometry("600x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

build_cyl_tab(notebook)
build_motor_tab(notebook)

root.mainloop()

