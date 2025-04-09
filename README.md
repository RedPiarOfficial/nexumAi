# Документация фреймворка Nexum

## Содержание

1. [Введение](#введение)
2. [Установка](#установка)
3. [Начало работы](#начало-работы)
4. [Клиент](#клиент)
5. [API для генерации текста](#api-для-генерации-текста)
   - [Доступные модели](#доступные-модели-текста)
   - [Примеры использования](#примеры-использования-текста)
6. [API для генерации изображений](#api-для-генерации-изображений)
   - [Доступные модели](#доступные-модели-изображений)
   - [Настройки генерации изображений](#настройки-генерации-изображений)
   - [Примеры использования](#примеры-использования-изображений)
7. [Интеграция с Tor](#интеграция-с-tor)
8. [Расширенное использование](#расширенное-использование)
9. [Устранение неполадок](#устранение-неполадок)
10. [Справочник API](#справочник-api)

## Введение

Nexum — это Python-фреймворк, предоставляющий доступ к множеству AI-сервисов через унифицированный API. Он включает:

- **API для генерации текста**: Создание текста с использованием различных AI-моделей, включая Gemini, GPT-4, Llama и другие
- **API для генерации изображений**: Создание изображений из текстовых промптов с использованием различных моделей диффузии
- **Интеграция с Tor**: Опциональная поддержка прокси для повышенной приватности

Nexum разработан для простоты использования при обеспечении доступа к мощным возможностям искусственного интеллекта.

## Установка

```python
# Информация об установке будет добавлена после публикации пакета
# Вероятно, через pip:
# pip install nexum
```

### Требования

- Python 3.9 или выше
- Для интеграции с Tor: запущенный сервис Tor на вашей машине

## Начало работы

Начните с импорта класса Client и создания экземпляра клиента:

```python
from nexum import Client

# Инициализация клиента
client = Client()
```

## Клиент

Класс `Client` является основной точкой входа для взаимодействия с API Nexum. Он предоставляет доступ к двум основным сервисам:

- `completion`: Для генерации текста
- `diffusion`: Для генерации изображений

### Базовое использование

```python
from nexum import Client

client = Client()

# Доступ к генерации текста
completion = client.completion

# Доступ к генерации изображений
diffusion = client.diffusion
```

## API для генерации текста

API для генерации текста позволяет создавать текстовые ответы с использованием различных AI-моделей.

### Создание текстовых ответов

```python
from nexum import Client

client = Client()

# Создание простого ответа
messages = [
    {"role": "user", "content": "Привет!"}
]

# Использование модели по умолчанию (Gemini-2.0-F-Thinking)
response = client.completion.create(messages)
print(response)

# Использование конкретной модели по ID
response = client.completion.create(messages, model=4)  # Использует GPT-4o
print(response)

# Использование конкретной модели по имени
response = client.completion.create(messages, model="Llama-3.3")
print(response)

# Проверка используемой модели
response = client.completion.create(messages, model_check=True)
print(response)

# Использование Tor-прокси для повышенной приватности
response = client.completion.create(messages, proxy=True)
print(response)
```

### Доступные модели текста

Nexum предоставляет доступ к множеству моделей генерации текста от разных провайдеров:

#### Модели Google
- **Gemini-2.0-F-Thinking** (ID: 1): Глубокое понимание контекста, генерация осмысленных ответов
- **Gemini-2.0-Flash** (ID: 2): Высокоскоростная генерация текста с отличным пониманием контекста
- **Gemini-1.5-Flash** (ID: 3): Быстрая и эффективная генерация текста с хорошим пониманием запросов пользователя

#### Модели OpenAI
- **GPT-4o** (ID: 4): Мультимодальная модель, поддерживающая более 50 языков с улучшенным пониманием контекста
- **O1-Mini** (ID: 5): Оптимизирована для задач STEM, особенно математики и программирования

#### Модели DeepSeek
- **Deepseek-R1-Distill** (ID: 6): Компактные модели для задач рассуждения и программирования

#### Модели Meta
- **Llama-3.3** (ID: 7): Продвинутая языковая модель с 70 миллиардами параметров
- **Llama-3.1** (ID: 8): Крупная языковая модель с 405 миллиардами параметров и контекстом до 128k токенов

#### Модели Alibaba
- **Qwen2.5** (ID: 9): Модель с 72,7 миллиардами параметров и контекстом до 128k токенов, улучшенная для кодирования и математики

#### Модели xAI
- **Grok-2** (ID: 11): Продвинутая языковая модель с возможностями генерации изображений
- **Grok-Beta** (ID: 12): Экспериментальная модель с улучшенным рассуждением

#### Модели ToolBaz
- **ToolBaz-v3.5-Pro** (ID: 13): Продвинутая модель генерации текста
- **ToolBaz-v3** (ID: 14): Базовая модель генерации текста

#### Модели Mixtral
- **Mixtral** (ID: 15): Мощная модель с 141 миллиардом параметров, использующая архитектуру Mixture-of-Experts

#### Нефильтрованные модели
- **L3-Euryale-v2.1** (ID: 16): Модель с 70 миллиардами параметров на основе архитектуры LLaMA-3
- **Midnight-Rose** (ID: 17): Нефильтрованная языковая модель
- **Unity** (ID: 18): Нефильтрованная языковая модель
- **Unfiltered_X** (ID: 19): Нефильтрованная модель с 141 миллиардом параметров

### Примеры использования текста

```python
from nexum import Client
from nexum.system.completions.utils.models import Models

# Инициализация клиента
client = Client()

# Создание запроса с отображением используемой модели
messages = [{'role': 'user', 'content': 'Привет!'}]
response = client.completion.create(messages, model_check=True, model=2)
print(response)

# Просмотр всех доступных моделей
all_models = Models().get_models()
print(all_models)

# Поиск модели по ID
model = Models().get_model_by_id(1)
print(model)

# Поиск модели по названию
model = Models().get_model_by_name('Gemini-2.0-F-Thinking')
print(model)

# Универсальный поиск модели (по ID или названию)
model = Models().get_model(1)  # По ID
print(model)
model = Models().get_model('Gemini-2.0-F-Thinking')  # По названию
print(model)
```

## API для генерации изображений

API для генерации изображений позволяет создавать изображения из текстовых промптов с использованием различных моделей диффузии.

### Создание изображений

```python
from nexum import Client
from nexum.system.diffusion.utils.settings import Settings

client = Client()

# Генерация изображения с настройками по умолчанию
prompt = "cute anime cat"
client.diffusion.create(prompt)  # Сохраняет в ./media/image.jpg

# Использование конкретной модели и путь сохранения
client.diffusion.create("beautiful mountain landscape", path="./output/landscape.jpg", model="flux-2")

# Пользовательские настройки (только для модели sdxl-flash)
settings = Settings(model=2)  # Инициализация настроек для sdxl-flash
settings.set_resolution((768, 512))  # Установка пользовательского разрешения
settings.set_steps(20)  # Установка количества шагов вывода
settings.negative_prompt("blurry, low quality")  # Установка пользовательского негативного промпта

client.diffusion.create(
    "cute anime girl", 
    path="./output/custom_anime.jpg", 
    settings=settings,
    model=2
)

# Использование Tor-прокси
client.diffusion.create("cute anime cat", path="./output/proxy_cat.jpg", proxy=True)
```

### Доступные модели изображений

Nexum в настоящее время поддерживает следующие модели генерации изображений:

1. **flux-2** (ID: 1)
   - Стили: Реалистичный и Аниме
   - NSFW-контент: Не поддерживается
   - Настройки: Не настраиваемые

2. **sdxl-flash** (ID: 2)
   - Стили: Реалистичный и Аниме
   - NSFW-контент: Поддерживается
   - Настройки: Полностью настраиваемые

### Настройки генерации изображений

Для моделей, поддерживающих пользовательские настройки (в настоящее время только sdxl-flash), вы можете настроить следующие параметры:

```python
from nexum.system.diffusion.utils.settings import Settings

settings = Settings(model=2)  # Инициализация настроек для sdxl-flash

# Установка пользовательского негативного промпта
settings.negative_prompt("low quality, blurry, distorted")

# Установка определенного сида для воспроизводимых результатов (или 'random' для случайного сида)
settings.set_seed(42)  # Или settings.set_seed('random')

# Установка пользовательского разрешения (высота, ширина)
settings.set_resolution((768, 512))  

# Установка количества шагов вывода (больше = больше деталей, но медленнее)
settings.set_steps(20)
```

Настройки по умолчанию для sdxl-flash:
- Негативный промпт: `(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation`
- Сид: случайный
- Разрешение: 1024x1024
- Шаги: 15

### Примеры использования изображений

```python
from nexum import Client
from nexum.system.diffusion.utils.models import Models
from nexum.system.diffusion.utils.settings import Settings

# Инициализация клиента
client = Client()

# Базовая генерация изображения
client.diffusion.create('cute anime cat')  # Сохраняет в ./media/image.jpg

# Генерация с использованием конкретной модели и путем сохранения
client.diffusion.create('cute anime girl', path='./media/girl.png', model=2)

# Генерация с пользовательскими настройками
settings = Settings(model=2)
settings.negative_prompt('(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy...')
settings.set_seed('random')
settings.set_resolution((1024, 1024))
settings.set_steps(15)
client.diffusion.create(
    'cute anime girl', 
    path='./media/girl_steps_15.png', 
    model=2, 
    settings=settings
)

# Просмотр всех доступных моделей для генерации изображений
diffusion_models = Models().get_models()
print(diffusion_models)

# Поиск модели по ID или названию
model = Models().get_model(1)  # По ID
print(model)
model = Models().get_model('flux-2')  # По названию
print(model)
```

## Интеграция с Tor

Nexum предоставляет опциональную интеграцию с Tor-прокси для повышенной приватности. Эта функция требует запущенного сервиса Tor на вашей машине.

### Использование Tor-прокси

Добавьте параметр `proxy=True` к любому вызову API:

```python
# Генерация текста с Tor-прокси
response = client.completion.create(messages, proxy=True)

# Генерация изображения с Tor-прокси
client.diffusion.create(prompt, path="./output/image.jpg", proxy=True)
```

### Утилиты Tor

```python
from nexum.utils.webtor import Interfice_Tor

# Установка Tor, если не установлен
# Interfice_Tor.install_tor()

# Получение нового IP-адреса Tor
Interfice_Tor.new_ip()

# Проверка вашего текущего IP-адреса Tor
current_ip = Interfice_Tor.check_ip()
print(current_ip)

# Полный пример с использованием Tor
Interfice_Tor.new_ip()
nexus = Client()

messages = [{'role': 'user', 'content': 'Привет!'}]
print(nexus.completion.create(messages, model_check=True, model=2, proxy=True))
print(nexus.diffusion.create('cute anime cat', proxy=True))
```

## Расширенное использование

### Многоходовые разговоры

```python
from nexum import Client

client = Client()

messages = [
    {"role": "user", "content": "Привет, можешь помочь мне с задачей по Python?"},
    {"role": "ai", "content": "Конечно! Буду рад помочь с вашей задачей по Python. Над чем вы работаете?"},
    {"role": "user", "content": "Как отсортировать словарь по значению в Python?"}
]

response = client.completion.create(messages)
print(response)

# Добавление ответа для продолжения разговора
messages.append({"role": "ai", "content": response})
messages.append({"role": "user", "content": "Можешь показать еще один пример?"})

response = client.completion.create(messages)
print(response)
```

### Проверка доступных моделей

```python
from nexum.system.completions.utils.models import Models

models = Models()
all_models = models.get_models()

# Вывод всех доступных моделей
for provider, provider_models in all_models.items():
    print(f"\nМодели {provider}:")
    for model in provider_models:
        print(f"  - {model['model_name']} (ID: {model['model_id']})")
        if model['description']:
            print(f"    Описание: {model['description']}")
```

## Устранение неполадок

### Распространенные проблемы

1. **Ошибки подключения**
   - Убедитесь, что ваше интернет-соединение стабильно
   - При использовании Tor проверьте, что сервис Tor запущен на вашей машине

2. **Модель не найдена**
   - Перепроверьте ID или название модели
   - Используйте класс `Models` для получения списка доступных моделей

3. **Сбой при генерации изображения**
   - Убедитесь, что директория для сохранения изображений существует или используйте `os.makedirs()` для её создания
   - Попробуйте другую модель или более простой промпт

### Получение помощи

Если вы столкнулись с проблемами, не описанными в этой документации, пожалуйста:
- Проверьте обновленную документацию
- Поищите похожие проблемы в репозитории проекта
- Отправьте подробный отчет о баге с вашим кодом и сообщениями об ошибках

## Справочник API

### Client

```python
Client()
```

**Свойства:**
- `completion`: Доступ к API для генерации текста
- `diffusion`: Доступ к API для генерации изображений

### Completion

```python
client.completion.create(messages, model=1, model_check=False, proxy=False)
```

**Параметры:**
- `messages`: Список словарей сообщений с ключами 'role' и 'content'
- `model`: ID модели (int) или название (str), по умолчанию 1 (Gemini-2.0-F-Thinking)
- `model_check`: Включать ли информацию о модели в ответ, по умолчанию False
- `proxy`: Использовать ли Tor-прокси, по умолчанию False

**Возвращает:**
- Сгенерированный текстовый ответ в виде строки

### Diffusion

```python
client.diffusion.create(prompt, path='./media/image.jpg', settings=None, model=1, proxy=False)
```

**Параметры:**
- `prompt`: Текстовый промпт для генерации изображения
- `path`: Путь выходного файла, по умолчанию './media/image.jpg'
- `settings`: Опциональный объект Settings для настраиваемых моделей
- `model`: ID модели (int) или название (str), по умолчанию 1 (flux-2)
- `proxy`: Использовать ли Tor-прокси, по умолчанию False

**Возвращает:**
- Булево значение, указывающее на успех или неудачу

### Settings

```python
Settings(model=2)
```

**Методы:**
- `negative_prompt(prompt)`: Установка негативного промпта
- `set_seed(seed)`: Установка сида генератора (int или 'random')
- `set_resolution(res=(height, width))`: Установка выходного разрешения
- `set_steps(steps)`: Установка шагов вывода

**Свойство:**
- `setting`: Получение текущего словаря настроек
