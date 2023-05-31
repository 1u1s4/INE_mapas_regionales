from setuptools import setup, find_packages

setup(
    name='colorimapgt',
    version='0.7.1',
    author='Luis Alfredo Alvarado Rodríguez',
    description='Mapas colorimetricos a nivel regional de Guatemala.',
    long_description='',
    url='https://github.com/1u1s4/INE_mapas_regionales',
    keywords='development, setup, setuptools',
    python_requires='>=3',
    packages=find_packages(),
    py_modules=['mapa'],
    install_requires=[
        'geopandas',
        'matplotlib'
    ],
    package_data={
        'colorimapgt': ['regiones/*', 'plantilla.tex'],
    },
    include_package_data=True,
)