from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.origin = data["origin"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    # create
    @classmethod
    def create(cls, data):
        pass

    # read many
    @classmethod
    def get_all(cls):
        pass
    
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
        pass
    
        
        