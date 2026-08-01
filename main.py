import tkinter as tk
from tkinter import ttk
import calculator as calc

root = tk.Tk()
root.title("button explorer")
root. geometry("600x600")

# Variables

bore = 4
rod = 2
psi = 1000
flow = 10


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


ttk.Label(bore_frame, text=f"Bore {bore}").pack()
ttk.Label(rod_frame, text=f"Rod: {rod}").pack()
ttk.Label(psi_frame, text=f"Pressure: {psi}").pack()
ttk.Label(flow_frame, text=f"Flow: {flow}").pack()

output = ttk.Label(output_frame, text="")
output.pack()

# maths 
def calculate():

    global bore
    global rod
    global psi
    global flow

    push, pull = calc.force(psi, bore, rod)
    ext_speed, ret_speed = calc.cyl_speed(flow, bore, rod)

    
    outputs = (
        f"Push force: {push}\n"
        f"Pull force: {pull}\n"
        f"Extend speed: {ext_speed}\n"
        f"Retract speed: {ret_speed}\n"
    )

    output.config(text=outputs)
    

calculate()

def button():
    global bore
    global rod
    global psi
    global flow
    
    push, pull = calc.force(psi, bore, rod)
    ext_speed, ret_speed = calc.cyl_speed(flow, bore, rod)
    
    outputs = (
    f"Push force: {push}\n"
    f"Pull force: {pull}\n"
    f"Extend speed: {ext_speed}\n"
    f"Retract speed: {ret_speed}\n"
    )

    output.config(text=outputs)
    

# Buttons
bore_up = ttk.Button(bore_frame, text="↑", command=button).pack()
bore_down = ttk.Button(bore_frame, text="↓", command=button).pack()
rod_up = ttk.Button(rod_frame, text="↑", command=button).pack()
rod_down = ttk.Button(rod_frame, text="↓", command=button).pack()
psi_up = ttk.Button(psi_frame, text="↑", command=button).pack()
psi_down = ttk.Button(psi_frame, text="↓", command=button).pack()
flow_up = ttk.Button(flow_frame, text="↑", command=button).pack()
flow_down = ttk.Button(flow_frame, text="↓", command=button).pack()


root.mainloop()

