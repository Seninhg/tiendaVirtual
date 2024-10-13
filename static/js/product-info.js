const $btn_addCart = document.querySelector('#btn-add-cart');

$btn_addCart.addEventListener('click', (e) => {
    alert('No te emociones, aún no se puede agregar productos al carrito');
});


const $similar_products = document.querySelector('#similar-products');
$similar_products.addEventListener('click', (e) => {

    if (e.target.tagName == 'IMG' || e.target.tagName == 'P') {
        const $product = e.target.parentElement;
        const id = $product.getAttribute('data-id');
        window.location.href = `/producto/${id}`;
    }
});