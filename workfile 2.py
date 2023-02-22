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
            #print(cook_book)

        person_count = 3
        shop_list = {}
        for i in cook_book:
            ii = i.split()
            #print (ii)
            tittle = cook_book[food_name]
            for j in tittle:
                #print (j)
                new_ingredient_shop_list = j
                product = new_ingredient_shop_list['ingredient_name']
                weight = new_ingredient_shop_list['measure']
                amount = int (new_ingredient_shop_list['quantity']) * person_count
                weight_amount = {'measure' : weight, 'quantity' : amount}
                if product not in shop_list:
                    shop_list[product] = weight_amount
                else:
                    shop_list[product]['quantity'] = shop_list[product]['quantity'] + amount
        print (shop_list)
    return
food_list()
                
            