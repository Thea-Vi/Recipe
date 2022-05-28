from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.user = user.User.get_by_id({"id": data["user_id"]})
        self.name = data["name"]
        self.origin = data["origin"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    # create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (user_id, name, origin, description, instruction, created_at, updated_at) VALUES (%(user_id)s, %(name)s, %(origin)s, %(description)s, %(instruction)s, NOW(), NOW());"

# returns the ID of the newly created recipe
        return connectToMySQL("recipe_schema").query_db(query, data)
    # read many
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipe_schema").query_db(query)
        
        recipes = []
        for row in results:
            recipes.append(cls(row))
            
        return recipes
    
    # read one
    @classmethod
    def get_one(cls):
        pass

    # update
    @classmethod
    def update(cls, data):
        pass
    
    #delete
    @classmethod
    def delete(cls, data):
        pass

        
    @staticmethod
    def validate(post_data):
        is_valid = True
        
        if len(post_data["name"]) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
            
        if len(post_data["origin"]) < 2:
            flash("Origin must be at least 2 characters.")
            is_valid = False
            
        if len(post_data["description"]) < 2:
            flash("Description must be at least 8 characters.")
            is_valid = False
            
        if len(post_data["instruction"]) < 2:
            flash("Instruction must be at least 8 characters.")
            is_valid = False
        
        return is_valid
    
        
        