import tkinter as tk
from tkinter import messagebox

# Datos de ejemplo
peliculas = {
    "Matrix Resurrections": ["15:00", "18:00", "21:00"],
    "Duna Parte II": ["14:00", "17:00", "20:00"],
    "Intensamente 2": ["12:00", "16:00", "19:00"]
}

butacas_filas = 5
butacas_columnas = 8

reservas = {}

class CineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 Cine Virtual")
        self.pelicula = tk.StringVar()
        self.horario = tk.StringVar()
        self.butacas_seleccionadas = set()

        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.root, text="Seleccione una película:").grid(row=0, column=0, sticky='w')
        self.menu_peliculas = tk.OptionMenu(self.root, self.pelicula, *peliculas.keys(), command=self.actualizar_horarios)
        self.menu_peliculas.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Seleccione horario:").grid(row=1, column=0, sticky='w')
        self.menu_horarios = tk.OptionMenu(self.root, self.horario, "")
        self.menu_horarios.grid(row=1, column=1, padx=10, pady=5)

        self.butacas_frame = tk.Frame(self.root)
        self.butacas_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.btn_reservar = tk.Button(self.root, text="Reservar Butacas 🎟️", command=self.reservar)
        self.btn_reservar.grid(row=3, column=0, columnspan=2, pady=10)

    def actualizar_horarios(self, seleccion):
        horarios = peliculas[seleccion]
        self.horario.set("")
        self.menu_horarios['menu'].delete(0, 'end')
        for h in horarios:
            self.menu_horarios['menu'].add_command(label=h, command=tk._setit(self.horario, h))
        self.actualizar_butacas()

    def actualizar_butacas(self):
        for widget in self.butacas_frame.winfo_children():
            widget.destroy()

        self.butacas_seleccionadas.clear()
        pelicula = self.pelicula.get()
        horario = self.horario.get()
        clave = (pelicula, horario)
        reservadas = reservas.get(clave, set())

        for fila in range(butacas_filas):
            for col in range(butacas_columnas):
                nombre_butaca = f"{chr(65+fila)}{col+1}"
                estado = "normal"
                if nombre_butaca in reservadas:
                    estado = "disabled"

                btn = tk.Checkbutton(
                    self.butacas_frame, text=nombre_butaca,
                    command=lambda b=nombre_butaca: self.seleccionar_butaca(b)
                )
                btn.grid(row=fila, column=col)
                if estado == "disabled":
                    btn.configure(state="disabled")

    def seleccionar_butaca(self, nombre):
        if nombre in self.butacas_seleccionadas:
            self.butacas_seleccionadas.remove(nombre)
        else:
            self.butacas_seleccionadas.add(nombre)

    def reservar(self):
        if not self.pelicula.get() or not self.horario.get():
            messagebox.showwarning("Falta selección", "Debe seleccionar una película y un horario.")
            return
        if not self.butacas_seleccionadas:
            messagebox.showwarning("Sin butacas", "Seleccione al menos una butaca.")
            return

        clave = (self.pelicula.get(), self.horario.get())
        reservas.setdefault(clave, set()).update(self.butacas_seleccionadas)

        messagebox.showinfo("Reserva confirmada", f"Reservaste: {', '.join(sorted(self.butacas_seleccionadas))}")
        self.actualizar_butacas()

if __name__ == "__main__":
    root = tk.Tk()
    app = CineApp(root)
    root.mainloop()
