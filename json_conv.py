import json


# Путь к JSON-файлу
json_path = "data/data_2.0.json"
# Путь к выходному HTML-файлу
output_path = "dishes_output.html"

# Загрузка данных из JSON
with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    

bakery = []
breakfast = []
desserts = []
drinks = []
main_courses = []
salads = []
sauces = []
side_dishes = []
snacks = []
soups = []

for dish in data['Dishes']:
    if dish['category_id'] == 1:
        soups.append(dish)
    elif dish['category_id'] == 2:
        salads.append(dish)
    elif dish['category_id'] == 3:
        main_courses.append(dish)
    elif dish['category_id'] == 4:
        desserts.append(dish)
    elif dish['category_id'] == 5:
        snacks.append(dish)
    elif dish['category_id'] == 6:
        bakery.append(dish)
    elif dish['category_id'] == 7:
        drinks.append(dish)
    elif dish['category_id'] == 8:
        side_dishes.append(dish)
    elif dish['category_id'] == 9:
        sauces.append(dish)
    elif dish['category_id'] == 10:
        breakfast.append(dish)

with open('data/soups.json', 'w', encoding='utf-8') as file:
    json.dump(soups, file, indent=4, ensure_ascii=False)

with open('data/salads.json', 'w', encoding='utf-8') as file:
    json.dump(salads, file, indent=4, ensure_ascii=False)
    
with open('data/main_courses.json', 'w', encoding='utf-8') as file:
    json.dump(main_courses, file, indent=4, ensure_ascii=False) 
    
with open('data/desserts.json', 'w', encoding='utf-8') as file:
    json.dump(desserts, file, indent=4, ensure_ascii=False)

with open('data/snacks.json', 'w', encoding='utf-8') as file:
    json.dump(snacks, file, indent=4, ensure_ascii=False)

with open('data/bakery.json', 'w', encoding='utf-8') as file:
    json.dump(bakery, file, indent=4, ensure_ascii=False)
    
with open('data/drinks.json', 'w', encoding='utf-8') as file:
    json.dump(drinks, file, indent=4, ensure_ascii=False) 
    
with open('data/side_dishes.json', 'w', encoding='utf-8') as file:
    json.dump(side_dishes, file, indent=4, ensure_ascii=False)

with open('data/sauces.json', 'w', encoding='utf-8') as file:
    json.dump(sauces, file, indent=4, ensure_ascii=False)

with open('data/breakfast.json', 'w', encoding='utf-8') as file:
    json.dump(breakfast, file, indent=4, ensure_ascii=False)
    

print("✅")