# finds dishes that can be made from all your ingredients
def get_dishes_by_all_components(components, dishes):

    result = {}

    for dish in dishes.keys():

        add = True

        for component in dishes[dish].keys():
            if component not in components.keys():
                add = False
            else:
                if dishes[dish][component] > components[component]:
                    add = False

        if add:
            result[dish] = dishes[dish]

    return result


# finds dishes that contains any of your ingredients
def get_dishes_by_one_component(components, dishes):

    result = {}

    for dish in dishes.keys():

        dish_components = 0

        for component in dishes[dish].keys():
            if component in components:
                result[dish] = dishes[dish]

    return result
