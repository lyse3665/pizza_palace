from flask_app import app
from flask import redirect, session
from flask_app.models import models_order, models_pizza


@app.get('/destroy_order/pizza/<int:id>')
def destroy_order_and_pizza(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id,
        'user_id': session['user_id']
    }
    
    models_order.Order.destroy_order(data)
    return redirect('/homepage')


@app.post('/create_order')
def create_order():
    if 'user_id' not in session:
        return redirect('/logout')
    order = {
        'method': session['method'],
        'quantity': session['quantity'],
        'size': session['size'],
        'crust': session['crust'],
        'meat': session['meat'],
        'cheese': session['cheese'],
        'sauce': session['sauce'],
        'topping': session['topping'],
        'price': session['price'],
        'total': session['total'],
        'user_id': session['user_id']
    }
    models_order.Order.save_new_order(order)
    return redirect('/homepage')