# 🐾 ЛапаДапамога

**ЛапаДапамога** — это платформа для объединения волонтёров и организаторов добрых дел. Проект создан для упрощения взаимодействия между теми, кто нуждается в помощи, и теми, кто готов помочь.

---

## 🌸 О проекте

Платформа предоставляет:

- 🧑‍🤝‍🧑 регистрацию волонтёров и организаторов (с выбором роли);
- 📋 создание и редактирование волонтёрских проектов (для организаторов);
- 🤝 возможность присоединяться к проектам (для волонтёров);
- 👤 личный кабинет с редактированием профиля и отображением своих проектов;
- 🔐 авторизацию через логин/пароль и Telegram.

---

## ⚙️ Технологии

- Python 3.13  
- Django 5.2  
- SQLite (в dev-режиме)  
- Bootstrap 5  
- Telegram Login Widget  
- Git, GitHub

---

## 🚀 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/KulekKonfet/lapadapamoga.git
cd lapadapamoga
```

2. Создайте виртуальное окружение и активируйте:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции и запустите сервер:
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Демонстрация

- Главная: http://127.0.0.1:8000/
- Проекты: http://127.0.0.1:8000/projects/
- Регистрация: http://127.0.0.1:8000/signup/
- Вход: http://127.0.0.1:8000/login/
- Telegram-вход: http://127.0.0.1:8000/telegram-login/

---

## 📝 Автор

**Татьяна Андрушкевич**  
📧 [tanush.snytko@gmail.com](mailto:tanush.snytko@gmail.com)  
📞 +375 33 366-63-39  
🔗 [GitHub: @KulekKonfet](https://github.com/KulekKonfet)

---

## ❤️ Благодарности

Спасибо всем волонтёрам, вдохновившим на создание этой платформы!

---


# Запуск Telegram-бота
python manage.py runbot
