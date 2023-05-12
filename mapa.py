import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors

class Mapa:
    def __init__(self, nombre_archivo: str, datos: pd.DataFrame=pd.DataFrame({}), shape_file: str='regiones/regiones.shp') -> None:
        self.datos = datos
        self.nombre_archivo = nombre_archivo
        self.tracts = gpd.read_file(shape_file)

    def agregar_datos(self, datos_nuevos: list) -> None:
        self.datos = pd.DataFrame({
            'region': ['Región I', 'Región II', 'Región III', 'Región IV', 'Región V', 'Región VI', 'Región VII', 'Región VIII'],
            'nueva_columna': datos_nuevos
        })

    def hacer_mapa(self) -> None:
        for reg in self.datos['region']:
            self.tracts.loc[self.tracts['region'] == reg, 'nueva_columna'] = self.datos.loc[self.datos['region'] == reg, 'nueva_columna'].values[0]
        # Define el mapa de colores personalizado
        cmap = colors.LinearSegmentedColormap.from_list("", ['#6363DB', '#3F46BF', '#000080'])

        fig, ax = plt.subplots(figsize=(13.5, 10))  # Crea una figura y ejes con un tamaño específico

        # Desactiva la leyenda, establece el color de borde a blanco y el grosor a 1.5
        self.tracts.plot(column="nueva_columna", cmap=cmap, edgecolor="white", linewidth=1.5, legend=False, ax=ax)
        ax.axis('off')  # Desactiva los ejes

        plt.savefig(f"{self.nombre_archivo}.pdf", format='pdf', bbox_inches='tight')  # Guarda la figura como PDF
        plt.show()  # Muestra la figura


p = Mapa('hola')
p.agregar_datos([61, 770, 1168, 775, 863, 1722, 673, 648])
p.hacer_mapa()
