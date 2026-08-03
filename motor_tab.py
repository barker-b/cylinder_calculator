from tkinter import ttk
import calculator as calc
from button_class import Button

def build_motor_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Motor")

    mot_frame = ttk.Frame(tab)
    mot_frame.pack()

        # Variables
    values = {
        "displacement": 10,
        "psi": 1000,
        "flow": 10,
    }


    # Frames
    active_frame = ttk.Frame(tab,)
    active_frame.pack()

    displacement_frame = ttk.Frame(active_frame)
    displacement_frame.pack(pady=20)
    psi_frame = ttk.Frame(active_frame)
    psi_frame.pack(pady=20)
    flow_frame = ttk.Frame(active_frame)
    flow_frame.pack(pady=20)


    output_frame = ttk.Frame(tab)
    output_frame.pack()

    # Labels

    labels = {}

    formats = {
    "displacement": "Displacement: {} in³.",
    "psi": "Pressure: {} PSI.",
    "flow": "Flow: {} GPM.",
    }

    labels["displacement"] = ttk.Label(
        displacement_frame,
        text=f"Displacement: {values['displacement']} in³",
        font=("TkDefaultFont", 12)
    )

    labels["psi"] = ttk.Label(
        psi_frame,
        text=f"Pressure: {values['psi']} PSI",
        font=("TkDefaultFont", 12)
    )

    labels["flow"] = ttk.Label(
        flow_frame,
        text=f"Flow: {values['flow']} GPM",
        font=("TkDefaultFont", 12)
    )

    labels["displacement"].pack()
    labels["psi"].pack()
    labels["flow"].pack()

    output = ttk.Label(output_frame, text="", font=("TkDefaultFont", 12))
    output.pack()

    # maths 
    def calculate():

        displacement = values["displacement"]
        psi = values["psi"]
        flow = values["flow"]

        torque = calc.torque(psi, displacement)
        speed = calc.mot_speed(flow, displacement)
        
            
        outputs = (
            f"Motor tourque: {torque:,.0f} in-lbs.\n"
            f"Motor speed: {speed:.0f} rpm.\n"
        )

        output.config(text=outputs)
        

    calculate()

    def motor_stops(key, new_value, values):
        if new_value < 0:
             new_value = 0
        return new_value
        

    def button(key, amount):
            values[key] += amount
            labels[key].config(text=f"{key.capitalize()}: {values[key]}")
            calculate()

        

    Button(displacement_frame, "displacement", +0.5, values, labels, calculate, motor_stops, formats)
    Button(displacement_frame, "displacement", -0.5, values, labels, calculate, motor_stops, formats)

    Button(psi_frame, "psi", +100, values, labels, calculate, motor_stops, formats)
    Button(psi_frame, "psi", -100, values, labels, calculate, motor_stops, formats)

    Button(flow_frame,"flow", +1, values, labels, calculate, motor_stops, formats)
    Button(flow_frame,"flow", -1, values, labels, calculate, motor_stops, formats)
