import math
import tkinter as tk
from tkinter import ttk, messagebox


def convert_temperature():
    """Convert the entered temperature to the selected unit."""
    try:
        value = float(temperature_var.get().strip())

        if not math.isfinite(value):
            raise ValueError

        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        # Convert the input value to Celsius first.
        if from_unit == "Celsius":
            celsius = value
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9
        else:  # Kelvin
            celsius = value - 273.15

        # Temperatures below absolute zero are not physically possible.
        if celsius < -273.15:
            messagebox.showerror(
                "Invalid temperature",
                "Please enter a temperature at or above absolute zero."
            )
            return

        # Convert Celsius to the chosen output unit.
        if to_unit == "Celsius":
            converted_value = celsius
            symbol = "°C"
        elif to_unit == "Fahrenheit":
            converted_value = (celsius * 9 / 5) + 32
            symbol = "°F"
        else:  # Kelvin
            converted_value = celsius + 273.15
            symbol = "K"

        result_var.set(f"{converted_value:.2f} {symbol}")

    except ValueError:
        messagebox.showerror(
            "Invalid input",
            "Please enter a valid numeric temperature."
        )


def reset_fields():
    """Clear the input and restore the default unit choices."""
    temperature_var.set("")
    from_unit_var.set("Celsius")
    to_unit_var.set("Fahrenheit")
    result_var.set("Your converted temperature will appear here")
    temperature_entry.focus()


# Create the main application window.
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("520x430")
root.resizable(False, False)
root.configure(bg="#EAF2FF")

# Variables that store values from the GUI.
temperature_var = tk.StringVar()
from_unit_var = tk.StringVar(value="Celsius")
to_unit_var = tk.StringVar(value="Fahrenheit")
result_var = tk.StringVar(value="Your converted temperature will appear here")

# Page heading.
tk.Label(
    root,
    text="Temperature Converter",
    font=("Arial", 24, "bold"),
    bg="#EAF2FF",
    fg="#12355B"
).pack(pady=(28, 6))

tk.Label(
    root,
    text="Convert between Celsius, Fahrenheit and Kelvin",
    font=("Arial", 11),
    bg="#EAF2FF",
    fg="#456A8F"
).pack(pady=(0, 20))

# Main card.
card = tk.Frame(root, bg="white", padx=28, pady=24)
card.pack(padx=35, fill="both")

tk.Label(
    card,
    text="Enter temperature",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#12355B"
).grid(row=0, column=0, columnspan=2, sticky="w")

temperature_entry = tk.Entry(
    card,
    textvariable=temperature_var,
    font=("Arial", 14),
    width=27,
    relief="solid",
    bd=1
)
temperature_entry.grid(row=1, column=0, columnspan=2, pady=(6, 18), ipady=6)
temperature_entry.focus()

tk.Label(
    card,
    text="From",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#12355B"
).grid(row=2, column=0, sticky="w")

tk.Label(
    card,
    text="To",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#12355B"
).grid(row=2, column=1, sticky="w", padx=(16, 0))

units = ["Celsius", "Fahrenheit", "Kelvin"]

from_menu = ttk.Combobox(
    card,
    textvariable=from_unit_var,
    values=units,
    state="readonly",
    width=16,
    font=("Arial", 11)
)
from_menu.grid(row=3, column=0, pady=(6, 20), ipady=4)

to_menu = ttk.Combobox(
    card,
    textvariable=to_unit_var,
    values=units,
    state="readonly",
    width=16,
    font=("Arial", 11)
)
to_menu.grid(row=3, column=1, padx=(16, 0), pady=(6, 20), ipady=4)

button_frame = tk.Frame(card, bg="white")
button_frame.grid(row=4, column=0, columnspan=2, pady=(0, 18))

tk.Button(
    button_frame,
    text="Convert",
    command=convert_temperature,
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="#12355B",
    activebackground="#1D4ED8",
    activeforeground="white",
    width=13,
    relief="flat",
    pady=8
).grid(row=0, column=0, padx=6)

tk.Button(
    button_frame,
    text="Reset",
    command=reset_fields,
    font=("Arial", 11, "bold"),
    bg="#DCE8F7",
    fg="#12355B",
    activebackground="#C9DBF1",
    width=13,
    relief="flat",
    pady=8
).grid(row=0, column=1, padx=6)

tk.Label(
    card,
    textvariable=result_var,
    font=("Arial", 14, "bold"),
    bg="#E8F1FF",
    fg="#12355B",
    wraplength=380,
    padx=14,
    pady=14
).grid(row=5, column=0, columnspan=2, sticky="ew")

# Pressing Enter performs conversion too.
root.bind("<Return>", lambda event: convert_temperature())

root.mainloop()