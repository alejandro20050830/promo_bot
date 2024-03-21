import os
import zipfile

def comprimir_archivos_session(carpeta_origen = os.getcwd(), archivo_destino = 'db/saved_sessions.zip'):
    """
    Comprime todos los archivos con extensión .session en un archivo ZIP.

    Args:
        carpeta_origen (str): Ruta de la carpeta que contiene los archivos .session.
        archivo_destino (str): Ruta del archivo ZIP de destino.
    """
    with zipfile.ZipFile(archivo_destino, 'w') as archivo_zip:
        for nombre_archivo in os.listdir(carpeta_origen):
            if nombre_archivo.endswith('.session'):
                ruta_completa = os.path.join(carpeta_origen, nombre_archivo)
                archivo_zip.write(ruta_completa, arcname=nombre_archivo)

def descomprimir_archivo_zip(archivo_zip= 'db/saved_sessions.zip', carpeta_destino = os.getcwd()):
    """
    Descomprime un archivo ZIP en una carpeta específica y luego lo elimina.

    Args:
        archivo_zip (str): Ruta del archivo ZIP a descomprimir.
        carpeta_destino (str): Ruta de la carpeta donde se guardarán los archivos descomprimidos.
    """
    with zipfile.ZipFile(archivo_zip, 'r') as archivo_zip_:
        archivo_zip_.extractall(carpeta_destino)

    # Eliminar el archivo ZIP después de descomprimirlo
    #os.remove(archivo_zip)

# Ejemplo de uso:
#carpeta_origen = os.getcwd()
#archivo_destino = 'cache/saved_sessions.zip'
#carpeta_destino = os.getcwd()

#comprimir_archivos_session()
#descomprimir_archivo_zip()
