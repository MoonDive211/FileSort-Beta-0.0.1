import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# --- Configuración de extensiones ---
formatos = {
    "Documentos": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".pem", ".tsv"],
    "Imagenes": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
    "Ejecutables": [".exe", ".msi", ".pkg", ".deb", ".dmg", ".msix"],
    "Comprimidos": [".zip", ".rar", ".tar", ".gz"],
}

def mover_archivo(archivo, nombre_carpeta, ruta_origen):
    ruta_destino = os.path.join(ruta_origen, nombre_carpeta)
    
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)
        
    try:
        origen = os.path.join(ruta_origen, archivo)
        destino = os.path.join(ruta_destino, archivo)
        shutil.move(origen, destino)
    except Exception as e:
        print(f"❌ Error moviendo {archivo}: {e}")

def organizar(ruta_seleccionada):
    if not ruta_seleccionada:
        messagebox.showwarning("Atención", "Por favor, selecciona una carpeta primero.")
        return

    conteo = 0
    for archivo in os.listdir(ruta_seleccionada):
        ruta_completa = os.path.join(ruta_seleccionada, archivo)
        
        if os.path.isfile(ruta_completa):
            nombre, ext = os.path.splitext(archivo)
            ext = ext.lower()
            encontrado = False
            
            for carpeta, extensiones in formatos.items():
                if ext in extensiones:
                    mover_archivo(archivo, carpeta, ruta_seleccionada)
                    encontrado = True
                    conteo += 1
                    break
            
            if not encontrado and ext != "":
                mover_archivo(archivo, "Otros", ruta_seleccionada)
                conteo += 1
                
    messagebox.showinfo("Éxito", f"Organización completada.\nArchivos movidos: {conteo}")

# --- Funciones de la Interfaz ---
def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        entrada_ruta.delete(0, tk.END)
        entrada_ruta.insert(0, carpeta)

def ejecutar_limpieza():
    ruta = entrada_ruta.get()
    organizar(ruta)

# --- Configuración de la Ventana (GUI) ---
ventana = tk.Tk()
ventana.title("FileSort Pro - Beta 0.0.2")
ventana.geometry("500x250")
ventana.config(padx=20, pady=20)

tk.Label(ventana, text="Selecciona la carpeta a organizar:", font=("Arial", 10, "bold")).pack(pady=10)

# Frame para la entrada y el botón de búsqueda
frame_ruta = tk.Frame(ventana)
frame_ruta.pack(fill="x")

entrada_ruta = tk.Entry(frame_ruta, font=("Arial", 10))
entrada_ruta.pack(side="left", expand=True, fill="x", padx=5)

btn_buscar = tk.Button(frame_ruta, text="Examinar", command=seleccionar_carpeta)
btn_buscar.pack(side="right")

# Botón principal de ejecución
btn_ordenar = tk.Button(ventana, text="🚀 Organizar Archivos", 
                       bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
                       command=ejecutar_limpieza, height=2)
btn_ordenar.pack(pady=30, fill="x")

ventana.mainloop()