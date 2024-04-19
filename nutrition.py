fruit=input("Fruit? ")

#Dictionary for the 20 most common fruits
calories={
    "Apple":"130",
    "Avocado":"50",
    "Banana":"110",
    "Cantaloupe":"50",
    "Grapefruit": "60",
    "Grapes":"90",
    "Honeydew":"50",
    "Kiwifruit":"90",
    "Lemon":"15",
    "Lime":"20",
    "Nectarine":"60",
    "Orange":"80",
    "Peach":"60",
    "Pear":"100",
    "Pineaplle":"50",
    "Plums":"70",
    "Strawberries":"50",
    "Sweet cherries":"100",
    "Tangerine":"50",
    "Watermelon":"80"
}

if fruit in calories:
    for fruit_name, fruit_calories in calories.items(): 
        fruit=fruit.replace(fruit_name, fruit_calories)

    print(fruit)

else:
    print("Not found")