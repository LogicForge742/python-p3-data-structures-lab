spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [x["name"] for x in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food["heat_level"] >5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
     name = food["name"]
     cuisine = food["cuisine"]
     heat_level = food["heat_level"]
     #chilli emoji
     heat_visual = "🌶" * heat_level

     print(f"{name} ({cuisine}) | Heat Level: {heat_visual}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
        

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:   # filter only spiciest foods
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            heat_visual = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_visual}")



def get_average_heat_level(spicy_foods):
    heat_total = 0
    for food in spicy_foods:
        heat_total += food["heat_level"]
    average = heat_total / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    print(spicy_foods)
    return spicy_foods
