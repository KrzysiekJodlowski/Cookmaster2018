# adding notes
def add_note(dish_name, text):

    dish_name = "dishes_notes/" + dish_name + ".txt"

    with open(dish_name, "a+") as file:
        file.write(text + "\n")

    return dish_name
