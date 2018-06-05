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


def get_length_of_the_list(imported_list):

    return len(imported_list)


def print_list_of_options_to_choose(list_of_options):

    for number, option in enumerate(list_of_options):
        print((number + 1), option)


def get_input_from_user(length_of_list):

    valid_input = False

    while valid_input is False:
        get_option_choosed_by_user = int(input("\nChoose option from list above: "))
        if get_option_choosed_by_user > length_of_list:
            print_warning("You have entered invalid number")
        else:
            valid_input = True

    return str(get_option_choosed_by_user)


def print_header(header):
    print("\n***", header.upper(), "***\n")


def print_warning(warning):
    print("\nA t t e n t i o n  ! ! !\n", warning, "!!!\n")