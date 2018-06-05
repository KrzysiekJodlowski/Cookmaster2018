import common
import time


def print_results(dishes):

    chosen_dishes = []
    print("Recipes I have found:")
    i = 1

    for dish in dishes.keys():
        print(i, dish)
        chosen_dishes.append(dish)
        i += 1

    return chosen_dishes


def display_graphics(graphic_file):

    with open(graphic_file, "r+") as file:
        lines = file.readlines()
        lines = [item.strip("\n") for item in lines]
    for line in lines:
        print(line)
        time.sleep(0.05)


def print_recipe(dish_name, directory):

    dish_name = directory + dish_name + ".txt"

    with open(dish_name, "r") as file:
        lines = file.readlines()
        list_recipe = [item.strip("\n") for item in lines]
        for line in list_recipe:
            print("   ", line)
    print()