from os import system
import os.path
import printing
import common


# choosing what to show on main menu
def show_main_menu(authors):

    main_menu = "graphics/menu.txt"
    dishes_details_directory = "dishes_details/"
    decision = "0"

    while decision != "4":

        printing.display_graphics(main_menu)
        decision = input("\nWhat you want to do?\n")

        if decision == "1":

            final_dishes = common.meal_type_decision("find")

            if len(final_dishes) < 1:
                print("\nA t t e n t i o n  ! ! !\nThere is no such product !!!\n")
            else:
                printing.print_results(final_dishes)
                all_dishes = list(final_dishes.keys())  # common.get_list_of_ordered_dishes(final_dishes)
                choosen_dish = common.choose_dish(final_dishes, all_dishes)
                print("\n***", choosen_dish.upper(), "***\n")
                printing.print_recipe(choosen_dish, dishes_details_directory)
                common.deciding_to_add_note(choosen_dish)
                return

        elif decision == "2":

            food_recipes = common.meal_type_decision("show")
            printing.print_results(food_recipes)
            all_dishes = common.get_list_of_ordered_dishes(food_recipes)
            dish_name = common.choose_dish(all_dishes, all_dishes)
            print("\n***", dish_name.upper(), "***\n")
            printing.print_recipe(dish_name, "dishes_details/")

            if os.path.isfile("dishes_notes/" + dish_name + ".txt") is True:
                print("    N O T E S \n")
                printing.print_recipe(dish_name, "dishes_notes/")

        elif decision == "3":
            printing.display_graphics(authors)
            input("Hit any key to exit")


# main function
def main():

    welcome_screen = "graphics/welcome.txt"
    end_screen = "graphics/end.txt"
    authors = "graphics/authors.txt"

    system("clear")
    printing.display_graphics(welcome_screen)
    input("\nClick anything to start")
    system("clear")

    show_main_menu(authors)
    system("clear")
    printing.display_graphics(end_screen)


if __name__ == "__main__":
    main()
