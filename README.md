# Texto_a_voz_con_Python
Esta aplicación está diseñada para convertir texto en archivos de audio utilizando la tecnología 
de síntesis de voz de Google (gTTS). Puede procesar archivos locales de texto o texto obtenido 
de enlaces web, tener en cuenta que esto último es utilizando la tecnología newspaper la cual puede
contar con errores en algunas webs y no tener éxito al substraer información.

Instalación
Asegúrate de tener Python 3.x instalado en tu sistema.
Instala las dependencias del proyecto utilizando pip:

pip install 
gtts 
newspaper3k 
googletrans==4.0.0-rc1

Estructura del Proyecto
main.py: El script principal que contiene la lógica de la aplicación.
outputs/: Carpeta donde se guardan los archivos de audio generados.
textos/: Carpeta opcional donde se almacenan los archivos de texto para su conversión.

Uso
-   Ejecuta el script main.py.
-   Selecciona el idioma de salida y el origen del texto (local u online).
-   Si seleccionas un archivo local, se abrirá un cuadro de diálogo para que selecciones el archivo 
    (se debe de minimizar el editor de código).
-   Si seleccionas un enlace web, ingresa la URL del texto.
-   El texto será traducido y convertido a audio.
-   El archivo de audio resultante se guardará en la carpeta outputs.
-   Reproduce el archivo de audio automáticamente tras finalizar.

Este README proporciona una visión general de la aplicación, incluyendo cómo instalarla, cómo usarla 
y cómo contribuir al proyecto. Puedes personalizarlo según tus necesidades específicas.

Desarrollador:
Mi nombre es David Rivas, Ingeniero de Sistemas, espero que te guste esta aplicación
se trata de mi primer proyecto programado en python, si deseas contactar conmigo, puedes hacerlo 
por medio de los siguientes contactos:

Correcto: ing.davidrivas96@gmail.com
WhatsApp: +58 4246903020

