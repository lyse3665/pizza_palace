from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_user, models_order, models_favorite, models_pizza
# Bcrypt import
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) # We are creating an object called bcrypt,
# which is made by invoking the function Bcrypt with our app as an argument.

# Get Routes
# Route for rendering the Registration page.
@app.route('/')
def registration():
    return render_template('registration.html')

# Route for rendering the Login page.
@app.route('/user_login')
def user_login():
    return render_template('login.html')

# Route for logging a user out.
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/user_login')

# Route for rendering the Homepage.
@app.route('/homepage')
def check_session():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session ['user_id']
    }
    return render_template('homepage.html', user=models_user.User.get_user_by_id(data))

# Route for rendering the Craft Pizza page.
@app.route('/craft_pizza')
def craft_pizza():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('craft_pizza.html')

# Route for rendering the Re-order Pizza page.
# @app.route('/craft_fav_pizza')
# def craft_fav_pizza():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         'id': session['user_id']
#     }
#     user_favorite = models_favorite.Favorite.get_user_favortie(data)
#     return render_template('reorder_fav.html', user_favorite=user_favorite)

@app.route('/craft_fav_pizza')
def craft_fav_pizza():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    favorite = models_favorite.Favorite.get_all_user_favorites(data)
    user_favorite =Favorite.get_user_favortie(data)
    return render_template('reorder.html', user_favorite=user_favorite)

# Route for rendering the Surprise Pizza page.
@app.route('/craft_surprise_pizza')
def craft_surprise_pizza():
    if 'user_id' not in session:
        return redirect('/logout')
    crusts = models_pizza.Pizza.random_crusts()
    meats = models_pizza.Pizza.random_meats()
    cheeses = models_pizza.Pizza.random_cheeses()
    sauces = models_pizza.Pizza.random_sauces()
    toppings = models_pizza.Pizza.random_toppings()
    return render_template('craft_surprise_pizza.html', crusts=crusts, meats=meats,
    cheeses=cheeses, sauces=sauces, toppings=toppings)

@app.route('/order')
def order():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    order=models_order.Order.get_one_order_by_id(data)
    return render_template('order.html', order=order)

# Route for rendering the Account page.
@app.route('/account')
def account():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    orders = models_order.Order.get_all_user_orders(data)
    user = models_user.User.get_user_by_id(data)
    return render_template('account.html', orders=orders, user=user)

# Post Routes
# Route for registering a user.
@app.post('/register')
def register():
    if not models_user.User.validate_user(request.form):
        # We redirect to the template with the form.
        return redirect('/')
    # Create data object for hashing a user's password.
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "address": request.form['address'],
        "city": request.form['city'],
        "state": request.form['state'],
        "password": bcrypt.generate_password_hash(request.form['password']), # Function for generating the hash.
        "confirm_password": request.form['confirm_password']
    }
    """We save the data to the database and are returned a user's id. We put
    this user id into session because when we go back to the dashboard we want
    to check if the user is in session and if they are not we redirect them.
    This is how we keep our applications safe."""
    id = models_user.User.save_new_user(data)
    session['user_id'] = id
    return redirect('/homepage')

# Route for logging a user in.
@app.post('/login')
def login():
    user = models_user.User.get_user_by_email(request.form)
    if not user:
        flash("Invalid email or password.", "login")
        return redirect('/user_login')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid email or password.", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/homepage')

# Route for editing a user's infromation.
@app.post('/update_user')
def update_user():
    if 'user_id' not in session:
        return redirect('/logout')
    if not models_user.User.edit_user_validation(request.form):
        return redirect('/account')
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'address': request.form['address'],
        'city': request.form['city'],
        'state': request.form['state']
    }
    models_user.User.update_user(data)
    return redirect('/homepage')