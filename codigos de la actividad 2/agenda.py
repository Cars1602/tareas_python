import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")
        
        # Lista para almacenar eventos
        self.eventos = []
        
        # Frame principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Widgets
        self.crear_widgets()
        
        # Cargar eventos de ejemplo (opcional)
        self.cargar_eventos_ejemplo()
        
    def crear_widgets(self):
        # Etiquetas y campos de entrada
        ttk.Label(self.main_frame, text="Título:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.titulo_entry = ttk.Entry(self.main_frame, width=40)
        self.titulo_entry.grid(row=0, column=1, columnspan=2, pady=5, sticky=tk.W)
        
        ttk.Label(self.main_frame, text="Descripción:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.descripcion_entry = ttk.Entry(self.main_frame, width=40)
        self.descripcion_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky=tk.W)
        
        ttk.Label(self.main_frame, text="Fecha (dd/mm/aaaa):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.fecha_entry = ttk.Entry(self.main_frame, width=15)
        self.fecha_entry.grid(row=2, column=1, pady=5, sticky=tk.W)
        self.fecha_entry.insert(0, datetime.now().strftime("%d/%m/%Y"))
        
        ttk.Label(self.main_frame, text="Hora (hh:mm):").grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
        self.hora_entry = ttk.Entry(self.main_frame, width=8)
        self.hora_entry.grid(row=2, column=3, pady=5, sticky=tk.W)
        self.hora_entry.insert(0, "12:00")
        
        # Botones
        ttk.Button(self.main_frame, text="Agregar Evento", command=self.agregar_evento).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Eliminar Evento", command=self.eliminar_evento).grid(row=3, column=2, columnspan=2, pady=10)
        
        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.main_frame, columns=("Título", "Descripción", "Fecha", "Hora"), show="headings")
        self.tree.grid(row=4, column=0, columnspan=4, sticky=tk.NSEW, pady=10)
        
        # Configurar columnas
        self.tree.heading("Título", text="Título")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        
        self.tree.column("Título", width=120)
        self.tree.column("Descripción", width=180)
        self.tree.column("Fecha", width=80)
        self.tree.column("Hora", width=60)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=4, column=4, sticky=tk.NS)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Configurar expansión
        self.main_frame.rowconfigure(4, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
    
    def cargar_eventos_ejemplo(self):
        eventos_ejemplo = [
            {"titulo": "Reunión de trabajo", "descripcion": "Planificación del proyecto X", "fecha": "15/06/2023", "hora": "09:00"},
            {"titulo": "Cita médica", "descripcion": "Control anual", "fecha": "20/06/2023", "hora": "16:30"},
        ]
        for evento in eventos_ejemplo:
            self.eventos.append(evento)
            self.tree.insert("", tk.END, values=(evento["titulo"], evento["descripcion"], evento["fecha"], evento["hora"]))
    
    def agregar_evento(self):
        titulo = self.titulo_entry.get()
        descripcion = self.descripcion_entry.get()
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        
        if not titulo:
            messagebox.showerror("Error", "El título es obligatorio")
            return
        
        try:
            # Validar formato de fecha
            datetime.strptime(fecha, "%d/%m/%Y")
            # Validar formato de hora
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora incorrecto")
            return
        
        nuevo_evento = {
            "titulo": titulo,
            "descripcion": descripcion,
            "fecha": fecha,
            "hora": hora
        }
        
        self.eventos.append(nuevo_evento)
        self.tree.insert("", tk.END, values=(titulo, descripcion, fecha, hora))
        
        # Limpiar campos
        self.titulo_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)
        self.fecha_entry.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.hora_entry.delete(0, tk.END)
        self.hora_entry.insert(0, "12:00")
        
        messagebox.showinfo("Éxito", "Evento agregado correctamente")
    
    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showerror("Error", "Seleccione un evento para eliminar")
            return
        
        item = self.tree.item(seleccion[0])
        titulo = item['values'][0]
        
        # Buscar y eliminar el evento de la lista
        for i, evento in enumerate(self.eventos):
            if evento["titulo"] == titulo:
                del self.eventos[i]
                break
        
        self.tree.delete(seleccion[0])
        messagebox.showinfo("Éxito", "Evento eliminado correctamente")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()