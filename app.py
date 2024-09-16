from flask import Flask, flash, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '9f2c687aaef44d3eebfc8e58a13a99df'

products = [
    {'id': 1, 'name': 'Product 1', 'description': 'This is a detailed description for product 1.', 'price': 29.99, 'image_url': '/static/img/product1.jpg'},
    {'id': 2, 'name': 'Product 2', 'description': 'This is a detailed description for product 2.', 'price': 49.99, 'image_url': '/static/img/product2.jpg'},
    {'id': 3, 'name': 'Product 3', 'description': 'This is a detailed description for product 3.', 'price': 19.99, 'image_url': '/static/img/product3.jpg'},
    {'id': 4, 'name': 'Product 4', 'description': 'This is a detailed description for product 4.', 'price': 25.99, 'image_url': '/static/img/product4.jpg'},
    {'id': 5, 'name': 'Product 5', 'description': 'This is a detailed description for product 5.', 'price': 34.99, 'image_url': '/static/img/product5.jpg'},
    {'id': 6, 'name': 'Product 6', 'description': 'This is a detailed description for product 6.', 'price': 59.99, 'image_url': '/static/img/product6.jpg'},
    {'id': 7, 'name': 'Product 7', 'description': 'This is a detailed description for product 7.', 'price': 39.99, 'image_url': '/static/img/product7.jpg'},
    {'id': 8, 'name': 'Product 8', 'description': 'This is a detailed description for product 8.', 'price': 49.99, 'image_url': '/static/img/product8.jpg'},
    {'id': 9, 'name': 'Product 9', 'description': 'This is a detailed description for product 9.', 'price': 29.99, 'image_url': '/static/img/product9.jpg'},
    {'id': 10, 'name': 'Product 10', 'description': 'This is a detailed description for product 10.', 'price': 19.99, 'image_url': '/static/img/product10.jpg'},
    {'id': 11, 'name': 'Product 11', 'description': 'This is a detailed description for product 11.', 'price': 24.99, 'image_url': '/static/img/product11.jpg'},
    {'id': 12, 'name': 'Product 12', 'description': 'This is a detailed description for product 12.', 'price': 34.99, 'image_url': '/static/img/product12.jpg'},
    {'id': 13, 'name': 'Product 13', 'description': 'This is a detailed description for product 13.', 'price': 44.99, 'image_url': '/static/img/product13.jpg'},
    {'id': 14, 'name': 'Product 14', 'description': 'This is a detailed description for product 14.', 'price': 54.99, 'image_url': '/static/img/product14.jpg'},
    {'id': 15, 'name': 'Product 15', 'description': 'This is a detailed description for product 15.', 'price': 64.99, 'image_url': '/static/img/product15.jpg'},
    {'id': 16, 'name': 'Product 16', 'description': 'This is a detailed description for product 16.', 'price': 74.99, 'image_url': '/static/img/product16.jpg'},
    {'id': 17, 'name': 'Product 17', 'description': 'This is a detailed description for product 17.', 'price': 84.99, 'image_url': '/static/img/product17.jpg'},
    {'id': 18, 'name': 'Product 18', 'description': 'This is a detailed description for product 18.', 'price': 94.99, 'image_url': '/static/img/product18.jpg'},
    {'id': 19, 'name': 'Product 19', 'description': 'This is a detailed description for product 19.', 'price': 104.99, 'image_url': '/static/img/product19.jpg'},
    {'id': 20, 'name': 'Product 20', 'description': 'This is a detailed description for product 20.', 'price': 114.99, 'image_url': '/static/img/product20.jpg'},
    {'id': 21, 'name': 'Product 21', 'description': 'This is a detailed description for product 21.', 'price': 124.99, 'image_url': '/static/img/product21.jpg'},
]

def initialize_cart():
    if 'cart' not in session:
        session['cart'] = []

@app.route('/')
def index():
    initialize_cart()
    total = sum(item['price'] for item in session['cart'])
    total = "{:.2f}".format(total)
    cart_items = session['cart']
    return render_template('index.html', products=products, cart_items=cart_items, total=total)

@app.route('/products')
def view_products():
    initialize_cart()
    total = sum(item['price'] for item in session['cart'])
    total = "{:.2f}".format(total)
    cart_items = session['cart']
    return render_template('products.html', products=products, cart_items=cart_items, total=total)

@app.route('/product/<int:product_id>')
def view_product_details(product_id):
    initialize_cart()
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return redirect(url_for('index'))
    total = sum(item['price'] for item in session['cart'])
    total = "{:.2f}".format(total)
    cart_items = session['cart']
    return render_template('product_details.html', product=product, cart_items=cart_items, total=total)

@app.route('/cart')
def cart_page():
    initialize_cart()
    total = sum(item['price'] for item in session['cart'])
    total = "{:.2f}".format(total)
    return render_template('cart.html', cart=session['cart'], total=total)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    if query:
        search_results = [product for product in products if query.lower() in product['name'].lower() or query.lower() in product['description'].lower()]
    else:
        search_results = []

    initialize_cart()
    total = sum(item['price'] for item in session['cart'])
    total = "{:.2f}".format(total)
    cart_items = session['cart']

    return render_template('search_results.html', products=search_results, query=query, cart_items=cart_items, total=total)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)