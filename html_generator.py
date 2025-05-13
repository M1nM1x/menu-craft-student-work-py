import json

# Путь к JSON-файлу
json_path = "raw_data.json"
# Путь к выходному HTML-файлу
output_path = "dishes_output.html"

# Загрузка данных из JSON
with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Начало HTML-документа
html_output = []


for dish in data['Dishes']:
    name = dish["dish_name"]
    description = dish["description"]
    recipe = dish["recipe"]
    calories = dish["calories"]
    cooking_time = dish["cooking_time"]
    difficulty = dish["difficulty"]
    ingredients = dish["ingredients"]

    # Создание HTML для ингредиентов
    ingredients_html = "\n".join([
        f'<li>{item["ingredient"]} {item["quantity"]} {item["unit"]}</li>'
        for item in ingredients
    ])

    # Структура карточки блюда
    card_html = f'''
<div class="dish_card">
    <div class="left_part">
        <img src="{{{{ url_for('static', filename='images/Блюда/{name}.jpg') }}}}" class="dish_img">
        <div class="characteristic">
            <div class="char_el">
                <p>Калории: {calories}</p>
            </div>
            <div class="char_el">
                <p>Время приготовления: {cooking_time}</p>
            </div>
            <div class="char_el">
                <p>Сложность: {difficulty}</p>
            </div>
        </div>
    </div>

    <div class="right_part">
        <div class="dish_info">
            <h1 class="dish_title">{name}</h1>
            <p class="description">{description}</p>
            <hr class="trait"/>
            <p class="info_title">Ингредиенты</p>
            <ul class="ingredients_list">
                {ingredients_html}
            </ul>
            <p class="info_title">Метод приготовления</p>
            <p class="cooking_method_text">{recipe}</p>
        </div>
    </div>  
</div>
    '''
    html_output.append(card_html.strip())

# Запись результата в файл
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(html_output))

print(f"✅ HTML сгенерирован и сохранён в {output_path}")
