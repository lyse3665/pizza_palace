from flask_app import app
from flask import redirect, request, session
from flask_app.models import models_favorite

# Post Routes
@app.post('/update_favorite')
def update_favortie():
    if 'user_id' not in session:
        return redirect('/logout')
    favorite = {
        'size': request.form['size'],
        'crust': request.form['crust'],
        'meat': request.form['meat'],
        'cheese': request.form['cheese'],
        'sauce': request.form['sauce'],
        'topping': request.form['topping'],
        'user_id': session['user_id'],
        'order_id': request.form['order_id']
    }
    models_favorite.Favorite.save_new_favorite(favorite)
    return redirect('/homepage')

