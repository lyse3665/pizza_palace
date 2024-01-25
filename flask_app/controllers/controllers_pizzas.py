from flask_app import app
from flask import redirect, request, session
from flask_app.models import models_pizza, models_order

# Post Routes
# Route for creating a pizza.
@app.post('/create_pizza')
def create_pizza():
    if 'user_id' not in session:
        return redirect('/logout')
    if not models_pizza.Pizza.validate_pizza(request.form):
        return redirect('/craft_pizza')

    pizza = {
        'method': request.form['method'],
        'size': request.form['size'],
        'quantity': request.form['quantity'],
        'crust': request.form['crust'],
        'sauce': request.form['sauce'],
        'cheese': request.form['cheese'],
        'meat': request.form['meat'],
        'topping': request.form['topping'],
        'order_id': session['user_id']
    }

    models_pizza.Pizza.save_new_pizza(pizza)

    delivery = float(request.form['method'])
    price = float(request.form['size'])
    quantity = float(request.form['quantity'])
    tax = (price * quantity + delivery) * .07
    total_price = round(price * quantity + delivery + tax, 2)
    total = total_price

    order = {
        'method': request.form['method'],
        'size': request.form['size'],
        'crust': request.form['crust'],
        'quantity': request.form['quantity'],
        'meat': request.form['meat'],
        'cheese': request.form['cheese'],
        'sauce': request.form['sauce'],
        'topping': request.form['topping'],
        'total': total,
        'user_id': session['user_id']
    }
    models_order.Order.save_new_order(order)
    return redirect('/homepage')


# Route for creating a favorited pizza.
@app.post('/create_craft_pizza')
def create_fav_pizza():
    if 'user_id' not in session:
        return redirect('/logout')
    if not models_pizza.Pizza.validate_pizza(request.form):
        return redirect('/craft_fav_pizza')
    pizza = {
        'method': request.form['method'],
        'size': request.form['size'],
        'crust': request.form['crust'],
        'quantity': request.form['quantity'],
        'meat': request.form['meat'],
        'cheese': request.form['cheese'],
        'sauce': request.form['sauce'],
        'topping': request.form['topping'],
        'order_id': session['user_id']
    }
    models_pizza.Pizza.save_new_pizza(pizza)

    delivery = float(request.form['method'])
    price = float(request.form['size'])
    quantity = float(request.form['quantity'])
    tax = (price * quantity + delivery) * .07
    total_price = round(price * quantity + delivery + tax, 2)
    total = total_price


    order = {
        'total': total,
        'method': request.form['method'],
        'size': request.form['size'],
        'crust': request.form['crust'],
        'quantity': request.form['quantity'],
        'meat': request.form['meat'],
        'cheese': request.form['cheese'],
        'sauce': request.form['sauce'],
        'topping': request.form['topping'],
        'user_id': session['user_id']
    }
    models_order.Order.save_new_order(order)
    return redirect('/homepage')

# Route for creating a Surprise pizza.
@app.post('/create_random_pizza')
def create_random_pizza():
    if 'user_id' not in session:
        return redirect('/logout')
    if not models_pizza.Pizza.validate_pizza(request.form):
        return redirect('/craft_fav_pizza')

    pizza = {
        'method': request.form['method'],
        'size': request.form['size'],
        'crust': request.form['crust'],
        'quantity': request.form['quantity'],
        'meat': request.form['meat'],
        'cheese': request.form['cheese'],
        'sauce': request.form['sauce'],
        'topping': request.form['topping'],
        'order_id': session['user_id']
    }
    models_pizza.Pizza.save_new_pizza(pizza)

    delivery = float(request.form['method'])
    price = float(request.form['size'])
    quantity = float(request.form['quantity'])
    tax = (price * quantity + delivery) * .07
    total_price = round(price * quantity + delivery + tax, 2)
    total = total_price


    order = {
        'total': total,
        'method': request.form['method'],
        'size': request.form['size'],
        'crust': request.form['crust'],
        'quantity': request.form['quantity'],
        'meat': request.form['meat'],
        'cheese': request.form['cheese'],
        'sauce': request.form['sauce'],
        'topping': request.form['topping'],
        'user_id': session['user_id']
    }
    models_order.Order.save_new_order(order)
    return redirect('/homepage')