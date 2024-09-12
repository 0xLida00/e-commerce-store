# e-commerce-store
This repository contains an e-commerce web app built with Python and Flask. Users can browse products, add items to their cart, and checkout. Features include live cart updates, product detail pages, and cart management, demonstrating Flask routing, sessions, and Jinja2 templates.

## Installation
1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Run the Flask application.

## Features
- Browse products
- View product details
- Add products to cart (basic functionality)
- Remove product from the cart
- About Us and Contact Us pages

## Prerequisites
- Python 3.7 or higher
- Virtual environment (recommended)

## Installation Steps
1. **Clone the Repository**:
    git clone https://github.com/0xLida00/e-commerce-store
    cd e-commerce-store

2. **Create a Virtual Environment**:
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**:
    Install the required Python packages using `pip`:
       pip install -r requirements.txt

4. **Run the Application**:
    Start the Flask development server:
    flask run
    The application will be available at `http://127.0.0.1:5000`.

## Usage
	•	Visit the homepage to browse products.
	•	Click on a product to view its details.
	•	Add products to the cart and view the cart contents.
	•	Explore the About us and Contact Us pages for more information about the store.

## Customization
	•	Products: You can modify the products by editing the products list in app.py.
	•	Styles: Customize the look and feel by editing the CSS in static/css/style.css.
	•	JavaScript: Add interactive features by modifying static/js/script.js.

## Requirements
`requirements.txt`
    Flask~=2.0
    Gunicorn

## Contributing
We welcome contributions to improve the e-commerce-store site. If you have suggestions for new features or improvements, please feel free to submit a pull request or open an issue. Alternatively, please contact Lidao Betema at rodrigue.betema@gmail.com

## Project Structure
e-commerce_store/
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── img/
│   │   └── script.js
│   │   └── script.js
│   │   └── script.js
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── products.html
│   ├── products_details.html
│   ├── cart.html
│   ├── checkout.html
│   ├── about.html
│   └── contact.html
├── README.md
├── requirements.txt