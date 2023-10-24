#!/bin/bash
main_root='/workspaces/exercise-terminal-challenge'

echo "File, Size, Date" > archivos.csv
# Recorre el directorio y subdirectorios
find "$main_root" -type f | while read -r file; do
    # da nombre del archivo
    file_name=$(basename "$file")
    # da tamaño del archivo
    file_size=$(stat -c %s "$file")
    # da la fecha de modificación formateada en un formato legible
    file_date=$(date -d "@$(stat -c %Y "$file")" "+%d/%m/%Y %H:%M:%S")
    # añade informacion a archivo csv
    echo "$file_name,$file_size,$file_date" >> archivos.csv
done

echo "CSV exported to .csv files"