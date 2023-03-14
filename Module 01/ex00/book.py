from datetime import datetime
from recipe import Recipe

class Book():
    name: str
    last_update: datetime
    creation_date: datetime
    recipes_list: dict
    
    def __init__(self, name: str, last_update: datetime, creation_date: datetime):
        self.name = name
        if not isinstance(last_update, datetime):
            print("ValueError: last_update is not a datetime instance.")
            return
        if not isinstance(creation_date, datetime):
            print("ValueError: creation_date is not a datetime instance.")
            return
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def __str__(self) -> str:
        return self.name
    
    def get_recipe_by_name(self, name):
        """Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type """
        return self.recipes_list.get(recipe_type)

    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        if isinstance(recipe, Recipe):
            #print("TR ", self.recipes_list[recipe.recipe_type])
            self.recipes_list[recipe.recipe_type].append(recipe)
        else:
            print("ValueError: recipe is not a Recipe type.")
            return