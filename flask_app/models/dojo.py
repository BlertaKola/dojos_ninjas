#here we use oop
from flask_app.config.mysqlconnection import connectToMySQL 

class Dojo:
    db_name = 'dojos_ninjas'
    def __init__(self, data):
        self.id = data['id'],
        self.name = data['name'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
    
    @classmethod
    def getAllDojos(cls):
        query = 'SELECT * FROM dojos;'
        result = connectToMySQL(cls.db_name).query_db(query)
        return result

    @classmethod
    def createDojo(cls,data):
        query = 'INSERT INTO dojos (name) VALUES ( %(name)s);'
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def getDojosInfoById(cls,data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result

    

