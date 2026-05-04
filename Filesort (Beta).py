"""
proyecto Filesort

este programa podrá mover automaticamente archivos a carpetas especificas
segun su extensión

"""

import os
import shutil

# Definir la ruta a organizar

ruta = r"C:\Users\ma.borquezm\Desktop\Prueba Filesort"

#Diccionario de extensiones y carpetas

formatos = {
    "Documentos": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".pem", ".tsv"],
    "Imagenes": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
    "Ejecutables": [".exe", ".msi", ".pkg", ".deb", ".dmg", ".msix"],
    "Comprimidos": [".zip", ".rar", ".tar", ".gz"],
}

def organizar():
    
    #Lista los elementos en la ruta
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)
    
    #filtra solo archivos (Ignora carpetas ya creadas)    
        if os.path.isfile(ruta_completa):
            nombre, ext = os.path.splitext(archivo)
            ext = ext.lower() # Convertir la extensión a minúsculas para comparación
            
            encontrado = False #Variable de control para verificar si se encontró una extensión válida
            
            
        #Proceso N°1. Busca en el diccionario si la extensión del archivo coincide con alguna de las extensiones listadas
        for carpeta, extensiones in formatos.items():
                if ext.lower() in extensiones:
                    mover_archivo(archivo, carpeta)
                    encontrado = True
                    break # Salir del ciclo si ya se encontró un archivo
            
        #Proceso N°2. Si no se encuentra una extensión válida, mover el archivo a la carpeta "Otros"
        if not encontrado and ext != "":
            mover_archivo(archivo, "Otros")
            
            
def mover_archivo(archivo, nombre_carpeta):
    ruta_carpeta = os.path.join(ruta, nombre_carpeta)
        
      #Crear la carpeta si no existe
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        
    #Mover el archivo a la carpeta correspondiente
    try:
        #Se usa shutil.move para mover el archivo a la carpeta destino, usamos ruta para evitar errores de origen y destino
        origen = os.path.join(ruta, archivo)
        destino = os.path.join(ruta_carpeta, archivo)
        shutil.move(origen, destino)
        print(f"✅ Movido: {archivo} -> {nombre_carpeta}")
    except Exception as e:
        print(f"❌ Error moviendo {archivo}: {e}")
        
if __name__ == "__main__":
    organizar()
    print("Organización completada.")