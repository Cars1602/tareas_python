import tkinter as tk
from tkinter import ttk

class TecladoNumerico:
    def __init__(self, root):
        self.root = root
        self.root.title("Teclado Numérico")
        self.root.geometry("300x400")
        
        # Variable para almacenar la entrada
        self.entrada = tk.StringVar()
        
        # Crear widgets
        self.crear_widgets()
    
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Display para mostrar la entrada
        display = ttk.Entry(main_frame, textvariable=self.entrada, 
                           font=('Arial', 18), justify='right', state='readonly')
        display.pack(fill=tk.X, pady=10)
        
        # Frame para los botones numéricos
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.BOTH, expand=True)
        
        # Distribución de botones (3x3 + fila extra)
        botones = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.', 'C'
        ]
        
        # Crear botones
        for i, texto in enumerate(botones):
            row = i // 3
            col = i % 3
            
            # Botón especial para el cero (más ancho)
            if texto == '0':
                btn = ttk.Button(btn_frame, text=texto, 
                                command=lambda t=texto: self.presionar_tecla(t))
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
            else:
                btn = ttk.Button(btn_frame, text=texto, 
                                command=lambda t=texto: self.presionar_tecla(t))
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        # Botón de borrado (Backspace)
        btn_borrar = ttk.Button(btn_frame, text="⌫", 
                              command=self.borrar_ultimo)
        btn_borrar.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
        
        # Configurar el grid para que los botones se expandan
        for i in range(4):
            btn_frame.rowconfigure(i, weight=1)
        for i in range(3):
            btn_frame.columnconfigure(i, weight=1)
        
        # Botón de resultado (fuera del grid numérico)
        btn_igual = ttk.Button(main_frame, text="=", 
                              command=self.calcular_resultado)
        btn_igual.pack(fill=tk.X, pady=5)
    
    def presionar_tecla(self, tecla):
        if tecla == 'C':
            self.entrada.set('')
        else:
            current = self.entrada.get()
            self.entrada.set(current + tecla)
    
    def borrar_ultimo(self):
        current = self.entrada.get()
        self.entrada.set(current[:-1])
    
    def calcular_resultado(self):
        try:
            expresion = self.entrada.get()
            if expresion:
                resultado = eval(expresion)
                self.entrada.set(str(resultado))
        except Exception as e:
            self.entrada.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = TecladoNumerico(root)
    root.mainloop()