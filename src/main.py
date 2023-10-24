# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
import os
import pandas as pd
from datetime import datetime

main_root = '/workspaces/exercise-terminal-challenge'


def lista_archivos(ruta):
    archivos = []
    for carpeta_actual, subcarpeta, archivos_carpeta in os.walk(main_root):
        for archivo in archivos_carpeta:
            archivos.append(os.path.join(carpeta_actual, archivo))
    return archivos

def tamaño_archivo(archivos):
    tamaños = []
    for archivo in archivos:
        tamaño = os.path.getsize(archivo)
        tamaños.append(tamaño)
    return tamaños

def obtener_dates(archivos):
    date_archivos = []
    for archivo in archivos:
        fecha_modificacion = os.path.getmtime(archivo)
        date_archivos.append(datetime.utcfromtimestamp(fecha_modificacion).strftime('%d/%m/%Y %H:%M:%S'))
    return date_archivos

all_archivos = lista_archivos(main_root)
archivo_pesos = tamaño_archivo(all_archivos)
date_archivos = obtener_dates(all_archivos)

archivo_pd = pd.DataFrame({'Archivos': all_archivos, 'Size': archivo_pesos, 'Fechas': date_archivos})

print(archivo_pd)

archivo_pd.to_csv('/workspaces/exercise-terminal-challenge/src/tabla.csv', index= False)



# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV

main_root='/workspaces/exercise-terminal-challenge'

