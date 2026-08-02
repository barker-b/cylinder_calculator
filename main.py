import tkinter as tk
from tkinter import ttk
import calculator as calc
from button_class import Button

root = tk.Tk()
root.title("Cylinder Calculator")
root.geometry("600x600")

# Variables
values = {
    "bore": 4,
    "rod": 2,
    "psi": 1000,
    "flow": 10,
}


# Frames
active_frame = ttk.Frame(root,)
active_frame.pack()

bore_frame = ttk.Frame(active_frame)
bore_frame.pack(pady=20)
rod_frame = ttk.Frame(active_frame)
rod_frame.pack(pady=20)
psi_frame = ttk.Frame(active_frame)
psi_frame.pack(pady=20)
flow_frame = ttk.Frame(active_frame)
flow_frame.pack(pady=20)


output_frame = ttk.Frame(root)
output_frame.pack()

# Labels

labels = {}


labels["bore"] = ttk.Label(
    bore_frame,
    text=f"Bore: {values['bore']}",
    font=("TkDefaultFont", 12)
)

labels["rod"] = ttk.Label(
    rod_frame,
    text=f"Rod: {values['rod']}",
    font=("TkDefaultFont", 12)
)

labels["psi"] = ttk.Label(
    psi_frame,
    text=f"Pressure: {values['psi']}",
    font=("TkDefaultFont", 12)
)

labels["flow"] = ttk.Label(
    flow_frame,
    text=f"Flow: {values['flow']}",
    font=("TkDefaultFont", 12)
)

labels["bore"].pack()
labels["rod"].pack()
labels["psi"].pack()
labels["flow"].pack()

output = ttk.Label(output_frame, text="", font=("TkDefaultFont", 12))
output.pack()

# maths 
def calculate():

    bore = values["bore"]
    rod = values["rod"]
    psi = values["psi"]
    flow = values["flow"]
    
    push, pull = calc.force(psi, bore, rod)
    ext_speed, ret_speed = calc.cyl_speed(flow, bore, rod)

    
    outputs = (
        f"Push force: {push:,.0f} pounds.\n"
        f"Pull force: {pull:,.0f} pounds.\n"
        f"Extend speed: {ext_speed:.0f} in/min\n"
        f"Retract speed: {ret_speed:.0f} in/min\n"
    )

    output.config(text=outputs)
    

calculate()

def button(key, amount):
        values[key] += amount
        labels[key].config(text=f"{key.capitalize()}: {values[key]}")
        calculate()

    

Button(bore_frame, "bore", +0.5, values, labels, calculate)
Button(bore_frame, "bore", -0.5, values, labels, calculate)

Button(rod_frame, "rod", +0.25, values, labels, calculate)
Button(rod_frame, "rod", -0.25, values, labels, calculate)

Button(psi_frame, "psi", +100, values, labels, calculate)
Button(psi_frame, "psi", -100, values, labels, calculate)

Button(flow_frame,"flow", +1, values, labels, calculate)
Button(flow_frame,"flow", -1, values, labels, calculate)


root.mainloop()

