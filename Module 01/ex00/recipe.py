from typing import List

class Recipe():
    name: str
    cooking_lvl: int
    ingredients: List[str]
    description: str
    recipe_type: str
    
    def __init__(self, name: str, cooking_lvl: int,
                ingredients: List[str], recipe_type: str, description=''):
        self.name = name
        try:
            int(cooking_lvl)
        except ValueError:
            print("ValueError: Cooking level is not an int.")
            return None
        self.cooking_lvl = cooking_lvl
        self.ingredients = ingredients
        self.description = description
        if recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert":
            self.recipe_type = recipe_type
        else:
            print("ValueError: recipe_type is not a valid option.")
            return None

    def __str__(self) -> str:
        return "Name: {} / Lvl: {} / Ingredients: {} / Desc: {} / Type: {}".format(self.name, self.cooking_lvl, self.ingredients, self.description, self.recipe_type)
