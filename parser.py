import json

with open('convert.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# print(data['Units'])

categories = []
units = []
ingredients = []
dishes = []

dish_categories = [
    (1, 1), (6, 1), (11, 1), (17, 1), (26, 1), (30, 1), (35, 1), (42, 1), (57, 1), (64, 1), (70, 1), (74, 1), (79, 1), (85, 1), (92, 1), (2, 2), (5, 2), (9, 2), (23, 2), (32, 2), (40, 2), (48, 2), (55, 2), (63, 2), (69, 2), (76, 2), (83, 2), (89, 2), (94, 2), (98, 2), (3, 3), (7, 3), (10, 3), (12, 3), (15, 3), (16, 3), (21, 3), (24, 3), (27, 3), (33, 3), (43, 3), (46, 3), (53, 3), (61, 3), (75, 3), (4, 4), (8, 4), (22, 4), (25, 4), (29, 4), (31, 4), (38, 4), (47, 4), (56, 4), (59, 4), (71, 4), (78, 4), (86, 4), (91, 4), (99, 4), (39, 5), (40, 5), (41, 5), (60, 5), (63, 5), (73, 5), (82, 5), (90, 5), (96, 5), (100, 5), (13, 6), (14, 6), (18, 6), (36, 6), (44, 6), (50, 6), (58, 6), (77, 6), (87, 6), (95, 6), (51, 7), (52, 7), (84, 7), (88, 7), (19, 8), (20, 8), (28, 8), (34, 8), (62, 8), (37, 9), (45, 9), (54, 9), (42, 10), (49, 10), (65, 10), (67, 10), (93, 10), (97, 10)
]

dish_ingredients = [
    (1, 8, 300, 1), (1, 9, 200, 1), (1, 10, 400, 1), (1, 15, 200, 1), (2, 30, 100, 1), (2, 16, 200, 1), (2, 35, 50, 1), (2, 34, 30, 1), (3, 20, 200, 1), (3, 33, 100, 1), (3, 34, 50, 1), (3, 6, 2, 1), (4, 36, 250, 1), (4, 37, 100, 1), (4, 38, 200, 1), (4, 39, 20, 1), (5, 10, 300, 1), (5, 23, 100, 1), (5, 28, 150, 1), (5, 29, 150, 1), (6, 41, 200, 1), (6, 40, 100, 1), (6, 12, 50, 1), (6, 3, 5, 1), (7, 45, 300, 1), (7, 15, 200, 1), (7, 3, 5, 1), (7, 12, 50, 1), (8, 36, 200, 1), (8, 4, 100, 1), (8, 2, 100, 1), (8, 6, 2, 1), (9, 28, 150, 1), (9, 29, 150, 1), (9, 21, 100, 1), (9, 27, 50, 1), (10, 45, 200, 1), (10, 15, 200, 1), (10, 21, 100, 1), (10, 14, 100, 1)
]

for i in range(len(data['Categories'])):
    categories.append(
        {
            "category_id": i + 1,
            "category_name": data['Categories'][i]['category_name']
        }
    )

for i in range(len(data['Units'])):
    units.append(
        {
            "unit_id": i + 1,
            "unit_name": data['Categories'][i]['category_name']
        }
    )

for i in range(len(data['Ingredients'])):
    ingredients.append(
        {
            "ingredient_id": i + 1,
            "ingredient_name": data['Ingredients'][i]['ingredient_name']
        }
    )

ingredients_raw = []

for i in range(len(dish_ingredients)):
    ingredients_raw.append(
        {
            "ingredient": 
        }
    )

for i in range(len(data['Dishes'])):
    for j in range(len(dish_categories)):
        for z in range(len(dish_ingredients)):
            if dish_categories[j][0] == i + 1:
                dishes.append(
                    {
                        "dish_id": i + 1,
                        "dish_name": data['Dishes'][i]['dish_name'],
                        "description": data['Dishes'][i]['description'],
                        "recipe": data['Dishes'][i]['recipe'],
                        "calories": data['Dishes'][i]['calories'],
                        "cooking_time": data['Dishes'][i]['cooking_time'],
                        "difficulty": data['Dishes'][i]['difficulty'],
                        "category_id": dish_categories[j][1],
                        "ingredients": ingredients_raw[i]
                    }
                )
            



# print(ingredients)

result = {
    "Categories": categories,
    "Units": units,
    "Ingredients": ingredients,
    "Dishes": dishes
}

with open('data/data.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False)

# print(len(dishes))
