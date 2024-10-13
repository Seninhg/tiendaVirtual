import {obtenerProductos} from "./request.js";

const $products_list = document.querySelector('#products-list');

$products_list.addEventListener('click', (e) => {
    if (e.target.tagName === 'BUTTON') {
        const id_producto = e.target.parentElement.getAttribute('data-id');

        alert(`No te emociones, aún no se puede agregar productos al carrito. Producto con id: ${id_producto}`);
    }


    /**
     * Se agrega la condición para que se pueda ver los detalles del producto
     * al hacer click en la imagen o en el nombre del producto
     * el usuario será redirigido a una página con mayor información del producto
     */
    if (e.target.tagName === 'IMG' || e.target.tagName === 'H3') { 
        const id_producto = e.target.parentElement.getAttribute('data-id');

        //regiridir a los usuarios a la página de detalles del producto
        window.location.href = `/producto/${id_producto}`;
    }
});



let currentPage = 1;
const perPage = 10; // Puedes ajustar el número de productos por página

document.addEventListener('DOMContentLoaded', function() { 
    const prevPageBtn = document.getElementById('prev-page');
    const nextPageBtn = document.getElementById('next-page');
    const pageNumberInput = document.getElementById('page-input');
    
    // Función para actualizar la paginación
    const actualizarPaginacion = (paginaActual, totalProductos) => {
        // Actualizar el valor del input con el número de la página actual
        pageNumberInput.value = paginaActual;

        // Deshabilitar el botón "Anterior" si estamos en la primera página
        prevPageBtn.disabled = paginaActual === 1;

        // Deshabilitar el botón "Siguiente" si no hay más productos en la página actual
        nextPageBtn.disabled = totalProductos < perPage;
    };

    const cargarProductos = async (page) => {
        try {
            // Obtener los productos de la API
            const totalProductos = await obtenerProductos(page, perPage);

            // Actualizar la paginación una vez cargados los productos
            actualizarPaginacion(page, totalProductos);
        } catch (error) {
            console.error('Error al cargar los productos:', error);
        }
    };

    // Listeners para botones de paginación
    prevPageBtn.addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            cargarProductos(currentPage);
        }
    });

    nextPageBtn.addEventListener('click', () => {
        currentPage++;
        cargarProductos(currentPage);
    });

    // Event listener para el input de número de página (cargar automáticamente al cambiar valor)
    pageNumberInput.addEventListener('change', () => {
        let selectedPage = parseInt(pageNumberInput.value);
        if (!isNaN(selectedPage) && selectedPage > 0) {
            currentPage = selectedPage;
            cargarProductos(currentPage);
        } else {
            pageNumberInput.value = currentPage; // Volver a la página actual si el número es inválido
        }
    });

    // Cargar la primera página de productos al iniciar
    cargarProductos(currentPage);
});