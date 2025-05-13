import random
import json
import os

MENU_FILE = 'data/daily_menu.json'

with open('data/data_2.0.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

breakfast = []
lunch = []
dinner = []

for dish in data['Dishes']:
    if 'завтрак' in dish['criteria']:
        breakfast.append(dish)

    if 'обед' in dish['criteria']:
        lunch.append(dish)
        
    if 'ужин' in dish['criteria']:
        dinner.append(dish)


def load_daily_menu():
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return None


def save_daily_menu(menu):
    with open(MENU_FILE, 'w', encoding='utf-8') as file:
        json.dump(menu, file, indent=4, ensure_ascii=False)


from datetime import date

PAST_MENUS_FILE = 'data/past_menus.json'

def save_past_menu(menu):
    today = str(date.today())
    if os.path.exists(PAST_MENUS_FILE):
        with open(PAST_MENUS_FILE, 'r', encoding='utf-8') as file:
            past_menus = json.load(file)
    else:
        past_menus = {}

    past_menus[today] = menu
    with open(PAST_MENUS_FILE, 'w', encoding='utf-8') as file:
        json.dump(past_menus, file, indent=4, ensure_ascii=False)

def generate_menu(preferences=None):
    filtered_breakfast = [dish for dish in breakfast if not preferences or (
        (preferences.get('cuisine') in dish['criteria']) and
        (preferences.get('difficulty') == dish['difficulty']) and
        (int(preferences.get('calories', 1000)) >= dish['calories'])
    )]
    filtered_lunch = [dish for dish in lunch if not preferences or (
        (preferences.get('cuisine') in dish['criteria']) and
        (preferences.get('difficulty') == dish['difficulty']) and
        (int(preferences.get('calories', 1000)) >= dish['calories'])
    )]
    filtered_dinner = [dish for dish in dinner if not preferences or (
        (preferences.get('cuisine') in dish['criteria']) and
        (preferences.get('difficulty') == dish['difficulty']) and
        (int(preferences.get('calories', 1000)) >= dish['calories'])
    )]

    menu = {
        "breakfast": random.choice(filtered_breakfast) if filtered_breakfast else random.choice(breakfast),
        "lunch": random.choice(filtered_lunch) if filtered_lunch else random.choice(lunch),
        "dinner": random.choice(filtered_dinner) if filtered_dinner else random.choice(dinner)
    }
    save_daily_menu(menu)
    save_past_menu(menu)  # Сохраняем меню в историю
    return menu