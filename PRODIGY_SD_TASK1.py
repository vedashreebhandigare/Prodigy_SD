import tkinter as tk
from tkinter import ttk, messagebox

def convert_temp():
    try:
        val = float(entry_val.get())
        from_unit = combo_from.get()
        
        result = ""
        if from_unit == "Celsius":
            kelvin = val + 273.15
            fahrenheit = (val * 9 / 5) + 32
            result = f"Kelvin: {kelvin:.2f}\nFahrenheit: {fahrenheit:.2f}"
        elif from_unit == "Fahrenheit":
            celsius = (val - 32) * 5 / 9
            kelvin = celsius + 273.15
            result = f"Celsius: {celsius:.2f}\nKelvin: {kelvin:.2f}"
        elif from_unit == "Kelvin":
            celsius = val - 273.15
            fahrenheit = (celsius * 9 / 5) + 32
            result = f"Celsius: {celsius:.2f}\nFahrenheit: {fahrenheit:.2f}"
        else:
            result = "Invalid selection."
        
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Input error", "Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Enter temperature:").pack(pady=5)
entry_val = tk.Entry(root, width=20)
entry_val.pack(pady=5)

tk.Label(root, text="Select original unit:").pack(pady=5)
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from.pack(pady=5)
combo_from.current(0)

btn_convert = tk.Button(root, text="Convert", command=convert_temp)
btn_convert.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack(pady=10)

root.mainloop()
