# 🐍 Filesort

> **Filesort** es un script de automatización en Python diseñado para mantener tu escritorio o carpetas de descargas impecables.

El programa escanea un directorio específico y mueve automáticamente los archivos a carpetas organizadas según su extensión (Documentos, Imágenes, Videos, etc.).

---

## ✨ Características

*   **🧠 Clasificación Inteligente:** Clasifica archivos en categorías predefinidas de forma automática.
*   **📂 Gestión Dinámica de Carpetas:** Si la carpeta de destino no existe, el script la crea por ti.
*   **❓ Manejo de Desconocidos:** Los archivos con extensiones no identificadas se mueven a una carpeta llamada `Otros`.

*   **🛡️ Prevención de Errores:** 
    *   Ignora carpetas existentes para evitar bucles.
    *   Manejo de excepciones mediante bloques `try-except` para una ejecución robusta.

---

## 🛠️ Cómo funciona


| 📂 Categoría | 🛠️ Extensiones Soportadas |
| :--- | :---: |
| **Documentos** | <kbd>.pdf</kbd> <kbd>.docx</kbd> <kbd>.txt</kbd> <kbd>.pptx</kbd> <kbd>.xlsx</kbd> <kbd>.pem</kbd> <kbd>.tsv</kbd> |
| **Imágenes** | <kbd>.jpg</kbd> <kbd>.jpeg</kbd> <kbd>.png</kbd> |
| **Videos** | <kbd>.mp4</kbd> <kbd>.avi</kbd> <kbd>.mkv</kbd> |
| **Música** | <kbd>.mp3</kbd> <kbd>.wav</kbd> |
| **Ejecutables** | <kbd>.exe</kbd> <kbd>.msi</kbd> <kbd>.pkg</kbd> <kbd>.deb</kbd> <kbd>.dmg</kbd> |
| **Comprimidos** | <kbd>.zip</kbd> <kbd>.rar</kbd> <kbd>.tar</kbd> <kbd>.gz</kbd> |

## 🚀 Instalación y Uso

Sigue estos pasos para poner en marcha **Filesort** en tu equipo:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/filesort.git
   cd filesort
   ```

2. **Configura tu ruta:**
   Abre el archivo `main.py` y modifica la variable `ruta` con la dirección de la carpeta que deseas organizar:
   ```python
   # Ejemplo de configuración
   ruta = r"C:\Usuarios\tu-usuario\Downloads"
   ```

3. **Ejecuta el script:**
   ```bash
   python main.py
   ```

---

## 💻 Requisitos

No necesitas instalar librerías externas, ya que el script utiliza la **biblioteca estándar** de Python:

*   **Python 3.x** instalado.
*   Módulos internos: `os`, `shutil`.

---

## 📄 Licencia

Este proyecto es de código abierto bajo la licencia **MIT**. ¡Siéntete libre de usarlo y mejorarlo!
