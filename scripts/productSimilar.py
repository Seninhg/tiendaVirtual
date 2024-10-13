import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Definir la función para calcular similitud de coseno
def calcular_similitud(nombre_del_producto, data):
    # Vectorizar los nombres de los productos
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(data['nombre'])

    # Combinar características
    features = np.column_stack([tfidf_matrix.toarray(), data['calificacion'], data['precio_descuento'], data['precio_actual']])

    # Calcular la matriz de similitud de coseno
    similarity_matrix = cosine_similarity(features)

    # Obtener el índice del producto dado
    product_index = data[data['nombre'] == nombre_del_producto].index[0]

    # Obtener las similitudes con otros productos
    product_similarities = similarity_matrix[product_index]

    # Obtener los índices de los productos más similares
    most_similar_products_indices = np.argsort(-product_similarities)

    #excluimos el producto actual| obtenemos los 10 productos más similares
    most_similar_products_indices = most_similar_products_indices[most_similar_products_indices != product_index][:20]

    # Obtener los productos más similares con todas sus columnas
    most_similar_products = data.loc[most_similar_products_indices]

    return most_similar_products



def obtenerSimilares(id, data):
    nombreProducto = data.loc[data['id_producto'] == id, 'nombre'].values[0]
    most_similar_products = calcular_similitud(nombreProducto, data)
    #no retornamos los datos en JSON, sino en un DataFrame, como Dios los trajo al mundo
    return most_similar_products
