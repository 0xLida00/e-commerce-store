# E-Commerce Store

This is a simple e-commerce store built using Flask, HTML, CSS, and JavaScript.

## Installation
1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Run the Flask application.

## Features
- Browse products
- View product details
- Add products to cart (basic functionality)
- About and Contact pages

## Prerequisites
- Python 3.7 or higher
- Virtual environment (recommended)

## Installation Steps
1. **Clone the Repository**:
    git clone https://github.com/0xLida00/ecommerce_store.git
    cd ecommerce_store

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
	•	Explore the About and Contact pages for more information about the store.

## Customization
	•	Products: You can modify the products by editing the products list in app.py.
	•	Styles: Customize the look and feel by editing the CSS in static/css/style.css.
	•	JavaScript: Add interactive features by modifying static/js/script.js.

## Requirements
`requirements.txt`
    Flask~=2.0
    Gunicorn

## Contributing
We welcome contributions to improve the Interactive Quiz App. If you have suggestions for new features or improvements, please feel free to submit a pull request or open an issue.
Alternatively, please contact Lidao Betema at rodrigue.betema@gmail.com

## Project Structure
```plaintext
ecommerce_store/
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── img/
│   │   ├── background.jpg
│   │   ├── favicon.ico
│   │   └── storelogo.png
│   │   └── cushion.png
│   │   └── yoga_mat.png
│   │   └── water_bottle.png
│   │   └── wireless_charger.png
│   │   └── earbuds.png
│   │   └── laptop_stand.png
│   │   └── blender.png
│   │   └── headset.png
│   │   └── smartwatch.png
│   │   └── drone.png
│   │   └── adjustable_dumbbells.png
│   │   └── digital_picture_frame.png
│   │   └── air_purifier.png
│   │   └── doorbell.png
│   │   └── vacuum_cleaner.png
│   │   └── thermostat.png
│   │   └── gaming_console.png
│   │   └── kettle.png
│   │   └── gaming_mouse.png
│   │   └── desk_chair.png
│   │   └── speaker.png
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── products.html
│   ├── products_details.html
│   ├── search_results.html
│   ├── cart.html
│   ├── checkout.html
│   ├── about.html
│   └── contact.html
├── README.md
├── requirements.txt