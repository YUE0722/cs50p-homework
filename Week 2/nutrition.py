calories = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe":"50",
    "grapefruite": "60",
    "grapes": "90",
    "honeydew Melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet Cherries": "100",
    "tangerine": "50",
    "watermelon": "80",
}

i = input("Item: ").lower()
if i in calories:
    print(f"Calories: {calories[i]}")
else:
    print("", end = "")
