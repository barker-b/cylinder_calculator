import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("button explorer")
root. geometry("600x600")

# Variables
bore = tk.IntVar(value=4)
rod = tk.IntVar(value=2)
psi = tk.IntVar(value=1000)
flow = tk.IntVar(value=10)

a = tk.IntVar()
b = tk.IntVar()
c = tk.IntVar()
d = tk.IntVar()

# Frames
active_frame = ttk.Frame(root)
active_frame.pack()

output_frame = ttk.Frame(root)
output_frame.pack()

info_frame = ttk.Frame(active_frame,)
info_frame.pack()

button_frame = ttk.Frame(active_frame)
button_frame.pack()

# Labels
ttk.Label(info_frame, text="\n")
ttk.Label(info_frame, text=f"Bore {bore.get()}\n").pack()
ttk.Label(info_frame, text=f"Rod: {rod.get()}\n").pack()
ttk.Label(info_frame, text=f"Pressure: {psi.get()}\n").pack()
ttk.Label(info_frame, text=f"Flow: {flow.get()}\n").pack()

ttk.Label(output_frame, text=f"{a.get()}\n")
ttk.Label(output_frame, text=f"{b.get()}\n")
ttk.Label(output_frame, text=f"{c.get()}\n")
ttk.Label(output_frame, text=f"{d.get()}\n")

# maths 
def calculate():
    pass

# Buttons
ttk.Button(button_frame, text="↑", command=None).pack()
ttk.Button(button_frame, text="↓", command=None).pack()

root.mainloop()
