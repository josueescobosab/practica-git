import numpy as np


def resumen(valores):
    """Calcula percentiles, media, máximo y mínimo de una Serie o arreglo."""
    percentiles = [10, 30, 50, 70, 80, 90, 95, 99]
    resultado = {}

    for p in percentiles:
        resultado[f"p{p}"] = float(np.percentile(valores, p))

    resultado["media"] = float(valores.mean())
    resultado["max"] = float(valores.max())
    resultado["min"] = float(valores.min())

    resultado["n"] = int(len(valores))

    return resultado


class Analizador:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def rango(self):
        return max(self.datos) - min(self.datos)