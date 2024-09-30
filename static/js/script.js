document.addEventListener('DOMContentLoaded', function () {
    updateCartPreview();
    const imageModal = document.getElementById('image-modal');
    const modalImg = document.getElementById('modal-img');
    const closeImageModal = document.getElementsByClassName('modal-close')[0];

    const images = document.querySelectorAll('.product-image');
    images.forEach(function (image) {
        image.addEventListener('click', function (event) {
            event.preventDefault();
            imageModal.style.display = 'flex';
            modalImg.src = this.dataset.image;
        });
    });

    // Close the image modal when clicking the close button
    closeImageModal.onclick = function () {
        imageModal.style.display = 'none';
    };

    window.onclick = function (event) {
        if (event.target === imageModal) {
            imageModal.style.display = 'none';
        }
    };

    const addToCartButtons = document.querySelectorAll('.add-to-cart-button');
    addToCartButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const productId = this.dataset.productId;

            fetch('/add_to_cart/' + productId, {
                method: 'POST',
            })
            .then(response => response.json())
            .then(data => {
                const flashMessageDiv = document.getElementById('flash-message');
                flashMessageDiv.textContent = data.message;
                flashMessageDiv.classList.add('success');
                flashMessageDiv.style.display = 'block';

                setTimeout(() => {
                    flashMessageDiv.style.display = 'none';
                    flashMessageDiv.classList.remove('success');
                }, 4000);
                updateCartPreview();
            });
        });
    });

    function updateCartPreview() {
        fetch('/cart/data')
            .then(response => response.json())
            .then(data => {
                const cartPreview = document.getElementById('cart-preview');
                let html = '<h3>Cart Preview</h3>';
    
                if (data.cart_items.length > 0) {
                    html += '<ul>';
    
                    data.cart_items.forEach(item => {
                        html += `<li>${item.name}: €${item.price.toFixed(2)} x ${item.quantity} <a href="/decrease_quantity/${item.id}" class="remove-link">X</a></li>`;
                    });
    
                    html += '</ul>';
                    html += `<p><strong>Total: €${data.total}</strong></p>`;
                    html += '<a href="/cart" class="checkout-button">Proceed to Checkout</a>';
                } else {
                    html += '<p>Your cart is empty.</p>';
                }
                cartPreview.innerHTML = html;
    
                const removeLinks = document.querySelectorAll('.remove-link');
                removeLinks.forEach(link => {
                    link.addEventListener('click', function (event) {
                        event.preventDefault();

                        fetch(this.href, {
                            method: 'GET',
                        })
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            updateCartPreview();
                        })
                        .catch(error => {
                            console.error('There has been a problem with your fetch operation:', error);
                        });
                    });
                });
            });
    }

    // Payment Modal Code
    const paymentModal = document.getElementById('payment-modal');
    const checkoutButton = document.getElementById('checkout-button');
    const closePaymentModalButton = document.querySelector('.modal-close');
    const paymentForm = document.getElementById('payment-form');

    const openPaymentModal = () => {
        paymentModal.style.display = 'flex';
    };

    const closePaymentModal = () => {
        paymentModal.style.display = 'none';
    };

    // Close the payment modal if the user clicks outside the modal content
    const outsidePaymentModalClick = (event) => {
        if (event.target === paymentModal) {
            closePaymentModal();
        }
    };

    // Handle payment form submission
    const handlePaymentFormSubmit = (event) => {
        event.preventDefault();

        const fullName = document.getElementById('full-name').value;
        const cardNumber = document.getElementById('card-number').value;
        const expirationDate = document.getElementById('expiration-date').value;
        const cvv = document.getElementById('cvv').value;
        const amount = document.getElementById('amount').value;
        const saveCard = document.getElementById('save-card').checked;

        clearCart()
            .then(data => {
                if (data.success) {
                    window.location.href = '/checkout'; 
                } else {
                    console.error('Failed to clear the cart');
                }
            })
            .catch(error => {
                console.error('Error clearing the cart:', error);
            });

        closePaymentModal();
    };

    const clearCart = () => {
        return fetch('/clear_cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(response => response.json());
    };

    paymentModal.style.display = 'none';

    checkoutButton.addEventListener('click', openPaymentModal);
    closePaymentModalButton.addEventListener('click', closePaymentModal);
    window.addEventListener('click', outsidePaymentModalClick);
    paymentForm.addEventListener('submit', handlePaymentFormSubmit);
});