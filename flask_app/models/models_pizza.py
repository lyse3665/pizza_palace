from flask_app.config.mysqlconnection import connectToMySQL
# Flash messages import
from flask import flash
# Random import
import random

# Database name
db = "pizzeria"

# Pizza class.
class Pizza:
    def __init__(self, data):
        self.id = data['id']
        self.method = data['method']
        self.size = data['size']
        self.crust = data['crust']
        self.quantity = data['quantity']
        self.meat = data['meat']
        self.cheese = data['cheese']
        self.sauce = data['sauce']
        self.topping = data['topping']
        self.order_id = data['order_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Classmethod for saving a new pizza.
    @classmethod
    def save_new_pizza(cls, data):
        query = """INSERT INTO pizzas (method, size, crust, quantity, meat, cheese, sauce, topping, order_id)
                VALUES (%(method)s, %(size)s, %(crust)s, %(quantity)s, %(meat)s, %(cheese)s, %(sauce)s, %(topping)s, %(order_id)s);"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting a pizza by it's ID.
    @classmethod
    def get_pizza_by_id(cls, data):
        query = "SELECT * FROM pizzas WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    # Classmethod for getting a deleting a pizza.
    @classmethod
    def destroy_pizza(cls, data):
        query = "Delete * FROM pizzas WHERE id = %(id)s and user_id = %(user_id)s;"
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting random crusts.
    @classmethod
    def random_crusts(cls):
        crusts = []
        thin_crust = ["Thin crust"]
        flatbread = ["Flatbread crust"]
        original = ["Original crust"]
        stuffed_crust = ["Stuffed crust"]
        cheese_crust = ["Cheese crust"]
        garlic_crust = ["Garlic crust"]
        deep_dish = ["Deep dish"]
        crusts.append(thin_crust)
        crusts.append(flatbread)
        crusts.append(original)
        crusts.append(stuffed_crust)
        crusts.append(cheese_crust)
        crusts.append(garlic_crust)
        crusts.append(deep_dish)
        return random.choice(crusts)

    # Classmethod for getting random sauces.
    @classmethod
    def random_sauces(cls):
        sauces = []
        traditional = ["Traditional"]
        buffalo = ["Buffalo"]
        alfredo = ["Alfredo"]
        bbq = ["BBQ"]
        sweet = ["Sweet"]
        sauces.append(traditional)
        sauces.append(buffalo)
        sauces.append(alfredo)
        sauces.append(bbq)
        sauces.append(sweet)
        return random.choice(sauces)

    # Classmethod for getting random cheeses.
    @classmethod
    def random_cheeses(cls):
        cheeses = []
        provolone = ["Provolone"]
        american = ["American"]
        mozzorella = ["Mozzorella"]
        parmesan = ["Parmesan"]
        cheddar = ["Cheddar"]
        cheeses.append(provolone)
        cheeses.append(american)
        cheeses.append(mozzorella)
        cheeses.append(parmesan)
        cheeses.append(cheddar)
        return random.choice(cheeses)

    # Classmethod for getting random meats.
    @classmethod
    def random_meats(cls):
        meats = []
        pepperoni = ["Pepperoni"]
        sausage = ["Sausage"]
        ham = ["Ham"]
        chicken = ["Chicken"]
        bacon = ["Bacon"]
        meats.append(pepperoni)
        meats.append(sausage)
        meats.append(ham)
        meats.append(bacon)
        meats.append(chicken)
        return random.choice(meats)

    # Classmethod for getting random toppings.
    @classmethod
    def random_toppings(cls):
        toppings = []
        onions = ["Onions"]
        peppers = ["Peppers"]
        mushrooms = ["Mushrooms"]
        olives = ["Olives"]
        pineapples = ["Pineapples"]
        toppings.append(onions)
        toppings.append(peppers)
        toppings.append(mushrooms)
        toppings.append(olives)
        toppings.append(pineapples)
        return random.choice(toppings)

    # Staticmethod for validating a pizza.
    @staticmethod
    def validate_pizza(data):
        # Set is_valid to True.
        is_valid = True
        # Test if the method is selected.
        if data['method'] == '':
            flash("Method is required", "pizza")
            is_valid = False
        # Test if size is selected.
        if data['size'] == '':
            flash("Size is required.", "pizza")
            is_valid = False
        # Test if crust is selected.
        if data['crust'] == '':
            flash("Crust is required.", "pizza")
            is_valid = False
        # Test if quantity is selected.
        if data['quantity'] == '':
            flash("Quantity is required.", "pizza")
            is_valid = False
        # Test if quantity is selected.
        if data['sauce'] == '':
            flash("Sauce is required.", "pizza")
            is_valid = False
        # Test if quantity is selected.
        if data['cheese'] == '':
            flash("Cheese is required.", "pizza")
            is_valid = False
        return is_valid