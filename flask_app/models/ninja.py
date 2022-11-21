#here we use oop
from flask_app.config.mysqlconnection import connectToMySQL 

class Ninja:
    db_name = 'dojos_ninjas'
    def __init__(self, data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.age = data['age'],
        self.dojo_id = data['dojo_id'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
    
    @classmethod
    def getAllNinjas(cls):
        query = 'SELECT * FROM ninjas;'
        result = connectToMySQL(cls.db_name).query_db(query)
        return result
    
    @classmethod
    def createNinja(cls,data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );'
        return connectToMySQL('dojos_ninjas').query_db(query,data)

    @classmethod
    def getDojosNinjas(cls,data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id  WHERE ninjas.dojo_id = %(id)s;'
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return results