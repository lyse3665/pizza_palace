from flask_app.config.mysqlconnection import connectToMySQL

# Database name
db = "pizzeria"

# Favorite class.
class Favorite:
    def __init__(self, data):
        self.id = data['id']
        self.size = data['size']
        self.crust = data['crust']
        self.meat = data['meat']
        self.cheese = data['cheese']
        self.sauce = data['sauce']
        self.topping = data['topping']
        self.user_id = data['user_id']
        self.order_id = data['order_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Classmethod for saving a new favorite.
    @classmethod
    def save_new_favorite(cls, data):
        query = """INSERT INTO favorites (size, crust, meat, cheese, sauce, topping, user_id, order_id)
                VALUES (%(size)s, %(crust)s, %(meat)s, %(cheese)s, %(sauce)s, %(topping)s, %(user_id)s, %(order_id)s);"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting all of a user's favorties.
    @classmethod
    def get_all_user_favorites(cls, data):
        query = "SELECT * FROM favorites WHERE user_id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        user_favorites = []
        for favorite in results:
            print(favorite)
            user_favorites.append(cls(favorite))
        return user_favorites

    # Classmethod for getting a user's favorite pizza.
    @classmethod
    def get_user_favortie(cls, data):
        query = """SELECT * FROM favorites WHERE favorites.id = %(id)s AND order_id = %(order_id)s;"""
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return cls(results[0])