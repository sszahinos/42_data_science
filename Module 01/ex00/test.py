from book import Book
from recipe import Recipe
from datetime import datetime

recipe1 = Recipe("test1", 1, "test_list1", "starter")
recipe2 = Recipe("test2", 2, "test_list2", "lunch")
recipe3 = Recipe("test3", 3, "test_list3", "starter")
#print(recipe1)
book1 = Book("b_test1", datetime.now(), datetime.now())
#print(book1)
book1.add_recipe(recipe1)
book1.add_recipe(recipe2)
print("result: ", book1.get_recipe_by_name("test2"))
#print(book1.get_recipes_by_types("starter"))
book1.add_recipe("asdf")