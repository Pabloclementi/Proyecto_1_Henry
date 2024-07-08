# Proyecto 1 - Henry

## Descripción

Este es mi primer proyecto para el Bootcamp de Data Scientist en SoyHenry. El objetivo del proyecto es crear un modelo de recomendación de películas utilizando diversos análisis y técnicas de machine learning.

## Contenido del Proyecto

1.	Exploratory Data Analysis (EDA): Análisis inicial de los datos para entender las relaciones entre variables, detectar outliers y encontrar patrones interesantes.
Aqui se detectaron varios outliers en variables numericas, como runtime y en return, pero se mantuvieron ya que el modelo de recomendación solo se vasa en variables categoricas como genero, titulo, y descripción.
Se observo que la columna vote_average es la que manejaba una distribución mas uniforme y no se encontraba tan sesgada.
En el archivo EDA.html , en el directorio data se puede ver un paneo general del analisis.
2.	Preparación de Datos: Limpieza y transformación de datos para adecuarlos al modelo de recomendación.
3.	Modelo de Recomendación: Implementación de un sistema de recomendación de películas basado en características como género, título y overview.

## Estructura del Repositorio

•	data/: Contiene los archivos de datos utilizados en el proyecto.
•	notebooks/: Notebooks de Jupyter utilizados para el análisis y desarrollo del proyecto.
•	main.py: Código principal del modelo.
•	README.md: Este archivo, con la descripción del proyecto.
### Datos

La carpeta `data_original` no está incluida en este repositorio debido a su tamaño. Puedes descargarla desde el siguiente enlace:

[data_original](https://drive.google.com/drive/folders/1u3DQ7Plo3DB9ieg7bLhBd_pvSCg-exPr?usp=sharing)

Una vez descargada, coloca los archivos dentro de la carpeta data 

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo academico y pruebas._

 1.	Clona este repositorio:
    `git clone https://github.com/Pabloclementi/Proyecto_1_Henry.git` 
    
 2. Crea y activa un entorno virtual (opcional pero recomendado):
    `python -m venv env`
    `source env/bin/activate`  # En Windows usa `env\Scripts\activate`
    
3. Instala las dependencias necesarias:
    `pip install -r requirements.txt`

# Herramientas y Tecnologías Utilizadas

	•	Lenguajes y Librerías:
	•	Python
	•	Pandas
	•	NumPy
	•	Scikit-learn
	•	Jupyter Notebook
	•	Herramientas de EDA:
	•	YData
    •	Data Wrangler (extension de VSC)




## Ejecutando las pruebas ⚙️ 

[APP_Proyecto1](https://proyecto-1-henry-79jk.onrender.com/docs)


## Construido con 🛠️

_Herramienta utilizadas_


* [FastApi](https://fastapi.tiangolo.com/) - 
* [Render](https://render.com/) -


## Autores ✒️
[Pabloclementi](https://github.com/Pabloclementi) 😊


## Expresiones de Gratitud 🎁

* Agradecer a la cohorte numero 23 de DataScience , Profesores, Ta, Ha, Compañeros, etc
  📢
---
Muchas Gracias [Pabloclementi](https://github.com/Pabloclementi) 😊
