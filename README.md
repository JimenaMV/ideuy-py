*Esta herramienta digital forma parte del catálogo de herramientas del **Banco Interamericano de Desarrollo**. Puedes conocer más sobre la iniciativa del BID en [code.iadb.org](https://code.iadb.org)*

<br>

<p align="center">
<img  height="200"  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCtXkOdL-iKuv-Y8wMZA8piyiHTkrzPlMPnA&usqp=CAU">
</p>

<p align="center">
<img  src="https://img.shields.io/badge/license-BSD%202-green">
<img  src="https://img.shields.io/badge/version-0.1.0-yellow">
<img  src="https://img.shields.io/badge/build%20with-python-yellow">
   
<img  src="https://img.shields.io/github/last-commit/datauy/ElijoEstudiar">
<img  src="https://img.shields.io/website?up_color=green&up_message=online&url=https%3A%2F%2Felijoestudiar.edu.uy%2F%23%2Fintro">
<img  src="https://img.shields.io/badge/built%20with-ionic-blue">
<a href="https://sonarcloud.io/dashboard?id=datauy_ElijoEstudiar" target="_blank"><img src="https://sonarcloud.io/api/project_badges/measure?project=datauy_ElijoEstudiar&metric=alert_status"></a>
</p>

<p  align="center">
• <a  href="#-introducción">Introducción</a> •
<a  href="#notebook-guía-de-instalación-y-uso">Guía de instalación y uso</a> •
<a  href="#chart_with_downwards_trend-datos-abiertos">Datos abiertos</a> •
<a  href="#memo-procesamiento-de-datos">Procesamiento de datos</a> •
<a  href="#open_hands-lenguaje-inclusivo">Lenguaje inclusivo</a> •
<a  href="#---------acerca-de-data">Acerca de DATA</a> •
<a  href="#e-mail-contacto">Contacto</a> •
<a  href="#-contribuyendo">Contribuyendo</a> •
<a  href="#page_facing_up-licencia">Licencia, términos y condiciones</a> •
</p>

<br>

## <img src="https://www.gub.uy/infraestructura-datos-espaciales/sites/infraestructura-datos-espaciales/files/catalogo/IDE.jpg" height="26"> Introducción

Herramienta y paquete de Python que facilita la descarga programática de las ortoimágenes del vuelo fotogramétrico, disponibles desde el Visualizador online de la [Infraestructura de Datos Espaciales de Uruguay
(IDEuy)](https://www.gub.uy/infraestructura-datos-espaciales/).


<details><summary><b>Origen, Objetivos y Antecedentes</b></summary>

### :mag_right: Origen 

La Infraestructura de Datos Espaciales (IDE) fue creada por los Art. 35 y 36 de la Ley 19.149 de 2013 como un órgano desconcentrado de Presidencia de la República, con autonomía técnica. 
Su cometido es liderar la articulación y el fortalecimiento de la producción y el acceso de la información geográfica del Uruguay para que sea fiable, oportuna, interoperable, de alta calidad, y brinde apoyo en la toma de decisiones para el desarrollo nacional; esto incluye a organismos públicos, academia, empresas y ciudadanos. Se inspira en los principios de cooperación y coordinación entre las administraciones, así como en la transparencia y el acceso a la información pública. 

### Objetivos  
La IDE tiene como cometidos liderar la articulación y el fortalecimiento de la producción y acceso a la información geográfica del Uruguay para que sea fiable, oportuna, interoperable, de alta calidad, y brinde apoyo en el análisis y la toma de decisiones de organismos, academia, empresas y ciudadanos.

### Antecedentes

En julio de 2018 se conformó dentro de la IDEuy el Grupo de Trabajo sobre Imágenes Satelitales. La finalidad de este grupo es el intercambio de información y la coordinación interinstitucional para ordenar la producción, facilitar la disponibilidad, el acceso y uso de productos, servicios e información geográfica proveniente de sensores satelitales, como apoyo a los procesos de toma de decisiones para el desarrollo nacional, con una perspectiva de corto, mediano y largo plazo. 

Dentro de esta línea de trabajo también resalta un proyecto de cooperación internacional, que permitirá disponer en Uruguay de un Sistema de Aplicación Móvil de Recepción y Procesamiento de Datos Meteorológicos Satelitales Integrados Multisatélite. Este equipamiento se utilizará para la descarga y procesamiento de imágenes satelitales de plataformas como NOAA18, MODIS (Terra, Aqua) y FY-3D las cuales sirven como sustento en la gestión de temas atmosféricos, ambientales, forestales y de uso del suelo. Este equipo es fruto de un convenio firmado entre el Ministerio de Educación y Cultura (Uruguay) y el Ministerio de Ecología y Medio Ambiente (República Popular de China).
</details>
<br>

## :notebook: Guía de instalación y uso

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### 📋 Pre-requisitos
#### Para plataforma Web.
 - #### [Node.js](https://nodejs.org/en/)  >=10.19.0 <=11.15.0

Este proyecto requiere alguna de las versiones especificadas. Para evitar conflictos de versiones en tu sistema operativo recomendamos utilizar algún Node Version Manager, que permite usar multiples versiones de Node en un solo equipo.
 
**Linux y macOS**

Para ambos existe [nvm](https://github.com/nvm-sh/nvm), que puedes instalar mediante alguno de los siguientes comandos:

```
  $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```
```
  $ wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```

Si tienes problemas con la instalación, dirigete a su [repositorio](https://github.com/nvm-sh/nvm#troubleshooting-on-linux) para encontrar pistas.

**Windows**

Para Windows está disponible [nvm-windows](https://github.com/coreybutler/nvm-windows), cuyo instalador puedes descargar [aqui](https://github.com/coreybutler/nvm-windows/releases). Toma en consideración que para usar este paquete debes remover versiones existentes de node y npm antes de instalar.

Para más información dirígete al [proyecto](https://github.com/coreybutler/nvm-windows)
<br>

Una vez instalado, realizaremos el cambio de versión antes de agregar las demás herramientas (aplica para Linux, macOS y Windows):

````
  $ nvm install #versión (>=10.19.0 <=11.15.0)
  $ nvm use #versión (>=10.19.0 <=11.15.0)
````


- **[Ionic](https://ionicframework.com/docs/cli)** como framework base.
- **[Gulp](https://gulpjs.com/docs/en/getting-started/quick-start/)** para automatizar tasks.
- **[Bower](https://github.com/bower/bower)** para mantener actualizadas nuestras librerías.
- **[Cordova](https://ionicframework.com/docs/v3/intro/installation/)** para soporte de apps nativas.
```
  $ npm install -g @ionic/cli gulp-cli bower cordova
```

<br>


## 🔧Guía de instalación

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

###  🔧 	Instalación 

Empezaremos por clonar el repositorio:
```
  $ git clone https://github.com/datauy/ElijoEstudiar.git
  $ cd ElijoEstudiar/
```
Asegúrate de estar utilizando alguna de las versiones anteriormente especificadas:
````
  $ nvm use #versión
````
Instalamos el proyecto y actualizamos las librerías necesarias:

````
  $ npm install
  $ bower install
````

<br>

###  :computer: Uso  

Una vez instalado el proyecto corremos las [tasks](https://github.com/datauy/ElijoEstudiar/blob/master/gulpfile.js) creadas con gulp:
```
  $ gulp
```
Por último iniciamos el servidor de desarrollo local para **plataforma web**:

```
  $ ionic serve
```
¡Y listo! El proyecto se iniciará en la dirección http://localhost:8100 de tu navegador predeterminado y se actualizará con cada cambio que realices.


<br />


## :chart_with_downwards_trend: Datos abiertos

  
#### ¿Qué son los datos abiertos? 
El estado recoge y produce datos para cumplir con su función. Su publicación en formatos abiertos permite que sean reutilizados por el gobierno, sociedad civil, organizaciones, empresas o ciudadanos en general.

www.catalogodatos.gub.uy


#### Datos abiertos que utiliza la aplicación

Los datos utilizados en esta aplicación se encuentran disponibles para su reutilización a través del Catálogo Nacional de Datos Abiertos de AGESIC y otras fuentes, como datos abiertos, en formatos abiertos.

* ANEP - Centros educativos y oferta educativa
  
* INE - Mapas vectoriales (departamentos)

* IDE.uy - Localidades de Uruguay

Otros datos

* Banasevich, Isabel et al. Liceos del Uruguay. Montevideo: CES, 2008.

Los organismos estatales del sector público recogen, producen, reproducen y difunden datos para cumplir con su función pública. Incorporar la publicación de datos públicos en formatos abiertos abre la puerta a la posibilidad de que los mismos sean reutilizados en nuevos proyectos, que puedan combinarse con otras fuentes de datos y generar nuevas aplicaciones desarrolladas por el gobierno, por la sociedad civil, organizaciones, empresas o ciudadanos en general.

  
<br>
  

## :memo: Procesamiento de datos

Los análisis y visualizaciones provistos por esta aplicación son realizados por DATA Uruguay. Estas operaciones están disponibles para consulta a través del código de la aplicación disponible en GitHub, así como el resto del código fuente. De cualquier manera se detallan a continuación algunas definiciones clave para el procesamiento de los datos y presentación de resultados.

<details><summary><b>Turnos</b></summary>

La herramienta procura evitar ocultar a los/as usuarios/as información erróneamente, por lo que se aplica una política de filtros, donde si la certeza es baja, se opta por incluir información en los resultados, en lugar de excluirla. A modo de ejemplo; contamos con filtros para turnos que son “Matutino”, “Vespertino”, “Nocturno” y “Completo/Extendido”, que sirven para la enorme mayoría de la información disponible. Sin embargo, existen otros turnos que no están asociados al horario como por ejemplo “Rural”. En una búsqueda por filtrando únicamente a turno “Matutino”, se mostrarán también en los resultados, aquellos turnos que no sean “Matutino”, pero tampoco “Vespertino”, “Nocturno” y “Completo/Extendido”, de forma de evitar infomración que podría ser útil.

</details>

<details><summary><b>Filtros</b></summary>

De la misma forma, se procura siempre ofrecer resultados a la búsqueda, así sea que ésto implique ampliar el criterio. Si por ejemplo se está buscando un curso específico en una localidad donde no está disponible, el resultado no será nulo, sino que se mostrarán las opciones disponibles en otras partes del país.

</details>

<details><summary><b>Correcciones ortográficas</b></summary>

Los datos fuente originales, por diversas causas relacionadas con el origen y archivo de los mismos en sistemas antiguos, están disponiobles únicamente en mayúsculas y sin el uso de tildes. Para proveer una mejor experiencia de usuario, se adaptaron éstas bases originales para corregir éstos defectos y algunas correcciones ortográficas. Aunque se tomaron los máximos recaudos para evitar introducir errores en éste proceso, recomendamos utilizar para procesamientos los datos originales, enlazados en la sección “Datos abiertos que utiliza la aplicación” de este documento. Los datos reprocesados igualmente se encuentran disponibles en el Catálogo Nacional de Datos Abiertos.

</details>

<details><summary><b>Diccionario de sinónimos</b></summary>

Para facilitar búsquedas de cursos y niveles, se elaboró un diccionario de palabras que se usan coloquialmente para referirse a éstos, lo que permite etiquetarlos y ofrecerlos como resultado cuando se utilizan esas palabras. Por ejemplo, la palabras “tercero” ofrecerá tanto “Escuela común” (CEIP) como “Ciclo básico” (CES) entre sus resultados.

</details>

<details><summary><b>Previaturas</b></summary>

En los datos abiertos que utiliza la aplicación, se incluyen las previaturas que permiten acceder a cada curso. Como una forma de facilitar las consultas, usamos esta información para sugerirle a los/as usuarios/as qué previas se deben cursar para un curso, cuando la persona no tiene los requerimientos necesarios. Ésta información se brinda como ayuda, pero pueden existir otras opciones o cambios en las previaturas. Ante dudas sobre el nivel al que es posible acceder, se recomienda consultar en los centros de estudio, o en DerechosDeEstudiantes.edu.uy.

El árbol de previaturas generado a partir de esta información se encuentra disponibles en el Catálogo Nacional de Datos Abiertos.

</details>

<br>
  
## :open_hands: Lenguaje inclusivo

En la elaboración de este material se ha buscado que el lenguaje no invisibilice ni discrimine a las mujeres y a la vez que el uso reiterado de “ /o”, “/a”, “los y las”, etcétera, no dificulte la lectura. En la página 9 de la siguiente publicación se puede encontrar recomendaciones al respecto: [Guía de Lenguaje Inclusivo - INMUJERES](http://www.inmujeres.gub.uy/innovaportal/file/21498/1/15guia_de_lenguaje_inclusivo.pdf).
  
<br>

## ![enter image description here](https://avatars0.githubusercontent.com/u/1519867?s=25&v=4)         			Acerca de DATA

Somos una organización de la sociedad civil que trabaja creando herramientas sociales para promover la participación y el debate público a través de la transparencia, datos abiertos y acceso a la información.

www.datauy.org    	


<br>
  
##  :e-mail: Contacto

En caso de consultas sobre este paquete, IDEUY o contactos de prensa puede dirigirse a munshkr@gmail.com.

<br>

## 🤝 Contribuyendo

Como la mayoría de los proyectos que trabajan con datos abiertos y software libre, la retroalimentación de los usuarios es una herramienta fundamental para la mejora de los datos y su tratamiento, por lo que agradecemos e incentivamos la recepción de ideas, sugerencias o correcciones. Puedes escribirnos a devops@data.org.uy en caso que te interese colaborar de otra forma.

<br>

## :page_facing_up: Licencia

### Disponibilidad del código como software libre 

Copyright 2020 Dymaxion Labs
Ver [LICENSE.txt](LICENSE.txt).

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


###  Términos y condiciones 

La prestación de este servicio tiene carácter gratuito para los usuarios. Los usuarios se obligan a hacer buen uso del sitio web y de sus contenidos, respetando la normativa nacional vigente, las buenas costumbres y el orden público, comprometiéndose en todos los casos a no causar daños al mismo ni a ningún tercero. A tal efecto, el Usuario se abstendrá de utilizar cualquiera de los servicios con fines o efectos ilícitos, prohibidos en los presentes Términos y condiciones, lesivos de los derechos e intereses de terceros, o que de cualquier forma puedan dañar, inutilizar, sobrecargar, deteriorar o impedir la normal utilización de los servicios, documentos y toda clase de contenidos en cualquier equipo informático o de otros Usuarios.

Para asegurarnos de que la aplicación esté acorde a las necesidades de nuestros usuarios, e intentar mejorarla utilizamos Google Analytics para recolectar información sobre cómo se utiliza. Google Analytics almacena información como qué páginas ha visitado, cuánto tiempo ha navegado en las mismas, cómo llegó a la página, qué elementos clikea e información sobre qué navegador utiliza. Su dirección IP es enmascarada (parcialmente almacenada) y la información personal sólo es reportada en forma no individualizada (agregada). No permitimos a Google usar o compartir nuestros datos analíticos para ningún propósito además de proveernos de información analítica y recomendamos que todo usuario de Google Analytics siga la misma política.

## Limitación de responsabilidades

El BID no será responsable, bajo circunstancia alguna, de daño ni indemnización, moral o patrimonial; directo o indirecto; accesorio o especial; o por vía de consecuencia, previsto o imprevisto, que pudiese surgir:

i. Bajo cualquier teoría de responsabilidad, ya sea por contrato, infracción de derechos de propiedad intelectual, negligencia o bajo cualquier otra teoría; y/o

ii. A raíz del uso de la Herramienta Digital, incluyendo, pero sin limitación de potenciales defectos en la Herramienta Digital, o la pérdida o inexactitud de los datos de cualquier tipo. Lo anterior incluye los gastos o daños asociados a fallas de comunicación y/o fallas de funcionamiento de computadoras, vinculados con la utilización de la Herramienta Digital.




