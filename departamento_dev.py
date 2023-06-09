import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.colors as mcolors

def generar_escala_colores(color_hex: str) -> list[str]:
    color_hex = color_hex.lstrip("#")
    color_base = tuple(int(color_hex[i:i+2], 16) / 255.0 for i in range(0, 6, 2))

    # Crea el mapa de colores personalizado que va desde blanco hasta el color base y desde el color base hasta negro
    color_scale = mcolors.LinearSegmentedColormap.from_list(
        "scale", [(1.0, 1.0, 1.0), color_base, (0.0, 0.0, 0.0)]
    )

    # Genera una lista de valores entre 0 y 1
    scale_values = np.linspace(0, 1, 200) # Ajustado para tener en cuenta el color base adicional

    # Utiliza los valores de la escala para obtener los colores correspondientes de la escala de colores
    colors = [mcolors.rgb2hex(color_scale(val)) for val in scale_values]

    return colors[50:100] # Esto también puede necesitar ser ajustado dependiendo de cómo quieras que se vea la escala de colores

tracts = gpd.read_file('departamentos/departamentos.shp')

# Desactiva la leyenda, establece el color de borde a blanco y el grosor a 1.5
escala_de_color = generar_escala_colores("#3F46BF")
cmap = colors.LinearSegmentedColormap.from_list("", escala_de_color)

fig, ax = plt.subplots()  # Crea una figura y ejes con un tamaño específico
tracts.plot(column="departamen", cmap=cmap, edgecolor="white", linewidth=0.7, legend=False, ax=ax)

# Cálcula los centroides y los muestra en el gráfico
centroides = tracts.geometry.centroid
centroides.plot(ax=ax, color='red', marker='o', markersize=5)

ax.axis('off')  # Desactiva los ejes

# Guarda la figura como un PDF
plt.savefig('mi_mapa.pdf', format='pdf')

plt.show()
