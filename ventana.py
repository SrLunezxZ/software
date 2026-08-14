import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi primer formulario")
tk.Label(ventana, text="Nombre:").pack()
tk.Entry(ventana).pack()
tk.Button(ventana, text="Aceptar").pack()
ventana.mainloop