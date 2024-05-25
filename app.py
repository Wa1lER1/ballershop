from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

products = [
    {"id": 1, "name": "Jordan 10", "price": 200, "category": "Shoes", "image": "images/634e999fedf86841096b6367-nike-mens-air-jordan-10-retro-30th-bulls.jpg", "brand": "Jordan"},
    {"id": 2, "name": "Kyrie-small", "price": 150, "category": "Shoes", "image": "images/kyrie-small.png", "brand": "Nike"},
    {"id": 3, "name": "Jorban-small", "price": 130, "category": "Shoes", "image": "images/jordan-small.png", "brand": "Jordan"},
    {"id": 4, "name": "Kd-small", "price": 135, "category": "Shoes", "image": "images/kd-small.png", "brand": "Nike"},
    {"id": 5, "name": "Basketball clothes Los Angeles Lakers", "price": 200, "category": "Clothes", "image": "images/завантаження.jpg", "brand": "Nike"},
    {"id": 6, "name": "Basketball jersey Nike", "price": 100, "category": "Clothes", "image": "images/giannis-dri-fit-dna-basketball-jersey-hDp8Jh.png", "brand": "Nike"},
    {"id": 7, "name": "Basketball suit 3x1", "price": 80, "category": "Clothes", "image": "images/61IrjgYRu2L._AC_UF1000,1000_QL80_.jpg", "brand": "Other"},
    {"id": 8, "name": "BYU Basketball Unveils Uniform", "price": 150, "category": "Clothes", "image": "images/img_3409.jpg", "brand": "Nike"},
    {"id": 9, "name": "Basketball ball Meteor size 6", "price": 90, "category": "Basketballs", "image": "images/40248_1.jpg", "brand": "Other"},
    {"id": 10, "name": "Basketball ball Nike size 3", "price": 40, "category": "Basketballs", "image": "images/skills-basketball-size-3-YPTAr4ED.png", "brand": "Nike"},
    {"id": 11, "name": "Basketball ball Spalding size 7 ", "price": 90, "category": "Basketballs", "image": "images/spalding-nba-trainer-oversized-basketball-ball.jpg", "brand": "Spalding"},
    {"id": 12, "name": "Basketball ball Jordan gray size 8", "price": 110, "category": "Basketballs", "image": "images/jordan-playground-8p-basketball-wpMXj1.jpg", "brand": "Jordan"},
]
cart = []

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		selected_category = request.form.get('category')
		selected_brand = request.form.get('brand')
		filtered_products = products
		if selected_category:
			filtered_products = [product for product in products if product['category'] == selected_category]
		if selected_brand:
			filtered_products = [product for product in filtered_products if product['brand'] == selected_brand]
		else:
			filtered_products = products
		return render_template('index.html', products=filtered_products)
	return render_template('index.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
	product_id = int(request.form['product_id'])
	product = next((p for p in products if p['id'] == product_id), None)
	if product:
		cart.append(product)
		return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
	total_price = sum(product['price'] for product in cart)
	return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
	global cart
	cart = [product for product in cart if product['id'] != product_id]
	return redirect(url_for('view_cart'))

@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
	global cart
	thank_you = False
	total_price = sum(product['price'] for product in cart)
	if request.method == 'POST':
		phone = request.form.get('phone')
		email = request.form.get('email')
		name = request.form.get('name')
		surname = request.form.get('surname')
		if phone and email and name and surname:
			cart.clear()
			thank_you = True
	return render_template('checkout.html', cart=cart, thank_you=thank_you, total_price=total_price)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8001, debug=True)

