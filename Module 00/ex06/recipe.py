from typing import Dict

Recipe = Dict[str, {str, str, int}]
Cookbook = Dict[str, Recipe]

def print_recipes():
    for key in cookbook:
        print(key)

def print_details(recipe: str):
    print("Ingredients list: {}".format(cookbook[recipe]["ingredients"]))
    print("To be eaten for {}".format(cookbook[recipe]["meal"]))
    print("Takes {} minutes of cooking.".format(cookbook[recipe]["prep_time"]))

def delete_recipe(recipe: str):
    cookbook.pop(recipe, None)

def add_recipe():
    name = input("Enter the recipe's name: ")
    ingredients_quant = int(input("How many ingredients has the recipe?"))
    ingredients = []
    for x in range(ingredients_quant):
        ingredients.append(input("Ingredient nº{}: ".format(x)))
    meal_type = input("Type of meal: ")
    time_prep = input("Time to prepare: ")
    new_recipe: Recipe = {
        'ingredients': ingredients,
        'meal': meal_type,
        'prep_time': time_prep
    }
    cookbook[name] = new_recipe

def print_main_menu():
    print("""Welcome to the Python Cookbook !
List of available option:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit""")

def print_cookbook():
    for recipe in cookbook:
        print_details(recipe)
        print("--------")


bocadillo: Recipe = {
    "ingredients": ["jamón", "pan", "queso", "tomate"],
    "meal": "almuerzo",
    "prep_time": 10
}
tarta: Recipe = {
    "ingredients": ["harina", "azúcar", "huevos"],
    "meal": "postre",
    "prep_time": 60
}

ensalada: Recipe = {
    "ingredients": ["aguacate", "rúcula", "tomates", "espinacas"],
    "meal": "almuerzo",
    "prep_time": 15
}

cookbook: Cookbook = {}
cookbook["bocadillo"] = bocadillo
cookbook["tarta"] = tarta
cookbook["ensalada"] = ensalada

if __name__ == "__main__":
    while(True):
        print_main_menu()
        selection = input("Please, select an option: ")
        if selection == "1":
            add_recipe()
        elif selection == "2":
            delete_recipe(input("Recipe's name: "))
        elif selection == "3":
            print_details(input("Recipe's name: "))
        elif selection == "4":
            print_cookbook()
        elif selection == "5":
            print("Cookbook closed. Goodbye !")
            break
        else:
            print("Sorry, this option does not exist.")