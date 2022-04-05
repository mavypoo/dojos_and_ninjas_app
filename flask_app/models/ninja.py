from flask_app.config.mysqlconnection import connectToMySQL # Allow us to connect to MySQL

from flask_app import app
from flask_app.models import dojo, ninja # Create dojos by doing dojo.Dojo()


class Ninja:
    schema_name = "dojos_and_ninjas_schemas" # Class variable holding the name of the schema we'll use 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos = [] # Place holding Many Flinks linked to this carrier 



    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id ) VALUES ( %(first_name)s, %(last_name)s , %(age)s, %(dojo_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.schema_name).query_db(query, data)


