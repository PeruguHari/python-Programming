import tkinter as tk
import time
import matplotlib.pyplot as plt
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Power ratings in kW (1 unit = 1 kWh)
power_ratings = {
    "Fan": 0.075, "Light": 0.010, "AC": 1.500, 
    "TV": 0.150, "Refrigerator": 0.200, "Water Heater": 2.000
}

# Appliance states
appliances = {device: {"state": False, "start_time": None, "energy_used": 0} for device in power_ratings}

def toggle_appliance(device, button):
    """Toggle an appliance ON/OFF and update energy usage"""
    if appliances[device]["state"]:
        appliances[device]["state"] = False
        end_time = time.time()
        appliances[device]["energy_used"] += ((end_time - appliances[device]["start_time"]) / 3600) * power_ratings[device]
        appliances[device]["start_time"] = None
        button.config(bg="#FF3B30", text=f"{device} OFF")
    else:
        appliances[device]["state"] = True
        appliances[device]["start_time"] = time.time()
        button.config(bg="#4CD964", text=f"{device} ON")
    update_energy()

def update_energy():
    """Update the total energy used label and refresh the graph."""
    for device in appliances:
        if appliances[device]["state"] and appliances[device]["start_time"]:
            current_time = time.time()
            appliances[device]["energy_used"] += ((current_time - appliances[device]["start_time"]) / 3600) * power_ratings[device]
            appliances[device]["start_time"] = current_time
    total_energy = sum(appliances[device]["energy_used"] for device in appliances)
    total_bill = total_energy * 70.00  # 1 unit = 70.00 rupees
    energy_label.config(text=f"Total Energy: {total_energy:.2f} Units\nTotal Bill: ₹{total_bill:.2f}")
    update_graph()

def update_graph():
    """Update the graph dynamically with energy usage."""
    labels = list(appliances.keys())
    values = [appliances[device]["energy_used"] for device in labels]
    ax.clear()
    ax.bar(labels, values, color=['blue', 'yellow', 'red', 'purple', 'green', 'orange'])
    ax.set_ylabel("Energy Usage (Units)", fontsize=12)
    ax.set_title("Energy Consumption Per Appliance", fontsize=14)
    ax.set_xticklabels(labels, rotation=45, fontsize=10)
    canvas.draw()

def auto_refresh_graph():
    """Automatically update the graph every 5 seconds."""
    while True:
        time.sleep(5)
        update_energy()
        update_graph()

# GUI Setup
root = tk.Tk()
root.title("Hari's Home Applications")
root.geometry("500x700")
root.configure(bg="#1E1E1E")

title_label = tk.Label(root, text="Hari's Home Applications", font=("Arial", 18, "bold"), fg="white", bg="#1E1E1E")
title_label.pack(pady=10)

# Appliance Buttons
buttons = {}
for device in appliances:
    buttons[device] = tk.Button(root, text=f"{device} OFF", font=("Arial", 14), bg="#FF3B30", fg="white", width=20,
                                command=lambda d=device: toggle_appliance(d, buttons[d]))
    buttons[device].pack(pady=5)

# Energy Label
energy_label = tk.Label(root, text="Total Energy: 0.00 Units\nTotal Bill: ₹0.00", font=("Arial", 14), bg="#1E1E1E", fg="white")
energy_label.pack(pady=10)

# Graph Setup
fig, ax = plt.subplots(figsize=(7, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Start Auto Graph Refresh in Background
threading.Thread(target=auto_refresh_graph, daemon=True).start()

# Run GUI
root.mainloop()