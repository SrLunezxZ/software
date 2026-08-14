import tkinter as tk
from tkinter import messagebox

#=============================
# Creating the window object
#=============================
w = tk.Tk()
w.title("Conversor Medidas")
w.geometry("320x280")
w.resizable(False, False)

#=============================
# Titulo
#=============================
lbl_title = tk.Label(
    w,
    text="Conversor Medidas",

)
lbl_title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#======================================
# Funciones de conversion
#======================================
def libras_a_kilos():
    try:
        valor = float(txt_libras.get().strip())
        resultado = valor * 0.453592
        lbl_res_libras.config(text=f"{resultado:.2f} K")
    except ValueError:
        messagebox.showwarning("Advertencia", "Ingresa un numero valido")


def metros_a_km():
    try:
        valor = float(txt_metros.get().strip())
        resultado = valor / 1000
        lbl_res_metros.config(text=f"{resultado:.4f} km")
    except ValueError:
        messagebox.showwarning("Advertencia", "Ingresa un numero valido")


def yardas_a_cm():
    try:
        valor = float(txt_yardas.get().strip())
        resultado = valor * 91.44
        lbl_res_yardas.config(text=f"{resultado:.2f} cm")
    except ValueError:
        messagebox.showwarning("Advertencia", "Ingresa un numero valido")


#=======================================
# Fila Libras
#=======================================
lbl_libras = tk.Label(
w,
text="Libras"
)
lbl_libras.grid(row=1, column=0, padx=10, pady=15, sticky="w")


txt_libras = tk.Entry(
w,
width=10
)
txt_libras.grid(row=1, column=1, padx=5, pady=15)


btn_libras = tk.Button(
w,
text="Convertir", command=libras_a_kilos
)
btn_libras.grid(row=1, column=2, padx=5, pady=15, sticky="w")


lbl_res_libras = tk.Label(
w, 
text="", width=10, anchor="w"
)
lbl_res_libras.grid(row=1, column=3, padx=5, pady=15, sticky="w")

#=======================================
# Fila Metros
#=======================================
lbl_metros = tk.Label(
w,
text="Metros"
)
lbl_metros.grid(row=2, column=0, padx=10, pady=15, sticky="w")


txt_metros = tk.Entry(
w,
width=10
)
txt_metros.grid(row=2, column=1, padx=5, pady=15)


btn_metros = tk.Button(
w,
text="Convertir", command=metros_a_km
)
btn_metros.grid(row=2, column=2, padx=5, pady=15, sticky="w")

lbl_res_metros = tk.Label(
w,
text="", width=10, anchor="w"
)
lbl_res_metros.grid(row=2, column=3, padx=5, pady=15, sticky="w")

#=======================================
# Fila Yardas
#=======================================
lbl_yardas = tk.Label(
w,
text="Yardas"
)
lbl_yardas.grid(row=3, column=0, padx=10, pady=15, sticky="w")


txt_yardas = tk.Entry(
w,
width=10
)
txt_yardas.grid(row=3, column=1, padx=5, pady=15)

btn_yardas = tk.Button(
w,
text="Convertir", command=yardas_a_cm
)
btn_yardas.grid(row=3, column=2, padx=5, pady=15, sticky="w")

lbl_res_yardas = tk.Label(
w,
text="", width=10, anchor="w"
)
lbl_res_yardas.grid(row=3, column=3, padx=5, pady=15, sticky="w")

w.mainloop()