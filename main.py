from fastapi import FastAPI, HTTPException
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string 
from typing import List

#Cargamos los datasets en variables con el metodo de pandas pd.read_csv()
movies_df = pd.read_csv('data/moviesfinal.csv')
modelo_df = pd.read_csv('data/top_5000_movies.csv')

# Vectorización utilizando TF-IDF con stop words en None , previamente hecho en el EDA
vectorizer = TfidfVectorizer(stop_words=None)
tfidf_matrix = vectorizer.fit_transform(modelo_df['combined_features'])

#Obtenemos la similitud del coseno
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix) 

#Instanciamos la api
app= FastAPI() 

@app.get("/")
def read_root():
    return {"message": "Bienvenidos a la API , de mi primer proyecto"}



## Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
@app.get("/meses/{mes}")
def cantidad_filmaciones_mes(mes: str): 
    """
    Devuelve la cantidad de películas estrenadas en un Mes específico en español, con estado 'released'.
    
    Parameteros:
    mes (str): Debera ingresar un mes en español

    Returns:
    str: Una cadena con la cantidad de películas estrenadas en el Mes especificado.
    """
    #Mapeo de meses en español a numeros para utulizar funcion day of the week de pandas
    meses = {
    'enero': 1,
    'febrero': 2,
    'marzo': 3,
    'abril': 4,
    'mayo': 5,
    'junio': 6,
    'julio': 7,
    'agosto': 8,
    'septiembre': 9,
    'octubre': 10,
    'noviembre': 11,
    'diciembre': 12
}
    # Formatear la columna de release_date a formato datatime. 
    movies_df['release_date']= pd.to_datetime(movies_df['release_date'],format= '%Y-%m-%d')
    # Convertir el nombre del mes a minúsculas para asegurar coincidencia
    mes = mes.lower()
    
    # Verificar si el mes ingresado es válido, de lo contrario arroja error.
    if mes not in meses:
        raise HTTPException(status_code=400, detail=f"Mes ingresado '{mes}' no es válido. Por favor ingrese un mes en Español.")
    
    # Obtener el número del mes
    mes_numero = meses[mes]
    
    # Contar las películas estrenadas en el mes especificado, que hayan sido estrenadas
    peliculas_filtradas = movies_df[
        (movies_df['release_date'].dt.month == mes_numero)
    ]
    
    cantidad_peliculas = len(peliculas_filtradas)
    
    return {"mes": mes, "cantidad_peliculas": cantidad_peliculas} 


# Creamos funcio en donde Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.

@app.get("/dias_semana/{dia_espanol}")
def cantidad_peliculas_por_dia(dia_espanol: str):
    """
    Devuelve la cantidad de películas estrenadas en un día específico en español, con estado 'released'.
    
    Parameteros:
    df (DataFrame): El DataFrame que contiene las columnas 'release_date' y 'status'.
    dia_espanol (str): El día de la semana en español (lunes, martes, miércoles, jueves, viernes, sábado, domingo).

    Returns:
    str: Una cadena con la cantidad de películas estrenadas en el día especificado.
    """
    # Diccionario para mapear los días de la semana en español a números de día de la semana (0=Lunes, 6=Domingo)
    dias_semana = {
        'lunes': 0,
        'martes': 1,
        'miércoles': 2,
        'miercoles':2,
        'jueves': 3,
        'viernes': 4,
        'sábado': 5,
        'sabado':5,
        'domingo': 6
    }
 # Convertir la columna de fechas a datetime si no lo está
    movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
    
# Obtener el número de día de la semana correspondiente al día en español
    dia_numero = dias_semana.get(dia_espanol.lower())
    
    if dia_numero is None:
        raise ValueError("Día en español no válido")
    
    # Filtrar las filas donde el día de la semana coincide con el día especificado y el estado es 'released'
    peliculas = movies_df[(movies_df['release_date'].dt.dayofweek == dia_numero)]
    #Sumamos cantidad de las filas
    cantidad = len(peliculas)
    # Formatear el mensaje de retorno
    return f"{cantidad} películas fueron estrenadas en los días {dia_espanol}, con estado 'released'"


 
#Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
@app.get("/titulo/{titulo}")
def titulo(titulo: str):
    """
    Devuelve el título, el año de estreno y el score de una película específica.
    
    Parameteros:
    titulo (str): El título de la película.

    Returns:
    str: Una cadena con el título, el año de estreno y el score de la película.
    """

    # Filtrar las filas donde el título coincide con el título especificado, poniendolo todo en minuscula 
    pelicula = movies_df[movies_df['title'].str.lower() == titulo.lower()]
        
    # Verificar si la película existe
    if pelicula.empty:
            raise HTTPException(status_code=404, detail=f"Película '{titulo}' no encontrada.")
        
    # Obtener el título, el año de estreno y el score de la película
    titulo = pelicula['title'].values[0]
    año = int(pelicula['release_year'].values[0])
    score = pelicula['vote_average'].values[0]
    
    # Formatear el mensaje de retorno
    return f"Título: {titulo} Año de estreno: {año} Score: {score}"

# Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
#Ejemplo de retorno: La película `X` fue estrenada en el año `X`. La misma cuenta con un total de `X` valoraciones, con un promedio de `X`

