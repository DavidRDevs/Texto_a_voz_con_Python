"""Aplicación orientada a convertir un texto a voz utilizando gTTS para realizar la conversión
y os para abrir los archivos en caso de que se encuentren de manera local y luego
guardar el archivo resultante del proceso en una carpeta llamada outputs"""
# Imports Built-in:
import os
from tkinter import filedialog
from datetime import datetime

# Imports instalados:
from gtts import gTTS
from gtts import gTTSError
from newspaper import Article
from newspaper import ArticleException
from googletrans import Translator


def obtener_idioma_usuario():
    """Función para obtener el idioma seleccionado por el usuario"""
    while True:
        # Se genera un bucle dentro de otro bucle para que repita la consulta de las
        # opciones en caso de un error
        bucle = True
        while bucle:
            print("--------------------")
            print("""Seleccione el lenguaje del documento que desea convertir:
                1.- Español españa (es-ES)
                2.- Español EEUU (es-US)
                3.- Ingles (en-US)
                00.- Salir / Exit""")

            seleccion = input(
                "Seleccione el idioma del documento que desea convertir: ")

            if seleccion in ["1", "2", "3", "0", "00"]:
                if seleccion == "1":
                    return "es"
                elif seleccion == "2":
                    return "es"
                elif seleccion == "3":
                    return "en"
                elif seleccion == "00" or seleccion == "0":
                    print("Saliendo del programa, hasta luego!")
                    exit()  # Salir del programa
            else:
                print("Ingreso un valor no valido respecto al idioma. Intente de nuevo")


def obtener_origen_archivo():
    """Función para obtener el origen del archivo seleccionado por el usuario"""
    while True:
        # Se genera un bucle dentro de otro bucle para que repita la consulta de las
        # opciones en caso de un error
        bucle = True
        while bucle:
            print("--------------------")
            print("""Seleccione el origen de archivo que desea convertir:
            1.- Local (En su dispositivo)
            2.- Online (Algun archivo web)
            00.- Salir / Exit""")

            seleccion = input(
                "Seleccione el origen del archivo que desea convertir: ")
            if seleccion in ["1", "2", "0", "00"]:
                if seleccion == "1":
                    return "local"
                elif seleccion == "2":
                    return "online"
                elif seleccion == "00" or seleccion == "0":
                    print("Saliendo del programa, hasta luego!")
                    exit()  # Salir del programa
            else:
                print("Ingreso un valor no valido respecto al origen del archivo.")


def convertir_archivo_a_voz(file, nombre, idioma):
    """Función encargada de realizar la conversión de texto a voz desde un directorio local"""
    try:
        # se apertura el archivo encontrado en modo lectura
        with open(file, "r", encoding="utf-8") as file:
            print("Archivo encontrado, generando archivo de audio...")
            # se reemplazan los saltos de linea por un simple espacio para mejorar la lectura
            text = file.read().replace("\n", " ")
            # se realiza la traduccion del texto segun el lenguaje seleccionado por el usuario
            traduccion = Translator()
            traduccion_obj = traduccion.translate(text, dest=idioma)
            textofinal = str(traduccion_obj.text)
            # Luego de obtener el texto traducido, se pasa por gTTS para converir en audio
            conversion = gTTS(text=textofinal, lang=idioma, slow=False)

            conversion.save(f"Texto_a_voz/outputs/Conversión_{nombre}.mp3")

            reproducir_audio(nombre)

    except FileNotFoundError as e:
        print(f"""ERROR: Archivo {nombre} no encontrado: {e}""")
    except Exception as e:
        print(f"ERROR inesperado: {e}")


def convertir_enlace_a_voz(texto, nombre, idioma):
    """Función encargada de realizar la conversión de texto a voz desde un enlace web"""
    try:
        print("Texto encontrado, generando archivo de audio...")
        # se realiza la traduccion del texto segun el lenguaje seleccionado por el usuario
        traduccion = Translator()
        traduccion_obj = traduccion.translate(texto, dest=idioma)
        textofinal = str(traduccion_obj.text)
        # Luego de obtener el texto traducido, se pasa por gTTS para converir en audio
        conversion = gTTS(text=textofinal, lang=idioma, slow=False)

        conversion.save(f"Texto_a_voz/outputs/Conversión_{nombre}.mp3")

        reproducir_audio(nombre)

    except FileNotFoundError as e:
        print(f"""ERROR: Archivo {nombre} no encontrado: {e}""")
    except gTTSError as e:
        print("Error en gTTS:", e)

    except Exception as e:
        print(f"ERROR inesperado: {e}")


def reproducir_audio(nombre_archivo):
    """Función para reproducir archivo de audio recien generado"""
    print("Archivo creado con éxito, reproduciendo...")
    os.system(f"start Texto_a_voz/outputs/conversion_{nombre_archivo}.mp3")
    print("¡Reproducción exitosa!")
    print("--------------------")


def solicitar_archivo_a_convertir():
    """Funcion encargada de solicitar el archivo o enlace al usuario para posteriormente
    pasarlo por la funcion de convertir_texto_a_voz para convertirlo en un archivo mp3"""
    try:
        while True:
            # Se llama las siguientes funciones para tener la informacion necesaria y
            # poder llamar en ultima instancia la funcion de generacion de audio
            idioma = obtener_idioma_usuario()
            seleccion = obtener_origen_archivo()
            # Se trabaja de manera distinta en un caso respecto a otro
            # En el caso de directorio local, se utiliza el modulo tkinter
            if seleccion == "local":
                print(
                    "Minimice el editor de codigo para poder seleccionar el archivo...")
                directorio = filedialog.askopenfilename()
                # directorio de ejemplo = "Texto_a_voz/textos/python.txt"
                sin_barras = directorio.split("/")
                sin_extencion = sin_barras[-1].split(".")
                nombre_archivo = sin_extencion[0]
                convertir_archivo_a_voz(directorio, nombre_archivo, idioma)

            # En el caso de una direccion web, se utiliza el modulo newspaper
            elif seleccion == "online":
                enlace = input(
                    "Ingrese por favor el enlace de la web que desea convertir: ")
                # webs de ejemplo:
                # http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/
                # https://www.bbc.com/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics
                # https://ultimasnoticias.com.ve/noticias/miranda/inaugurada-escuela-para-productores-de-cacao-en-rio-chico/
                try:
                    # Inicializar el objeto Article
                    article = Article(enlace)
                    # Descargar y parsear el artículo con codificación UTF-8
                    article.download()
                    article.parse()
                    # Obtener el texto del artículo
                    texto = article.text.encode('utf-8').decode('utf-8')
                    nombre_archivo = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
                    convertir_enlace_a_voz(texto, nombre_archivo, idioma)
                except ArticleException as e:
                    print(
                        f"""\tERROR: Ocurrio un problema al acceder a la web: {e}""")
                except Exception as e:
                    print("--------------------")
                    print(f"""\tERROR: Ocurrio un error inesperado: {e}""")
                    print("--------------------")
                    return

            else:
                print(
                    "Ingreso un valor no valido, el programa se cerrara.")
                return  # Salir del programa

            respuesta = input("¿Desea convertir otro archivo? (si/no): ")
            if respuesta.lower() != 'si':
                print("Saliendo del programa, hasta luego!")
                return  # Salir del programa

    except ValueError:
        print("ERROR: Ingreso un valor no valido, intente de nuevo.")
    except Exception as e:
        print(f"ERROR inesperado: {e}")


solicitar_archivo_a_convertir()
