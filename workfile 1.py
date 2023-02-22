import os
def food_list():
    with open ('recipes.txt', 'r', encoding='utf8') as recipes:
        cook_book = {}
        for line in recipes:
            food_name = line.strip()
            cook_book [food_name] = []
            products_count = recipes.readline()
            for i in range(int(products_count)):
                prod = recipes.readline()
                ingredient_name, quantity, measure = prod.split('|')
                recipe = {'ingredient_name':ingredient_name, 'quantity':quantity, 'measure':measure.split()}
                cook_book[food_name].append(recipe)
            recipes.readline()
            print(cook_book)
    return
food_list()
                
            