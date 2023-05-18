from colorimapgt import mapa
import pandas as pd

# Crear una instancia de la clase Mapa
m = mapa.Mapa(
    nombre_archivo='miMapa',
    datos=pd.DataFrame({
          'region': ['Región I', 'Región II', 'Región III', 'Región IV', 'Región V', 'Región VI', 'Región VII', 'Región VIII'],
          'valores': [1, 2, 3, 4, 5, 6, 7, 8]
          }),
    color_base='#EB5BB1'
    )

# Hacer el mapa
m.hacer_mapa()

# Compilar el archivo LaTeX
m.compilar()
