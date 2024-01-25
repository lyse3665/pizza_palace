from flask_app.config.mysqlconnection import connectToMySQL

# Database name
db = "pizzeria"

# Order class.
class Order:
    def __init__(self, data):
        self.id = data['id']
        self.total = data['total']
        self.method = data['method']
        self.size = data['size']
        self.crust = data['crust']
        self.quantity = data['quantity']
        self.meat = data['meat']
        self.cheese = data['cheese']
        self.sauce = data['sauce']
        self.topping = data['topping']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Classmethod for saving a new order
    @classmethod
    def save_new_order(cls, data):
        query = """INSERT INTO orders (total, method, size, crust, quantity, meat, cheese, sauce, topping, user_id)
                VALUES (%(total)s, %(method)s, %(size)s, %(crust)s, %(quantity)s, %(meat)s, %(cheese)s, %(sauce)s, %(topping)s, %(user_id)s);"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting all the orders from a specific user.
    @classmethod
    def get_all_user_orders(cls, data):
        query = """SELECT * FROM orders WHERE user_id = %(id)s;""" # This query needs adjusted.
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        customer_orders = []
        for order in results:
            print(order)
            customer_orders.append(cls(order))
        return customer_orders

    # Classmethod for getting a order by id.
    @classmethod
    def get_one_order_by_id(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    # Classmethod for deleting a order.
    @classmethod
    def destroy_order(cls, data):
        query = "DELETE FROM orders WHERE id = %(id)s AND user_id = %(user_id)s;"
        return connectToMySQL(db).query_db(query, data)
