from flask_app import app
from flask_app.controllers import controllers_users, controllers_pizzas, controllers_orders, controllers_favorites





if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)