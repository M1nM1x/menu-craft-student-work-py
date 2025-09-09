from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

from gen_menu import generate_menu, load_daily_menu, save_daily_menu

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Нужен для сессий

# Путь к файлу с пользователями
USERS_FILE = 'data/users.json'

# Функция для загрузки пользователей из JSON
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return []

# Функция для сохранения пользователей в JSON
def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# Главная страница
@app.route('/')
def main_page():
    if 'username' in session:
        return render_template('main_page.html', username=session['username'])
    return redirect(url_for('login'))

# Страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        # Проверяем, существует ли пользователь
        if any(user['username'] == username for user in users):
            return 'Пользователь уже существует!'
        # Находим максимальный id и добавляем нового пользователя
        new_id = max([user['id'] for user in users], default=0) + 1
        users.append({'id': new_id, 'username': username, 'password': password})
        save_users(users)
        return redirect(url_for('login'))
    return render_template('register.html')

# Страница авторизации
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                return redirect(url_for('main_page'))
        return 'Неверный логин или пароль!'
    return render_template('login.html')

# Выход из аккаунта
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Другие маршруты
@app.route('/statistics')
def statistics():
    past_menus_file = 'data/past_menus.json'
    daily_menu = load_daily_menu()  # Загружаем текущее меню

    if not os.path.exists(past_menus_file):
        with open(past_menus_file, 'w', encoding='utf-8') as file:
            json.dump({}, file)  # Инициализируем пустой объект

    with open(past_menus_file, 'r', encoding='utf-8') as file:
        try:
            past_menus = json.load(file)
        except json.JSONDecodeError:
            past_menus = {}  # Если файл пуст или поврежден, используем пустой объект

    return render_template('statistics.html', daily_menu=daily_menu, past_menus=past_menus)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    users = load_users()
    current_user = next((user for user in users if user['username'] == session['username']), None)

    if not current_user:
        return 'Пользователь не найден!', 404

    if request.method == 'POST':
        if 'regenerate_menu' in request.form:  # Если нажата кнопка пересоздания меню
            generate_menu()
            return redirect(url_for('profile'))  # Редирект после пересоздания меню
        else:
            # Обновление данных профиля
            new_username = request.form['username']

            # Проверяем, что новое имя пользователя не занято
            if new_username != current_user['username'] and any(user['username'] == new_username for user in users):
                return 'Имя пользователя уже занято!'

            # Обновляем данные пользователя
            current_user['username'] = new_username
            session['username'] = new_username  # Обновляем сессию
            save_users(users)
            return redirect(url_for('profile'))  # Редирект после обновления профиля

    daily_menu = load_daily_menu() or generate_menu()
    return render_template('profile.html', user=current_user, daily_menu=daily_menu)



@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        # Сохраняем предпочтения в сессии
        session['preferences'] = {
            'cuisine': request.form['cuisine'],
            'difficulty': request.form['difficulty'],
            'calories': request.form['calories']
        }
        return redirect(url_for('settings'))
    preferences = session.get('preferences', {})
    return render_template('settings.html', preferences=preferences)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    if not query:
        return redirect(url_for('main_page'))

    with open('data/data_2.0.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    results = []
    for dish in data['Dishes']:
        if query in dish['dish_name'].lower() or query in dish['description'].lower():
            results.append(dish)

    return render_template('search_results.html', query=query, results=results)

@app.route('/add_to_menu/<int:dish_id>', methods=['POST'])
def add_to_menu(dish_id):
    meal = request.form['meal']
    with open('data/data_2.0.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    dish = next(d for d in data['Dishes'] if d['dish_id'] == dish_id)
    daily_menu = load_daily_menu() or {"breakfast": {}, "lunch": {}, "dinner": {}}
    daily_menu[meal] = dish
    save_daily_menu(daily_menu)
    return redirect(url_for('profile'))

# catalog routes
@app.route('/soups')
def soups():
    return render_template('soups.html')

@app.route('/bakery')
def bakery():
    return render_template('bakery.html')

@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html')

@app.route('/desserts')
def desserts():
    return render_template('desserts.html')

@app.route('/drinks')
def drinks():
    return render_template('drinks.html')

@app.route('/main_courses')
def main_courses():
    return render_template('main_courses.html')

@app.route('/salads')
def salads():
    return render_template('salads.html')

@app.route('/sauces')
def sauces():
    return render_template('sauces.html')

@app.route('/side_dishes')
def side_dishes():
    return render_template('side_dishes.html')

@app.route('/snacks')
def snacks():
    return render_template('snacks.html')

@app.route('/all')
def all():
    return render_template('all.html')

if __name__ == '__main__':
    app.run(debug=True)