@app.get("/votos/{titulo}")
def votos_titulo(titulo: str):
    """Se ingresa el título de una filmación esperando como respuesta el título, 
    la cantidad de votos y el valor promedio de las votaciones. 
    dLa misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, arrojara error. """

    movie = movies_df[movies_df['title'].str.lower() == titulo.lower()]
    if movie.empty:
            raise HTTPException(status_code=404, detail=f"Película '{titulo}' no encontrada.")
    titulo = movie['title'].values[0]
    votos= int(movie['vote_count'].values[0])
    promedio = movie['vote_average'].values[0]
    año = int(movie['release_year'].values[0])
    if votos < 2000:
            raise HTTPException(status_code=404, detail=f"Película '{titulo}' no cuenta con suficientes valoraciones.")
    return f"La película {titulo} fue estrenada en el año {año}. La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio}."


#Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. **La definición no deberá considerar directores.**
@app.get("/nombre_actor/{nombre_actor}") 
def get_actor(actor_name: str):
    """
    Devuelve el éxito del actor, la cantidad de películas en las que ha participado y el promedio de retorno.
    Esta funcion arrojara solo las peliculas en las que participo como actor, no contemplando si en la misma es actor y director.
    
    Parametros:
    actor_name (str): El nombre del actor.
    """
    # Convertir los nombres de los actores y directores a minúsculas en el DataFrame y rellenar NaN
    movies_df['actor'] = movies_df['actor'].str.lower().fillna('sin dato')
    movies_df['director'] = movies_df['director'].str.lower().fillna('sin dato')

    # Convertir el nombre del actor a minúsculas
    actor_name = actor_name.lower()
    
    # Filtrar las películas en las que ha participado el actor, excluyendo aquellas donde también sea el director
    actor_movies = movies_df[movies_df.apply(lambda row: actor_name in row['actor'].split(', ') and actor_name not in row['director'].split(', '), axis=1)]
    
    if actor_movies.empty:
        raise HTTPException(status_code=404, detail="El actor no se ha encontrado en el dataset")
    
    # Calcular el éxito del actor
    total_return = actor_movies['return'].sum()
    movie_count = actor_movies['id'].nunique()
    average_return = actor_movies['return'].mean()
    
    # Convertir a tipos nativos de Python
    total_return = float(total_return)
    average_return = float(average_return)
    
    return f"El actor `{actor_name.title()}` ha participado de `{movie_count}` filmaciones, el mismo ha conseguido un retorno de `{total_return:.2f}` con un promedio de `{average_return:.2f}` por filmación*"


#Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

@app.get("/nombre_director/{nombre_director}")
def get_director(director_name: str):
    """
    Devuelve información resumida sobre las películas dirigidas por un director específico.

    Parameteros:
    director_name (str): El nombre del director a buscar en el DataFrame.

    Returns:
    Un diccionario con el nombre del director, el éxito total medido por el retorno, 
    y detalles de cada película dirigida (título, retorno individual, costo y ganancia, 
    calculando esta ultima como recaudacion menos presupuesto(revenue-budget)).
    """
    # Convertir el nombre del director a minúsculas
    director_name = director_name.lower()
    
    # Filtrar las películas dirigidas por el director
    director_movies = movies_df[movies_df['director'].str.lower() == director_name]
    
    if director_movies.empty:
        raise HTTPException(status_code=404, detail=f"Director '{director_name}' no encontrado en el dataset")
    
    # Calcular el éxito del director sumando los retornos de todas las películas
    total_return = director_movies['return'].sum()
    
    # Preparar los detalles de cada película del director
    movies_detalles = []
    for index, row in director_movies.iterrows():
        movie_details = {
            'title': row['title'],
            'return': row['return'],
            'cost': row['budget'],
            'ganancia': row['revenue'] - row['budget']
        }
        movies_detalles.append(movie_details)
    
    # Formatear el mensaje de retorno
    mensajefinal = {
        'director_name': director_name.title(),  # Capitalizar el nombre del director
        'total_return': total_return,
        'movies_details': movies_detalles
    }
    
    return mensajefinal


################################################################


# Definir la función get_recommendations
def get_recommendations(title, df= modelo_df, cosine_sim=cosine_sim):
    try:
        # Obtener el índice de la película que coincide con el título
        idx = df[df['title'].str.lower() == title.lower()].index[0]

        # Obtener los scores de similitud de todas las películas con esa película
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Ordenar las películas según la puntuación de similitud
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Obtener las 5 películas más similares (excepto la misma película)
        sim_scores = sim_scores[1:6]

        # Obtener los índices de las películas más similares
        movie_indices = [i[0] for i in sim_scores]

        # Retornar los títulos de las películas más similares
        return df['title'].iloc[movie_indices].tolist()
    except IndexError:
        raise HTTPException(status_code=404, detail=f"No se encontraron películas similares para '{title}'. Asegúrate de haber puesto correctamente el título.")


@app.get("/recomendacion/{titulo}", response_model=List[str])
def recomendacion(titulo: str):
    """
    Devuelve un listado de cinco películas para recomendar, en base al titulo,genero, y descripcion
    Sobre las 5000 mil peliculas con mejor promedio de votos.

    Parámetros:
    título (str): El título de la película a la que se desea obtener recomendaciones."""

    recommended_movies = get_recommendations(titulo, modelo_df, cosine_sim)
    return recommended_movies
