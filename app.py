from flask import Flask, flash, render_template, redirect, url_for, session, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = '9f2c687aaef44d3eebfc8e58a13a99df'

products = [
    {'id': 1, 'name': 'LuxeComfort Cushion', 'description': 'Cozy, textured cushion with vibrant colors', 'price': 29.99, 'image_url': '/static/img/cushion.png'},
    {'id': 2, 'name': 'UltraGrip Yoga Mat', 'description': 'Textured yoga mat with vivid color on the floor', 'price': 49.99, 'image_url': '/static/img/yoga_mat.png'},
    {'id': 3, 'name': 'Eco-Friendly Bottle', 'description': 'Reusable water with earthy bottle with bamboo lid', 'price': 19.99, 'image_url': '/static/img/water_bottle.png'},
    {'id': 4, 'name': 'Charging Pad', 'description': 'A modern white wireless charger in white', 'price': 25.99, 'image_url': '/static/img/wireless_charger.png'},
    {'id': 5, 'name': 'Smart Earbuds', 'description': 'Compact earbuds with a futuristic design', 'price': 34.99, 'image_url': '/static/img/earbuds.png'},
    {'id': 6, 'name': 'Adjustable Stand', 'description': 'A modern, aluminum laptop stand holding a laptop', 'price': 59.99, 'image_url': '/static/img/laptop_stand.png'},
    {'id': 7, 'name': 'Blender', 'description': 'A powerful blender in a kitchen setting', 'price': 39.99, 'image_url': '/static/img/blender.png'},
    {'id': 8, 'name': 'AntiNoise Headset', 'description': 'A high-end over-ear headset on a table', 'price': 49.99, 'image_url': '/static/img/headset.png'},
    {'id': 9, 'name': 'Smartwatch', 'description': 'A sleek smartwatch with touch screen', 'price': 29.99, 'image_url': '/static/img/smartwatch.png'},
    {'id': 10, 'name': 'HD Camera Drone', 'description': 'A sleek drone flying high over a scenic landscape', 'price': 19.99, 'image_url': '/static/img/drone.png'},
    {'id': 11, 'name': 'Adjustable Weight', 'description': 'Adjustable dumbbells in a home gym setting', 'price': 59.99, 'image_url': '/static/img/adjustable_dumbbells.png'},
    {'id': 12, 'name': 'Digital Picture Frame', 'description': 'A digital picture frame displaying an image', 'price': 24.99, 'image_url': '/static/img/digital_picture_frame.png'},
    {'id': 13, 'name': 'Air Purifier', 'description': 'A stylish air purifier on a living room table', 'price': 44.99, 'image_url': '/static/img/air_purifier.png'},
    {'id': 14, 'name': 'Doorbell Camera', 'description': 'A compact, modern doorbell camera mounted', 'price': 54.99, 'image_url': '/static/img/doorbell.png'},
    {'id': 15, 'name': 'Vacuum Cleaner', 'description': 'A robot vacuum cleaner moving across a floor', 'price': 64.99, 'image_url': '/static/img/vacuum_cleaner.png'},
    {'id': 16, 'name': 'Smart Thermostat', 'description': 'A modern smart thermostat mounted on a wall', 'price': 44.99, 'image_url': '/static/img/thermostat.png'},
    {'id': 17, 'name': 'Gaming Console', 'description': 'A white gaming console on a gaming desk', 'price': 84.99, 'image_url': '/static/img/gaming_console.png'},
    {'id': 18, 'name': 'Electric Kettle', 'description': 'A modern stainless electric kettle on counter', 'price': 94.99, 'image_url': '/static/img/kettle.png'},
    {'id': 19, 'name': 'Gaming Mouse', 'description': 'A high-performance glowing wireless gaming mouse', 'price': 35.99, 'image_url': '/static/img/gaming_mouse.png'},
    {'id': 20, 'name': 'Ergonomic Chair', 'description': 'A modern ergonomic desk chair in a stylish office', 'price': 134.99, 'image_url': '/static/img/desk_chair.png'},
    {'id': 21, 'name': 'Bluetooth Speaker', 'description': 'A compact, waterproof Bluetooth speaker by a poolside', 'price': 44.99, 'image_url': '/static/img/speaker.png'},
]

def initialize_cart():
    if 'cart' not in session:
        session['cart'] = []

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    '''Renders the homepage, initializes the cart, and calculates total cart value.'''
    initialize_cart()
    total = sum(item['price'] * item['quantity'] for item in session['cart'])
    total = "{:.2f}".format(total)
    cart_items = session['cart']
    return render_template('index.html', products=products, cart_items=cart_items, total=total)

