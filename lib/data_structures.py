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
    array = []
    for food in spicy_foods:
        foodName = food["name"]
        array.append(foodName)
    return array

def get_spiciest_foods(spicy_foods):
    array = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            array.append(food)
    return array        
    
def print_spicy_foods(spicy_foods):
    array = []
    for food in spicy_foods:
        hit_level = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {hit_level}')
    return array

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food

def print_spiciest_foods(spicy_foods):
    array = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            hit_level = "🌶" * food["heat_level"]
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {hit_level}')
    return array

def get_average_heat_level(spicy_foods):
      return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)
    # num = 0;
    # for food in spicy_foods:
    #     sumOfAverage = sum(food["heat_level"])
    #     length = len(food)
    #     average = sumOfAverage/length
    # return average

def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods.append(spicy_food)
     return spicy_foods
