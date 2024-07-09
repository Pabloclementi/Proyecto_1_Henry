# Proyecto 1 - (MVP) Modelo de recomendacion de peliculas. 

## Descripción

El objetivo del proyecto es crear un (MVP) modelo de recomendación de películas utilizando diversos análisis y técnicas de machine learning.

## Contenido del Proyecto

1.	Exploratory Data Analysis (EDA): Análisis inicial de los datos para entender las relaciones entre variables, detectar outliers y encontrar patrones interesantes.
Aqui se detectaron varios outliers en variables numericas, como runtime y en return, pero se mantuvieron ya que el modelo de recomendación solo se vasa en variables categoricas como genero, titulo, y descripción.
Se observo que la columna vote_average es la que manejaba una distribución mas uniforme y no se encontraba tan sesgada.
En el archivo EDA.html , en el directorio data se puede ver un paneo general del analisis.
2.	Preparación de Datos: Limpieza y transformación de datos para adecuarlos al modelo de recomendación.
3.	Modelo de Recomendación: Implementación de un sistema de recomendación de películas basado en características como género, título y overview.

## Estructura del Repositorio

:file_folder: **data/** - Contiene los archivos de datos utilizados en el proyecto.

:file_folder: **notebooks/** - Notebooks de Jupyter utilizados para el análisis y desarrollo del proyecto.

:snake: **main.py** - Codigo principal principal del proyecto. 

:page_facing_up: **README.md** - Este archivo de documentación principal del proyecto.






### Datos

La carpeta `data_original` no está incluida en este repositorio debido a su tamaño. Puedes descargarla desde el siguiente enlace:

[data_original](https://drive.google.com/drive/folders/1u3DQ7Plo3DB9ieg7bLhBd_pvSCg-exPr?usp=sharing)

Una vez descargada, coloca los archivos dentro de la carpeta data 

## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo academico y pruebas._

1.	Clona este repositorio:
   ```sh
	git clone https://github.com/Pabloclementi/Proyecto_1_Henry.git
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):

   ```sh
   python -m venv env
   ```
3. Activa tu entorno virtual

   ```sh
   source env/bin/activate
   ``` 


4.	Instala las dependencias necesarias::
   ```python
	pip install -r requirements.txt
   ```


# Herramientas y Tecnologías Utilizadas

•	**Lenguajes y Librerías:**

•	Python

•	Pandas

•	NumPy

•	Scikit-learn

•	Jupyter Notebook

•	**Herramientas de EDA:**

•	YData

•	Data Wrangler (extensión de VSC)




## Ejecutando las pruebas ⚙️ 

[APP_Proyecto1](https://proyecto-1-henry-79jk.onrender.com/docs)
[VideoTuorial](https://drive.google.com/drive/folders/1A4I-TEvz9-nLHmXs_5oGJaKhWvlGON7r)

## Construido con 🛠️

_Herramienta utilizadas_


* [FastApi](https://fastapi.tiangolo.com/) - 
* [Render](https://render.com/) -


## Conclusion 

En este proyecto, se trabajó con datasets en archivos CSV, los cuales fueron sometidos a un proceso de ETL (Extracción, Transformación y Carga) y un Análisis Exploratorio de Datos (EDA). Se siguieron todas las consignas solicitadas durante el desarrollo del proyecto, asegurando un flujo de trabajo organizado y coherente.

Se creó una API utilizando FastAPI y se realizó el deployment en Render, facilitando el acceso y la interacción con el sistema de recomendación. El modelo de recomendaciones fue entrenado utilizando la similitud del coseno  y ha demostrado funcionar correctamente.

Para ser un MVP (Producto Mínimo Viable), se ha alcanzado un buen resultado, estableciendo una base sólida que, con más experiencia y tiempo, puede ser optimizada y mejorada significativamente.

## Autores ✒️
[Pabloclementi](https://github.com/Pabloclementi) 😊


## Expresiones de Gratitud 🎁

* Agradecer a la cohorte numero 23 de DataScience , Profesores, Ta, Ha, Compañeros, etc
  📢
---
Muchas Gracias [Pabloclementi](https://github.com/Pabloclementi) 😊
