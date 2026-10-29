#!/usr/bin/env bash

echo "Explorando datos"
date

echo "Tamaño del archivo:"
ls -lh datos/calidad_aire.csv

echo "Observaciones (sin encabezado):"
tail -n +2 datos/calidad_aire.csv | wc -l

echo "Primeras 3 filas:"
head -n 3 datos/calidad_aire.csv

echo "Registros por contaminante:"
tail -n +2 datos/calidad_aire.csv | cut -d',' -f3 | sort | uniq -c | sort -nr

echo "Lineas con Ozone:"
grep -c "Ozone" datos/calidad_aire.csv
