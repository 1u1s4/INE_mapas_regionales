import os
import shutil
import subprocess
import pkg_resources
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors

class Mapa:
    def __init__(self, nombre_archivo: str, datos: pd.DataFrame=pd.DataFrame({}), output_dir: str='output') -> None:
        self.datos = datos
        self.nombre_archivo = nombre_archivo
        self.tracts = gpd.read_file(pkg_resources.resource_filename(__name__, 'regiones/regiones.shp'))
        self.output_dir = output_dir

        # Crear el directorio si no existe
        os.makedirs(self.output_dir, exist_ok=True)

        # Copiar y renombrar el archivo plantilla.tex al directorio de salida
        shutil.copy(pkg_resources.resource_filename(__name__, 'plantilla.tex'), os.path.join(self.output_dir, f"{self.nombre_archivo}.tex"))

    def agregar_datos(self, datos_nuevos: list) -> None:
        self.datos = pd.DataFrame({
            'region': ['Región I', 'Región II', 'Región III', 'Región IV', 'Región V', 'Región VI', 'Región VII', 'Región VIII'],
            'valores': datos_nuevos
        })

    def hacer_mapa(self) -> None:
        for reg in self.datos['region']:
            self.tracts.loc[self.tracts['region'] == reg, 'valores'] = self.datos.loc[self.datos['region'] == reg, 'valores'].values[0]
        # Define el mapa de colores personalizado
        cmap = colors.LinearSegmentedColormap.from_list("", ['#6363DB', '#3F46BF', '#000080'])

        fig, ax = plt.subplots()  # Crea una figura y ejes con un tamaño específico

        # Desactiva la leyenda, establece el color de borde a blanco y el grosor a 1.5
        self.tracts.plot(column="valores", cmap=cmap, edgecolor="white", linewidth=0.7, legend=False, ax=ax)
        
        ax.axis('off')  # Desactiva los ejes

        # Guarda la figura en el directorio especificado
        plt.savefig(os.path.join(self.output_dir, f"mapa_sin_anotar.pdf"), format='pdf', dpi=100, bbox_inches='tight')

        # Crear el archivo datos.tex en la carpeta output con el formato especificado
        with open(os.path.join(self.output_dir, 'datos.tex'), 'w') as file:
            datos = self.datos['valores'].values
            file.write("\\def \\regionUno{" + str(datos[0]) + "}\n")
            file.write("\\def \\regionDos{" + str(datos[1]) + "}\n")
            file.write("\\def \\regionTres{" + str(datos[2]) + "}\n")
            file.write("\\def \\regionCuatro{" + str(datos[3]) + "}\n")
            file.write("\\def \\regionCinco{" + str(datos[4]) + "}\n")
            file.write("\\def \\regionSeis{" + str(datos[5]) + "}\n")
            file.write("\\def \\regionSiete{" + str(datos[6]) + "}\n")
            file.write("\\def \\regionOcho{" + str(datos[7]) + "}\n")

    def compilar(self):
        # Guarda el directorio de trabajo original
        original_dir = os.getcwd()

        # Cambia al directorio de salida
        os.chdir(self.output_dir)

        # Ejecuta el comando para compilar el archivo renombrado
        subprocess.run(['xelatex', '-synctex=1', '-interaction=nonstopmode', f"{self.nombre_archivo}.tex"], check=True)

        # Vuelve al directorio de trabajo original
        os.chdir(original_dir)
