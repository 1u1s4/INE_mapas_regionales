import os
import shutil
import subprocess
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors

class Mapa:
    def __init__(self, nombre_archivo: str, datos: pd.DataFrame=pd.DataFrame({}), shape_file: str='regiones/regiones.shp', output_dir: str='output') -> None:
        self.datos = datos
        self.nombre_archivo = nombre_archivo
        self.tracts = gpd.read_file(shape_file)
        self.output_dir = output_dir

        # Crear el directorio si no existe
        os.makedirs(self.output_dir, exist_ok=True)

        # Copiar y renombrar el archivo plantilla.tex al directorio de salida
        shutil.copy('plantilla.tex', os.path.join(self.output_dir, f"{self.nombre_archivo}.tex"))

    def agregar_datos(self, datos_nuevos: list) -> None:
        self.datos = pd.DataFrame({
            'region': ['Región I', 'Región II', 'Región III', 'Región IV', 'Región V', 'Región VI', 'Región VII', 'Región VIII'],
            'nueva_columna': datos_nuevos
        })
        # Crear el archivo datos.tex en la carpeta output con el formato especificado
        with open(os.path.join(self.output_dir, 'datos.tex'), 'w') as file:
            file.write("\\def \\regionUno{" + str(datos_nuevos[0]) + "}\n")
            file.write("\\def \\regionDos{" + str(datos_nuevos[1]) + "}\n")
            file.write("\\def \\regionTres{" + str(datos_nuevos[2]) + "}\n")
            file.write("\\def \\regionCuatro{" + str(datos_nuevos[3]) + "}\n")
            file.write("\\def \\regionCinco{" + str(datos_nuevos[4]) + "}\n")
            file.write("\\def \\regionSeis{" + str(datos_nuevos[5]) + "}\n")
            file.write("\\def \\regionSiete{" + str(datos_nuevos[6]) + "}\n")
            file.write("\\def \\regionOcho{" + str(datos_nuevos[7]) + "}\n")

    def hacer_mapa(self) -> None:
            for reg in self.datos['region']:
                self.tracts.loc[self.tracts['region'] == reg, 'nueva_columna'] = self.datos.loc[self.datos['region'] == reg, 'nueva_columna'].values[0]
            # Define el mapa de colores personalizado
            cmap = colors.LinearSegmentedColormap.from_list("", ['#6363DB', '#3F46BF', '#000080'])

            fig, ax = plt.subplots()  # Crea una figura y ejes con un tamaño específico

            # Desactiva la leyenda, establece el color de borde a blanco y el grosor a 1.5
            self.tracts.plot(column="nueva_columna", cmap=cmap, edgecolor="white", linewidth=0.7, legend=False, ax=ax)
            
            ax.axis('off')  # Desactiva los ejes

            # Guarda la figura en el directorio especificado
            plt.savefig(os.path.join(self.output_dir, f"mapa_sin_anotar.pdf"), format='pdf', dpi=100, bbox_inches='tight')

    def compilar(self):
        # Cambia al directorio de salida
        os.chdir(self.output_dir)

        # Ejecuta el comando para compilar el archivo renombrado
        subprocess.run(['xelatex', '-synctex=1', '-interaction=nonstopmode', f"{self.nombre_archivo}.tex"], check=True)

p = Mapa('mapa_IPC', output_dir='output2')
p.agregar_datos([5.86, 12.4, 7.27, 8.98, 7.85, 8.98, 11.72, 7.54])
p.hacer_mapa()
p.compilar()