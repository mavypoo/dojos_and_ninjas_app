#the connection to your schema will be done in your models file 

from flask_app.config.mysqlconnection import connectToMySQL # Allow us to connect to MySQL
# Might need to import your app in the future:
from flask_app import app

# Import other models as needed:
from flask_app.models.ninja import  Ninja # Create Ninja by doing ninja.Ninja()

class Dojo:
    schema_name = "dojos_and_ninjas_schemas" # Class variable holding the name of the schema we'll use 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = [] # Place holding Many Flinks linked to this carrier 

    # Use classmethods to interact with our database - where our queries will go
    

    # Show all the dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.schema_name).query_db(query) # No data parameter needed - nothing needed to query
        # Create an empty list to append our instance of dojos
        dojos = []
        # iterate over the db re sults and create isntances of dojos with cls.
        for dojo in results: #dojo is a representation of each row coming back
            dojos.append(cls(dojo)) #dojo is a representation of data and its going to translate all that stuff in there.
        return dojos

    # Adding a dojo
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL(cls.schema_name).query_db(query, data)
        return results
        # Whenever we save, it will return that ID of that row. 

    # Grab one ninja
    @classmethod  #data will be the id
    def get_one_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.schema_name).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for table in results:
            d = {
                'id': table['ninjas.id'],
                'first_name': table['first_name'],
                'last_name': table['last_name'],
                'age': table['age'],
                'created_at': table['created_at'],
                'updated_at': table['updated_at'],
            }
            dojo.ninjas.append(Ninja(d)) 
        return dojo
        