@app.route('/products')
def view_products():
    '''Displays the product listing page, initializes the cart, and calculates total cart value.'''
    initialize_cart()
    total = sum(item['price'] * item['quantity'] for item in session['cart'])
    total = "{:.2f}".format(total)
    cart_items = session['cart']
    return render_template('products.html', products=products, cart_items=cart_items, total=total)

@app.route('/product/<int:product_id>')
def view_product_details(product_id):
    '''Shows details for a specific product, initializes the cart, and checks if the product exists.'''
    initialize_cart()
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return redirect(url_for('index'))
    total = sum(item['price'] * item['quantity'] for item in session['cart'])
    total = "{:.2f}".format(total)
    cart_items = session['cart']
    return render_template('product_details.html', product=product, cart_items=cart_items, total=total)

@app.route('/cart')
def cart_page():
    '''Displays the cart page with the current items and total cart value.'''
    initialize_cart()
    total = sum(item['price'] * item['quantity'] for item in session['cart'])
    total = "{:.2f}".format(total)
    return render_template('cart.html', cart=session['cart'], total=total)

@app.route('/cart/data', methods=['GET'])
def cart_data():
    '''Returns the cart data as JSON.'''
    initialize_cart()
    cart_items = session['cart']
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    total = "{:.2f}".format(total)
    return jsonify(cart_items=cart_items, total=total)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    '''Adds a product to the cart or increases its quantity if it's already in the cart.'''
    initialize_cart()
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        # Check if product is already in the cart
        for item in session['cart']:
            if item['id'] == product_id:
                # Add 'quantity' key if it's not present
                if 'quantity' not in item:
                    item['quantity'] = 1
                # Increase quantity if product is already in the cart
                item['quantity'] += 1
                session.modified = True
                return jsonify({"success": True, "message": "Product quantity increased."})
        else:
            # Add product to cart if it's not already in the cart
            product['quantity'] = 1
            session['cart'].append(product)
            session.modified = True
            return jsonify({"success": True, "message": "Product added to cart."})

    return jsonify({"success": False, "message": "Product not found."})

@app.route('/decrease_quantity/<int:product_id>')
def decrease_quantity(product_id):
    '''Reduces the quantity of a product in the cart or removes it if the quantity is 1.'''
    initialize_cart()
    for item in session['cart']:
        if item['id'] == product_id:
            if item['quantity'] > 1:
                # Decrease quantity if more than one is in the cart
                item['quantity'] -= 1
                session.modified = True
                break
            else:
                # Remove product completely if quantity is 1
                session['cart'].remove(item)
                session.modified = True
                break
    next_page = request.args.get('next')
    return redirect(next_page or url_for('cart_page'))

@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    '''Clears all products from the cart and sends a success response.'''
    session['cart'] = []
    session.modified = True
    return jsonify({"success": True})

@app.route('/process_payment', methods=['POST'])
def process_payment():
    '''Processes payment, validates input, and clears the cart upon successful payment.'''
    data = request.get_json()
    
    # Mock payment processing logic
    full_name = data.get('fullName')
    card_number = data.get('cardNumber')
    expiration_date = data.get('expirationDate')
    cvv = data.get('cvv')
    amount = data.get('amount')

    # For now, we assume the payment is successful.

    session['cart'] = []
    session.modified = True
    return jsonify({"success": True, "message": "Payment processed successfully"})

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    '''Removes a specific product from the cart based on its product ID.'''
    initialize_cart()
    session['cart'] = [item for item in session['cart'] if item['id'] != product_id]
    session.modified = True
    return jsonify({'message': 'Product removed from cart'})

@app.route('/search')
def search():
    '''Searches for products by name or description and displays the result.'''
    query = request.args.get('query', '')
    if query:
        search_results = [product for product in products if query.lower() in product['name'].lower() or query.lower() in product['description'].lower()]
    else:
        search_results = []

    initialize_cart()
    total = sum(item['price'] * item['quantity'] for item in session['cart'])
    total = "{:.2f}".format(total)
    cart_items = session['cart']

    return render_template('search_results.html', products=search_results, query=query, cart_items=cart_items, total=total)

@app.route('/checkout')
def checkout():
    '''Clears the cart and displays a checkout confirmation message.'''
    initialize_cart()
    session['cart'] = []
    session.modified = True
    return render_template('checkout.html', message="Your payment has been received! Your package will be shipped shortly and you will be notified.")

@app.route('/contact', methods=['GET'])
def contact():
    '''Displays the contact page with a contact form.'''
    return render_template('contact.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact_submit():
    '''Handles contact form submission and displays a success message.'''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        flash('Thank you for reaching out! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/about')
def about():
    '''Displays the About page with company information.'''
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)