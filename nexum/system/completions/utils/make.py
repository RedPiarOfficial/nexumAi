import requests
import json
import base64
import random
import string
import time
from datetime import datetime, timedelta
import html

# Константы
TOKEN_URL = "https://data.toolbaz.com/token.php"
WRITING_URL = "https://data.toolbaz.com/writing.php"
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
SESSION_ID = "ERfvMHDEY5Fo1TTJu1W7hIZSA9dHcVyJCb5m"
TDF = -7

# Функция генерации случайной строки
def generate_random_string(length):
    return ''.join(random.choice(CHARACTERS) for _ in range(length))

# Функция кодирования HTML-сущностей
def encode_html_entities(text):
    entity_map = {
        '"': "\"",
        "&": "&",
        "'": "'",
        "<": "<",
        ">": ">",
        "`": "`"
    }
    text = text + "ㅤ"
    return ''.join(entity_map.get(char, char) for char in text)

# Функция получения текущего времени
def get_current_time():
    return int(time.time())

# Функция генерации токена
def generate_xa1py_token():
    browser_data = {
        "nV5kP": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "lQ9jX": "ru-RU",
        "sD2zR": "1920x1080",
        "tY4hL": "Europe/Moscow",  # Предполагаем часовой пояс для ru-RU
        "pL8mC": "Win32",
        "cQ3vD": 24,
        "hK7jN": 8
    }
    user_tracking = {
        "mM9wZ": [{"x": random.randint(0, 1920), "y": random.randint(0, 1080)} for _ in range(20)],
        "kP8jY": [random.choice(string.ascii_letters) for _ in range(10)]
    }
    token_data = {
        "bR6wF": browser_data,
        "uT4bX": user_tracking,
        "tuTcS": get_current_time(),
        "tDfxy": TDF,
        "RtyJt": generate_random_string(36),
        "extra": {
            "random_str": generate_random_string(50),
            "timestamp": str(datetime.utcnow()),
            "version": "1.0.0"
        }
    }
    json_data = json.dumps(token_data)
    base64_data = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
    return generate_random_string(6) + base64_data

# Функция установки куки
def set_cookie(cookies, name, value, days=1):
    expires = datetime.utcnow() + timedelta(days=days)
    cookies[name] = {"value": value, "expires": expires.timestamp()}
    return cookies

# Функция получения куки
def get_cookie(cookies, name):
    return cookies.get(name, {}).get("value")