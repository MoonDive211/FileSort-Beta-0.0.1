# 🐍 Filesort

> **Filesort** es un script de automatización en Python diseñado para mantener tu escritorio o carpetas de descargas impecables.

El programa escanea un directorio específico y mueve automáticamente los archivos a carpetas organizadas según su extensión (Documentos, Imágenes, Videos, etc.).

---

## ✨ Características

* **🖼️ Interfaz Gráfica (GUI):** No más consola negra. Usa una ventana intuitiva para seleccionar carpetas.

*   **🧠 Organización por Categorías:** Clasifica automáticamente documentos, imagenes, vídeos, música y más.

*   **📂 Seguridad:** Si la carpeta de destino no existe, el script la crea por ti.
*   **❓ Filtro Inteligente:** Los archivos con extensiones no identificadas se mueven a una carpeta llamada `Otros`.

*   **🛡️ Prevención de Errores:** 
    *   Ignora carpetas existentes para evitar bucles.
    *   Manejo de excepciones mediante bloques `try-except` para una ejecución robusta.

---

## 🛠️ Categoría de Organización

El sistema reconoce los siguientes formatos y los agrupa así:


| 📂 Categoría | 🛠️ Extensiones Soportadas |
| :--- | :---: |
| **Documentos** | <kbd>.pdf</kbd> <kbd>.docx</kbd> <kbd>.txt</kbd> <kbd>.pptx</kbd> <kbd>.xlsx</kbd> <kbd>.pem</kbd> <kbd>.tsv</kbd> |
| **Imágenes** | <kbd>.jpg</kbd> <kbd>.jpeg</kbd> <kbd>.png</kbd> |
| **Videos** | <kbd>.mp4</kbd> <kbd>.avi</kbd> <kbd>.mkv</kbd> |
| **Música** | <kbd>.mp3</kbd> <kbd>.wav</kbd> |
| **Ejecutables** | <kbd>.exe</kbd> <kbd>.msi</kbd> <kbd>.pkg</kbd> <kbd>.deb</kbd> <kbd>.dmg</kbd> |
| **Comprimidos** | <kbd>.zip</kbd> <kbd>.rar</kbd> <kbd>.tar</kbd> <kbd>.gz</kbd> |

## 🚀 Como instalar y usar

Sigue estos pasos para poner en marcha **Filesort** en tu equipo:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/MoonDive211/FileSort-Beta-0.0.1
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
*   Módulos internos: `os`, `shutil`, `tkinter`.

---


## 🗺️ Roadmap (Próximas Mejoras)

¡El proyecto sigue en constante desarrollo! (Cuando tenga tiempo libre) 

Estas son las funcionalidades que están en camino:

- [✔] **🎨 Interfaz Gráfica (GUI):** Implementación de una ventana amigable con `Tkinter` para evitar editar el código manualmente.

- [ ] **📋 Sistema de Logs:** Creación de un archivo `.log` para registrar qué archivos se movieron y detectar posibles errores.

- [ ] **⚡ Monitoreo en Tiempo Real:** Ejecución en segundo plano para organizar archivos al instante en cuanto lleguen a la carpeta.

- [ ] **⚙️ Configuración Externa:** Soporte para un archivo `.json` o `.yaml` para que el usuario defina sus propias categorías y extensiones.

---
## 📄 Licencia

Este proyecto es de código abierto bajo la licencia **MIT**. ¡Siéntete libre de usarlo y mejorarlo!
