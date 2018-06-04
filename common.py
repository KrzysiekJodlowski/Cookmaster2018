import algorithms
import note


# importing recipes as dictionary from file
def import_recipes(recipes_txt):

    with open(recipes_txt, "r+") as file:
        lines = file.readlines()
        recipies = [item.strip("\n").split(",") for item in lines]

    dishes = {}

    for i in range(0, len(recipies)-1, 2):
        dict_temp = {}
        for j in range(len(recipies[i+1])):
            temp = recipies[i+1][j]
            temp = temp.split(":")
            dict_temp[temp[0]] = temp[1]
        dishes[recipies[i][0]] = dict_temp
        i = i+1

    return dishes


# choosing number of dish
def choose_dish(final_dishes, all_dishes):

    dish_name = "nothing"

    while dish_name not in final_dishes:
        dish_number = input("Choose number of dish recipe You want to see!\n")
        dish_name = all_dishes[int(dish_number)-1]

    return dish_name


# creating list with established order of dishes
def get_list_of_ordered_dishes(dishes):

    all_dishes = []

    for dish in dishes.keys():
        all_dishes.append(dish)

    return all_dishes


# choosing note adding
def deciding_to_add_note(choosen_dish):

    decision = "0"

    while decision != "y" or decision != "n":
        decision = input("Do you want to add a note to your dish?(y/n)\n")
        if decision == "y":
            note_text = input("What you want to write in Your note?\n")
            note.add_note(choosen_dish, note_text)
        elif decision == "n":
            return
        else:
            print("\nYou can type only 'y' or 'n'\n")


def find_meals():

    meal_type = meal_type_decision()
    final_dishes = search_type(meal_type)
    return final_dishes


def show_meals():

    meal_type = meal_type_decision()
    print("\n*{0}*\n".format((meal_type.strip(".txt")).upper()))
    food_recipes = import_recipes(meal_type)
    return food_recipes


# choosing meal type
def meal_type_decision():

    choose = "0"
    breakfast, supper, dinner = "breakfast.txt", "supper.txt", "dinner.txt"
    # while choose not in ('b','s','d'):
    while choose != "b" or choose != "s" or choose != "d":
        choose = input("You want receipts for: breakfast, supper or dinner? (b,s,d)\n")
        if choose == "b":
            return breakfast
        elif choose == "s":
            return supper
        elif choose == "d":
            return dinner
        else:
            print("\nsomething went wrong, be sure you typed 'b', 's' or 'd'\n")


# getting dishes by choosen algorithm
def search_type(file_type):

    choose = "0"

    dishes = import_recipes(file_type)
    while choose != "1" or choose != "2":
        choose = input("Do You want to search for: \n 1.Receipts you can make with your ingredients \n 2.Receipts containing ingredient?(1 or 2)\n")
        if choose == "1":
            components = pick_components(choose)
            final_dishes = algorithms.get_dishes_by_all_components(components, dishes)
            break
        elif choose == "2":
            components = pick_components(choose)
            final_dishes = algorithms.get_dishes_by_one_component(components, dishes)
            break
        else:
            print("\nare you sure you picked 1 or 2? Try again!\n")

    return final_dishes


# picking data for right algorithm
def pick_components(type):

    ingredients_integer = True

    while ingredients_integer:
        try:
            number_of_ingredients = int(input("How many ingredients you want to use?\n"))
            ingredients_integer = False
        except ValueError:
            print("\nYou need to write a number!\n")

    if type == "1":
        components = {}
        for ingredients in range(int(number_of_ingredients)):
            ingredient = input("Pick ingredient\n")
            quantity = input("Pick quantity\n")
            components[ingredient] = quantity

    elif type == "2":
        components = []
        for ingredients in range(int(number_of_ingredients)):
            ingredient = input("Pick ingredient\n")
            components.append(ingredient)

    return components
