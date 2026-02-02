from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/products')
def product_list():
    """Product listing page"""
    return render_template('product-list.html')

# @app.route('/product/<int:product_id>')
# def product_detail(product_id=None):
#     """Product detail page"""
#     return render_template('product-detail.html', product_id=product_id)

@app.route('/cart')
def cart():
    """Shopping cart page"""
    return render_template('cart.html')

@app.route('/wishlist')
def wishlist():
    """Wishlist page"""
    return render_template('wishlist.html')

@app.route('/checkout')
def checkout():
    """Checkout page"""
    return render_template('checkout.html')

@app.route('/contact')
def contact():
    """Contact us page"""
    return render_template('contact.html')

@app.route('/login')
def login():
    """Login page"""
    return render_template('login.html')

@app.route('/register')
def register():
    """Registration page"""
    return render_template('register.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()