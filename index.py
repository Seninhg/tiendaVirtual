from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from scripts.productSimilar import obtenerSimilares

app = Flask(__name__)
CORS(app)

# Verificar si el archivo existe para evitar errores
DATASET_PATH = 'dataset/dataFormated.csv'

def load_data():
    """Carga el dataset en un DataFrame, manejando errores."""
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(f"No se encontró el archivo {DATASET_PATH}")
    try:
        return pd.read_csv(DATASET_PATH)
    except Exception as e:
        raise ValueError(f"Error al leer el archivo CSV: {e}")

# Vistas
@app.route('/')
def index():
    return render_template("productos.html")

@app.route('/producto/<int:id>')
def producto(id):
    """
    Vista híbrida: renderiza la información del producto en el servidor,
    con datos adicionales cargados vía AJAX.
    """
    try:
        data = load_data()
        producto = data.loc[data['id_producto'] == id]

        if producto.empty:
            return render_template("404.html"), 404

        producto = producto.to_dict(orient='records')[0]
        return render_template("product-info.html", producto=producto)
    
    except FileNotFoundError as e:
        return render_template("error.html", message=str(e)), 500
    except Exception as e:
        return render_template("error.html", message=f"Error inesperado: {str(e)}"), 500

# API
@app.get('/api/producto')
def get_products():
    """API para obtener productos."""
    try:
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=25, type=int)
        
        if page <= 0 or per_page <= 0:
            return jsonify({'status': 'error', 'content': 'Parámetros de paginación inválidos'}), 400
        
        data = load_data()
        start = (page - 1) * per_page
        end = start + per_page
        
        paginated_data = data.iloc[start:end]
        result = paginated_data.to_dict(orient='records')
        
        return jsonify({'status': 'success', 'content': result})
    
    except FileNotFoundError as e:
        return jsonify({'status': 'error', 'content': str(e)}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'content': f"Error inesperado: {str(e)}"}), 500

@app.get('/api/producto/<int:id>')
def get_product(id):
    """API para obtener un producto por su ID."""
    try:
        data = load_data()
        producto = data.loc[data['id_producto'] == id]
        
        if producto.empty:
            return jsonify({'status': 'error', 'content': 'Producto no encontrado'}), 404
        
        result = producto.to_dict(orient='records')
        return jsonify({'status': 'success', 'content': result})
    
    except FileNotFoundError as e:
        return jsonify({'status': 'error', 'content': str(e)}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'content': f"Error inesperado: {str(e)}"}), 500

@app.get('/api/productoSimilar')
def get_similar_products():
    """API para obtener productos similares (aún no implementado completamente)."""
    id = request.args.get('id', type=int)
    if id is None:
        return jsonify({'status': 'error', 'content': 'ID no proporcionado'}), 400
    
    try:
        data = load_data()
        productosSimilares = obtenerSimilares(id, data) #el resultado es un DataFrame, ojito
        
        if productosSimilares.empty:
            return jsonify({'status': 'error', 'content': 'No se encontraron productos similares'}), 404

        result = productosSimilares.to_dict(orient='records')
        return jsonify({'status': 'success', 'content': result})
    except FileNotFoundError as e:
        return jsonify({'status': 'error', 'content': str(e)}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'content': f"Error inesperado: {str(e)}"}), 500




# Manejo de errores global
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'status': 'error', 'content': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'status': 'error', 'content': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True)
