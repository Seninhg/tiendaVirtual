//Componentes para la aplicación

export const Producto = (producto) => {
    const productoElement = document.createElement('div');
    productoElement.classList.add('producto');

    productoElement.setAttribute('data-id', producto.id_producto); //identificador del producto

    productoElement.innerHTML = `
        <img src="${producto.imagen}" alt="${producto.nombre}">
        <h3>${producto.nombre}</h3>
        <div class="product_info">
            <p>Categoría: ${producto.categoria}</p>
            <p>Subcategoría: ${producto.sub_categoria}</p>
            <p>Calificación: ${producto.calificacion}</p>
            <p class="precio">Precio Actual: $${producto.precio_actual}</p>
            <p class="precio-descuento">Precio Descuento: $${producto.precio_descuento}</p>
        </div>
        <button>Agregar al carrito</button>
    `;
    return productoElement;
}

/**
 * Componente para mostrar productos similares
 * Es una versión más simple, solo muestra la imagen, nombre y precio
 */

export const SimpleProducto = (producto) => {
    const productItem = document.createElement('div');
    productItem.classList.add('similar-product-item');

    productItem.setAttribute('data-id', producto.id_producto);

    productItem.innerHTML = `
    <img src="${producto.imagen}" alt="${producto.nombre}" style="height: 150px; object-fit: cover;">
    <p class="product-name">${producto.nombre.length > 40 ? producto.nombre.substring(0, 37) + '...' : producto.nombre}</p>
    <p class="price">
        S/ ${producto.precio_actual}
        ${producto.precio_descuento ? `<span class="old-price">S/ ${producto.precio_descuento}</span>` : ''}
    </p>
`;

    return productItem;
}