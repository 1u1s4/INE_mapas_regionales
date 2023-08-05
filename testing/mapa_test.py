from colorimapgt import Mapa
import random
import pandas as pd

# Crear una instancia de la clase Mapa
m = Mapa(
    nombre_archivo='miMapa',
    datos=pd.DataFrame({
          'region': ['Región I', 'Región II', 'Región III', 'Región IV', 'Región V', 'Región VI', 'Región VII', 'Región VIII'],
          'valor': [2804, 1166, 1628, 1099, 1321, 3622, 820, 968]
          }),
    precision=0
    )

# Hacer el mapa
m.hacer_mapa()

# Compilar el archivo LaTeX
m.compilar()

m.limpiar()