document.addEventListener('DOMContentLoaded', function () {
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

    closeImageModal.onclick = function () {
        imageModal.style.display = 'none';
    };

    window.onclick = function (event) {
        if (event.target === imageModal) {
            imageModal.style.display = 'none';
        }
    };

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