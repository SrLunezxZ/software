import tkinter as tk
from tkinter import messagebox

#=============================
# Creating the window object
#=============================
w = tk.Tk()
w.title("basic calculator")
w.geometry("290x300")
w.resizable(False, False)

#=============================
# Window title object
#=============================
lbl_title = tk.Label(
    w,
    text="basic calculator",
)
lbl_title.grid(row=0, column=0, padx=10, pady=2, sticky="w")

#======================================
# Funciones de operaciones
#======================================
def calculate(operation):
    try:
        num1 = float(txt_name.get().strip())
        num2 = float(txt_age.get().strip())

        if operation == "suma":
            result = num1 + num2
        elif operation == "resta":
            result = num1 - num2
        elif operation == "multi":
            result = num1 * num2
        elif operation == "division":
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir por cero")
                return
            result = num1 / num2

        
        txt_resultado.config(state="normal")
        txt_resultado.delete("1.0", tk.END)
        txt_resultado.insert(tk.END, f"Resultado: {result:.4f}")
        txt_resultado.config(state="disabled")

    except ValueError:
        messagebox.showwarning("Advertencia", "Por favor ingresa números válidos")


#=======================================
# Number 1 
#=======================================
lbl_name = tk.Label(
    w,
    text="number 1:",
    anchor="w"
)
lbl_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")

txt_name = tk.Entry(w, width=15)
txt_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")

#=======================================
# Number 2 
#=======================================
lbl_age = tk.Label(
    w,
    text="number 2:",
    anchor="w"
)
lbl_age.grid(row=2, column=0, padx=10, pady=5, sticky="w")

txt_age = tk.Entry(w, width=15)
txt_age.grid(row=2, column=1, padx=10, pady=5, sticky="w")

#=======================================
# Buttons
#=======================================
btn_mas = tk.Button(
    w,
    text="+",
    width=5,
    command=lambda: calculate("suma")
)
btn_mas.grid(row=3, column=0, padx=10, pady=10, sticky="w")

btn_menos = tk.Button(
    w,
    text="-",
    width=5,
    command=lambda: calculate("resta")
)
btn_menos.grid(row=3, column=1, padx=10, pady=10, sticky="w")

btn_asterisco = tk.Button(
    w,
    text="*",
    width=5,
    command=lambda: calculate("multi")
)
btn_asterisco.grid(row=4, column=0, padx=10, pady=5, sticky="w")

btn_barra = tk.Button(
    w,
    text="/",
    width=5,
    command=lambda: calculate("division")
)
btn_barra.grid(row=4, column=1, padx=10, pady=5, sticky="w")


#=======================================
# Result section
#=======================================
lbl_resultado = tk.Label(
    w,
    text="Result:",
    anchor="w"
)
lbl_resultado.grid(row=6, column=0, padx=10, pady=(10, 5), sticky="w")

txt_resultado = tk.Text(
    w,
    width=10,
    height=3,
    state="disabled"
)
txt_resultado.grid(
    row=7,
    column=0,
    columnspan=2,
    padx=10,
    pady=5,
    sticky="ew"
)

w.mainloop()