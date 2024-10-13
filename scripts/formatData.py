import pandas as pd

data = pd.read_csv("dataset/electronics.csv", low_memory=False)

# Se quitan las columnas innecesarias
data = data.drop('link', axis=1)
data = data.drop('no_of_ratings', axis=1)

#Eliminación de nulos
data = data.dropna()

data.isnull().sum()

# Eliminación del caracter de la rupia china, ya que molesta la normalización de los datos al ser de tipo objeto
data['actual_price'] = data['actual_price'].str.replace('₹', '')
data['discount_price'] = data['discount_price'].str.replace('₹', '')
#%%
# Conversión a valores numericos
data[["ratings", "discount_price", "actual_price"]] = data[["ratings", "discount_price", "actual_price"]].apply(pd.to_numeric, errors='coerce')

data = data.dropna(subset=["ratings", "discount_price", "actual_price"])
#%%
#Conversión a valores flotantes
data[["ratings", "discount_price", "actual_price"]] = data[["ratings", "discount_price", "actual_price"]].astype(float)
#%%
# Traducción de columnas
data.columns = ['nombre', 'categoria', "sub_categoria", "imagen", "calificacion", "precio_descuento", "precio_actual"]


# Generación de identificador único autoincrementable
data['id_producto'] = range(1, len(data) + 1)

data.to_csv("dataset/dataFormated.csv", index=False)