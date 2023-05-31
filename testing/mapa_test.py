from colorimapgt import mapa
import random
import pandas as pd

# Crear una instancia de la clase Mapa
m = mapa.Mapa(
    nombre_archivo='miMapa',
    datos=pd.DataFrame({
          'region': ['Región I', 'Región II', 'Región III', 'Región IV', 'Región V', 'Región VI', 'Región VII', 'Región VIII'],
          'valores': random.sample(range(1, 100), 8)
          }),
    color_base='#EB5BB1',
    decimales=0
    )

# Hacer el mapa
m.hacer_mapa()

# Compilar el archivo LaTeX
m.compilar()
