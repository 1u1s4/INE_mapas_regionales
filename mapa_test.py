from mapa import Mapa
import pandas as pd

# Crear una instancia de la clase Mapa
m = Mapa(
    nombre_archivo='miMapa',
    datos=pd.DataFrame({
          'region': ['Región I', 'Región II', 'Región III', 'Región IV', 'Región V', 'Región VI', 'Región VII', 'Región VIII'],
          'valores': [1, 2, 3, 4, 5, 6, 7, 8]
          })
    )

# Hacer el mapa
m.hacer_mapa()

# Compilar el archivo LaTeX
m.compilar()
