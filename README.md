![ideuy-logo]( http://drive.google.com/uc?export=view&id=1wUy_yiXHLJo2uYeGEpvhaj73yI8eM1ik)
# Ideuy-py

![badge-license](https://img.shields.io/badge/license-BSD%202-green)
![badge-version](https://img.shields.io/badge/version-0.1.0-yellow)
![badge-build](https://img.shields.io/badge/build%20with-python-yellow)

# Contenido
1. [Resumen](#Resumen)
2. [Guía de instalación](#Guía-de-instalación)
4. []()
5. [Contacto](#Contacto)
6. [Contribución](#Contribución)
7. [Licencia](#Licencia)


# Resumen

Herramienta y paquete de Python que facilita la descarga programática de las
ortoimágenes del vuelo fotogramétrico, disponibles desde el Visualizador online
de la [Infraestructura de Datos Espaciales de Uruguay
(IDEuy)](https://www.gub.uy/infraestructura-datos-espaciales/).

## Guía de instalación

El paquete se puede instalar con pip, ejecutando desde una terminal:

```
pip install --user ideuy
```

## Uso

### Scripts de consola disponibles

* `ideuy_filter`: Filtra un shapefile de grilla con otro shapefile de Áreas de Interés (AOI).
* `ideuy_download_images`: Descarga las imágenes del vuelo basado en un shapefile de grilla.

## Desarrollo

Crear un entorno virtual e instalar el paquete con pip en modo desarrollo, por ejemplo:

```
virtualenv -p python3 .venv/
source .venv/bin/activate
pip install -e .
```
## Tecnologías utilizadas
   - [Python](https://www.python.org/)

## Contacto

En caso de consultas sobre este paquete, IDEUY o contactos de prensa puede dirigirse a munshkr@gmail.com. 

## Contribución

## Licencia

Ver [LICENSE.txt](LICENSE.txt).
