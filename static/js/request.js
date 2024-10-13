import { Producto, SimpleProducto} from "./components.js";


const urlToFetch = 'http://localhost:8080';


export const obtenerProductos = async (page, perPage) => {
    const response = await fetch(`${urlToFetch}/api/producto?page=${page}&per_page=${perPage}`);
    const productosFetch = await response.json()

    //elemento del DOOM
    const $products_list = document.querySelector('#products-list');

    //limpiamos el contenedor de productos
    $products_list.innerHTML = '';

    const fragment = document.createDocumentFragment();
    productosFetch.content.forEach(producto => {
        const ProductoElement = Producto(producto);
        fragment.appendChild(ProductoElement);
    });
    $products_list.appendChild(fragment);

    return productosFetch.content.length;
}

const obtenerProductosSimilares = async (id) => {
    try{
        /**
         * Fetch para obtener los productos similares
         * El id es proporcionado como media query
         */
        const response = await fetch(`${urlToFetch}/api/productoSimilar?id=${id}`);
        const productosFetch = await response.json();

        console.log(productosFetch);

        if (productosFetch.error){
            throw new Error(productosFetch.error);
            return;
        }
        //elemento del DOOM
        const $similarProductsContainer = document.querySelector('#similar-products');
        const fragment = document.createDocumentFragment();
        productosFetch.content.forEach(producto => {
            const ProductoElement = SimpleProducto(producto);
            fragment.appendChild(ProductoElement);
        });
        $similarProductsContainer.appendChild(fragment);
    }catch(error){
        console.error(error);
    }
}


if (document.querySelector('#similar-products')) {
    //obtenemos el id del producto actual
    const $product_target = document.querySelector('#product_target');
    const id = $product_target.getAttribute('data-id');
    obtenerProductosSimilares(id);
}


if (document.querySelector('#products-list')){
    obtenerProductos();
}