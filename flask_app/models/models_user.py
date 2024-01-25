from flask_app.config.mysqlconnection import connectToMySQL
# Flash messages import
from flask import flash
# REGEX import
import re
# Create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Database name
db = "pizzeria"

# User class.
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Classmethod for saving a new user.
    @classmethod
    def save_new_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, address, city, state, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(address)s, %(city)s, %(state)s, %(password)s);"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting a user by their email address.
    @classmethod
    def get_user_by_email(cls, data):
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # Classmethod for updating a user's details.
    @classmethod
    def update_user(cls, data):
        query = """UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, address=%(address)s,
                city=%(city)s, state=%(state)s WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query, data)

    # Classmethod for getting a user by their ID.
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    # Staticmethod for validating a user.
    @staticmethod
    def validate_user(data):
        # Set is_valid to True.
        is_valid = True
        # Test if the first name is at least 2 characters.
        if len(data['first_name']) < 2:
            flash("First name is required", "register")
            is_valid = False
        # Test if the last name is at at least 2 characters.
        if len(data['last_name']) < 2:
            flash("Last name is required.", "register")
            is_valid = False
        # Test whether email matches the  EMAIL_REGEX pattern.
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address." , "register")
            is_valid = False
        query = """SELECT * FROM users
                WHERE email = %(email)s;"""
        results = connectToMySQL(db).query_db(query, data)
        # Test if the email is already being used.
        if len(results) != 0:
            flash("This email is already being used.", "register")
            is_valid = False
        # Test if the address is at at least 3 characters.
        if len(data['address']) < 3:
            flash("Address is required.", "register")
            is_valid = False
        # Test if the City is at at least 3 characters.
        if len(data['city']) < 3:
            flash("City is required.", "register")
            is_valid = False
        # Test if the state is not empty.
        if data['state'] == "":
            flash("State is required.", "register")
            is_valid = False
        # Test if the password is a certain amount of characters.
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.", "register")
            is_valid = False
        # Test if passwords match.
        if data['password'] != data['confirm_password']:
            flash("Password does not match.", "register")
            is_valid = False
        return is_valid

    # Staticmethod for validating the editing of a user.
    @staticmethod
    def edit_user_validation(data):
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
            flash("First name must be more 2 characters.", 'update_user')
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last name must be more 2 characters.", 'update_user')
        if len(data['email']) < 10:
            is_valid = False
            flash("Email must be at least 10 characters.", 'update_user')
        if len(data['address']) < 5:
            is_valid = False
            flash("Address must be at least 5 characters.", 'update_user')
        if len(data['city']) < 3:
            is_valid = False
            flash("City is required.", 'update_user')
        if data['state'] == '':
            is_valid = False
            flash("State is required.", 'update_user')
        return is_valid