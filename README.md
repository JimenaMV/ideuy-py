*Esta herramienta digital forma parte del catálogo de herramientas del **Banco Interamericano de Desarrollo**. Puedes conocer más sobre la iniciativa del BID en [code.iadb.org](https://code.iadb.org)*

<br>

<p align="center">
<img  height="200"  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCtXkOdL-iKuv-Y8wMZA8piyiHTkrzPlMPnA&usqp=CAU">
</p>

<p align="center">
<img  src="https://img.shields.io/badge/license-BSD%202-green">
<img  src="https://img.shields.io/badge/version-0.1.0-yellow">
<img  src="https://img.shields.io/badge/build%20with-python-yellow">
</p>

<p  align="center">
• <a  href="#-introducción">Introducción</a> •
<a  href="#notebook-guía-de-instalación-y-uso">Guía de instalación y uso</a> •
<a  href="#chart_with_downwards_trend-datos-abiertos">Datos abiertos</a> •
<a  href="#memo-procesamiento-de-datos">Procesamiento de datos</a> •
<a  href="#---------acerca-de-data">Acerca de DATA</a> •
<a  href="#e-mail-contacto">Contacto</a> •
<a  href="#-contribuyendo">Contribuyendo</a> •
<a  href="#page_facing_up-licencia">Licencia, términos y condiciones</a> •
</p>

<br>

## <img src="https://www.gub.uy/infraestructura-datos-espaciales/sites/infraestructura-datos-espaciales/files/catalogo/IDE.jpg" height="26"> Introducción

IDEUY-py es una herramienta y paquete de Python que facilita y optimiza la descarga programática de las ortoimágenes del vuelo fotogramétrico, disponibles desde el Visualizador online de la [Infraestructura de Datos Espaciales de Uruguay
(IDEuy)](https://www.gub.uy/infraestructura-datos-espaciales/).

IDEUY-py surge de un proyecto generado con el gobierno de Uruguay el cual, implicaba el uso y descarga de múltiples ortoimágenes disponibles para su descarga manual en el [visualizador](https://visualizador.ide.uy/ideuy/core/load_public_project/ideuy/). Este visualizador es una herramienta que cuenta con un buscador, permitiéndo también trazar un area rectangular para obtener las imágenes. Sin embargo, implica una descarga poco óptima y lenta al ser una descarga manual. Por lo que se creo este paquete de Python para facilitar y optimizar la descarga de imágenes a través del filtrado del área de interés y descarga de ortoimágenes para su uso posterior.

<details><summary><b>Origen, Objetivos y Antecedentes</b></summary>

### :mag_right: Origen 

La IDE tiene como cometidos liderar la articulación y el fortalecimiento de la producción y acceso a la información geográfica del Uruguay para que sea fiable, oportuna, interoperable, de alta calidad, y brinde apoyo en el análisis y la toma de decisiones de organismos, academia, empresas y ciudadanos.

La Infraestructura de Datos Espaciales (IDE) fue creada por los Art. 35 y 36 de la Ley 19.149 de 2013 como un órgano desconcentrado de Presidencia de la República, con autonomía técnica. 
Su cometido es liderar la articulación y el fortalecimiento de la producción y el acceso de la información geográfica del Uruguay para que sea fiable, oportuna, interoperable, de alta calidad, y brinde apoyo en la toma de decisiones para el desarrollo nacional; esto incluye a organismos públicos, academia, empresas y ciudadanos. Se inspira en los principios de cooperación y coordinación entre las administraciones, así como en la transparencia y el acceso a la información pública. 

### Objetivos  
Optimizar la descarga de ortoimágenes a través de un paquete de Phyton evitando así la descarga manual desde su visualizador.

### Antecedentes

En julio de 2018 se conformó dentro de la IDEuy el Grupo de Trabajo sobre Imágenes Satelitales. La finalidad de este grupo es el intercambio de información y la coordinación interinstitucional para ordenar la producción, facilitar la disponibilidad, el acceso y uso de productos, servicios e información geográfica proveniente de sensores satelitales, como apoyo a los procesos de toma de decisiones para el desarrollo nacional, con una perspectiva de corto, mediano y largo plazo. 

En el marco de la iniciativa “Manos en la Data — Uruguay” (MeD-Uruguay) convocada por la Dirección de Investigaciones Socioeconómicas (DIS) de CAF-banco de Desarrollo de América Latina y la Agencia de Gobierno Electrónico y Sociedad de la Información y del Conocimiento (AGESIC), se trabajó en un ambicioso proyecto de tres componentes desarrolladas en simultáneo y en solo ocho semanas por distintas agencias del Estado uruguayo y Dymaxion Labs.
Para propiciar el uso de datos intensivo, eficiente y seguro dentro del Estado, CAF desarrolló esta iniciativa que consiste en una metodología de trabajo para la producción de prototipos de ciencia de datos, que atiendan una problemática o pregunta de política pública muy concreta, y lo hagan de manera rápida, colaborativa y costo-efectiva. MeD-Uruguay es la tercera réplica de esta iniciativa de CAF, que fue desarrollada previamente en Argentina y Colombia.
Los tres prototipos elaborados fueron:
 - Herramienta para el monitoreo de asentamientos informales
 - Herramienta para la detección y cuantificación de equipos de aprovechamiento solar
 - Herramienta para determinar categorías de caminos en la red vial uruguaya

Para el desarrollo de estos prototipos, Dymaxion Labs trabajó mano a mano con con técnicos de AGESIC, IDE , el Ministerio de Desarrollo Social de Uruguay (MIDES), el Ministerio de Vivienda y Ordenamiento Territorial (MVOT), el Ministerio de Industria, Energía y Minería (MIEM), el Ministerio de Transporte y Obra Pública (MTOP), la Oficina de Planeamiento y Presupuesto (OPP) y Gobiernos Departamentales (GGDD). Fue muy importante la participación y buena predisposición de todas las partes para lograr sortear los obstáculos que se presentaron a lo largo del proceso y llegar a los resultados pautados.
Cabe destacar que, dada la necesidad de un acceso intensivo a imágenes del vuelo fotogramétrico en los servidores de IDE, en el marco de Manos en la Data-Uruguay Dymaxion Labs desarrolló adicionalmente a los tres prototipos este paquete de Python que permite descargar las imágenes de manera programática y por área de interés, lo cual también contribuirá a un uso más provechoso de la valiosa herramienta de imágenes gestionada por IDE.

</details>
<br>

## :notebook: Guía de instalación y uso

### 📋 Pre-requisitos generales

 - #### [Python](https://www.python.org/)  v3.6 
 - #### [PIP](https://pypi.org/project/pip/)

Aseguremonos de tener instalado **GDAL** para poder iniciar la instalación.
 
### **Linux y macOS**
   #### **GDAL**

```
  $ sudo easy_install GDAL
```

Si tienes problemas con la instalación, dirigete a su [web](https://pypi.org/project/GDAL/) para encontrar pistas.

Ahora podemos instalar el paquete sin problemas:
```
pip install --user ideuy
```
### **Windows**

Para Windows está disponible [nvm-windows](https://github.com/coreybutler/nvm-windows), cuyo instalador puedes descargar [aqui](https://github.com/coreybutler/nvm-windows/releases). Toma en consideración que para usar este paquete debes remover versiones existentes de node y npm antes de instalar.

Para más información dirígete al [proyecto](https://github.com/coreybutler/nvm-windows)


### **Uso**

### Scripts de consola disponibles

* `ideuy_filter`: Filtra un shapefile de grilla (nacional o urbana) con otro shapefile de Áreas de Interés (AOI).
* `ideuy_download_images`: Descarga imágenes (en paralelo) de un formato a partir de un shapefile de grilla (generado por ideuy_filter).

Para obtener una lista de opciones de estos comandos:
```
ideuy_filter -h
```
```
ideuy_download -h
```
#### **Ejemplo de uso**
Supongamos que tenemos un Shapefile de polígonos, con áreas de interés. Se quiere descargar imágenes RGB en formato JPG, a nivel urbano.

En general, los pasos a seguir son:

- (opcional) Reproyecto shapefile a CRS epsg:5381 (es un requerimiento de ``ideuy_filter``)
- Filtro la grilla nacional con el Shapefile, usando ``ideuy_filter``
- Descargo imágenes con ``ideuy_download`` y la grilla filtrada

![shapefile-grilla](http://drive.google.com/uc?export=view&id=1wwP-8AlJXWIAUHh9P0HrcZWbt8XEZkKo)

Filtramos la grilla urbana. Esto genera un nuevo GeoJSON en data/ideuy/grilla_urbana_filtrada.geojson
```
ideuy_filter --type urban \
              --output data/ideuy/ grilla_urbana_filtrada.geojson \
              data/ideuy/areas.geojson
```
El comando anterior produce el archivo ``grilla_urbana_filtrada.geojson``, que contiene las hojas de la ortoimagen urbana que intersecan con los polígonos de ``areas.geojson``. Estas son las imágenes que debemos descargar.


## Desarrollo

Crear un entorno virtual e instalar el paquete con pip en modo desarrollo, por ejemplo:

```
virtualenv -p python3 .venv/
source .venv/bin/activate
pip install -e .
```

</details>

##  Autores
Puede dirigirse a [AUTHORS.rst](AUTHORS.rst).

##  :e-mail: Contacto

En caso de consultas sobre este paquete, IDEUY o contactos de prensa puede dirigirse a munshkr@gmail.com.

<br>

## 🤝 Contribuyendo

Cualquier ayuda en las pruebas, el desarrollo, la documentación y otras tareas es muy apreciada y útil para el proyecto. Puedes escribirnos a munshkr@gmail.com en caso que te interese colaborar con el proyecto.

<br>

## :page_facing_up: Licencia

### Disponibilidad del código como software libre 

El código fuente se libera bajo una licencia BSD-2. Por favor, consulte [LICENSE.txt](LICENSE.txt) para más información.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

This software is provided by the copyright holders and contributors "as is" and
Any express or implied warranties, including, but not limited to, the implied
Warranties of merchantability and fitness for a particular purpose are
Disclaimed. In no event shall the copyright holder or contributors be liable
For any direct, indirect, incidental, special, exemplary, or consequential
Damages (including, but not limited to, procurement of substitute goods or
Services; loss of use, data, or profits; or business interruption) however
Caused and on any theory of liability, whether in contract, strict liability,
Or tort (including negligence or otherwise) arising in any way out of the use
Of this software, even if advised of the possibility of such damage.


## Limitación de responsabilidades

El BID no será responsable, bajo circunstancia alguna, de daño ni indemnización, moral o patrimonial; directo o indirecto; accesorio o especial; o por vía de consecuencia, previsto o imprevisto, que pudiese surgir:

i. Bajo cualquier teoría de responsabilidad, ya sea por contrato, infracción de derechos de propiedad intelectual, negligencia o bajo cualquier otra teoría; y/o

ii. A raíz del uso de la Herramienta Digital, incluyendo, pero sin limitación de potenciales defectos en la Herramienta Digital, o la pérdida o inexactitud de los datos de cualquier tipo. Lo anterior incluye los gastos o daños asociados a fallas de comunicación y/o fallas de funcionamiento de computadoras, vinculados con la utilización de la Herramienta Digital.




