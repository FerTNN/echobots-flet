import flet as ft
import json
import os
import pyperclip

# Функция для загрузки данных из JSON-файла
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        print(f"Загрузка данных из файла: {file_path}")
        return json.load(file)

# Функция для копирования текста в буфер обмена
def copy_to_clipboard(text):
    pyperclip.copy(text)
    print(f"Скопировано в буфер обмена: {text}")

# Функция для создания карточки
def create_card(item, page):
    def on_click(e):
        print(f"Открыта карточка: {item.get('Бот', {}).get('text', '-') if isinstance(item.get('Бот'), dict) else item.get('Бот')}")
        # Создаем содержимое для детального просмотра
        details = []

        def add_copyable_field(label, value):
            if value not in ['-', '']:
                details.append(
                    ft.Row([
                        ft.Text(f"{label}: {value}", selectable=True),
                        ft.IconButton(ft.Icons.COPY, on_click=lambda e: copy_to_clipboard(value))
                    ])
                )
            else:
                details.append(ft.Text(f"{label}: {value}", selectable=True))

        add_copyable_field("Нынешний юз", item.get('Нынешний юз', '-'))
        add_copyable_field("Старый юз", item.get('Старый юз', '-'))
        add_copyable_field("Айди", item.get('Айди', '-'))

        details.extend([
            ft.Text(f"Первый запуск: {item.get('Первый запуск', '-')}", selectable=True),
            ft.Text(f"Второй запуск: {item.get('Второй запуск', '-')}", selectable=True),
            ft.Text(f"Дата смерти: {item.get('Дата смерти', '-')}", selectable=True),
            ft.Text(f"Владелец: {item.get('Владелец', '-')}", selectable=True),
            ft.Text(f"Статус: {item.get('Статус', '-')}", selectable=True),
        ])

        # Обрабатываем КД
        kd = item.get('Кд', '-')
        if isinstance(kd, dict):
            kd_text = kd.get('text', '-')
            kd_image = kd.get('image_path')
            kd_link = kd.get('link')
            details.append(ft.Text(f"Кд: {kd_text}", selectable=True))
            if kd_image and os.path.exists(kd_image):
                print(f"Добавление изображения КД: {kd_image}")
                details.append(ft.Image(src=kd_image, width=300, height=300))
            if kd_link:
                print(f"Добавление ссылки КД: {kd_link}")
                details.append(ft.TextButton("Открыть КД", on_click=lambda e, link=kd_link: (print(f"Открытие ссылки: {link}"), page.launch_url(link, web_popup_window=True))))

        # Обрабатываем ссылки для 'Каналы Ботов' и 'Сурсы'
        for key, button_label in [('Каналы Ботов', "Канал бота"), ('Сурсы', "Сурс")]:
            field = item.get(key)
            if isinstance(field, dict):
                link = field.get('link', '-')
                text = field.get('text', '-')
                if link and link not in ['-', '?', '', 'Cвои', 'Нету информации', 'Нету информации.']:
                    print(f"Добавление ссылки для {button_label}: {link}")
                    details.append(ft.TextButton(button_label, on_click=lambda e, lnk=link: (print(f"Открытие ссылки: {lnk}"), page.launch_url(lnk, web_popup_window=True))))
                else:
                    print(f"Добавление текста для {button_label}: {text}")
                    details.append(ft.Text(f"{button_label}: {text}", selectable=True))
            else:
                if field and field not in ['-', '', '?', 'Свои', 'Нету информации', 'Нету информации.']:
                    print(f"Добавление ссылки для {button_label}: {field}")
                    details.append(ft.TextButton(button_label, on_click=lambda e, lnk=field: (print(f"Открытие ссылки: {lnk}"), page.launch_url(lnk, web_popup_window=True))))
                else:
                    print(f"Добавление текста для {button_label}: {field}")
                    details.append(ft.Text(f"{button_label}: {field}", selectable=True))

        # Обрабатываем примечания
        notes = item.get('Примечания', '-')
        if isinstance(notes, dict):
            notes_text = notes.get('text', '-')
            notes_image = notes.get('image_path')
            details.append(ft.Text(f"Примечания: {notes_text}", selectable=True))
            if notes_image and os.path.exists(notes_image):
                print(f"Добавление изображения из примечаний: {notes_image}")
                details.append(ft.Image(src=notes_image, width=300, height=300))
        else:
            details.append(ft.Text(f"Примечания: {notes}", selectable=True))

        # Показываем детальное окно
        dialog = ft.AlertDialog(
            title=ft.Text(item['Бот'].get('text', '-') if isinstance(item['Бот'], dict) else item['Бот']),
            content=ft.Column(details, scroll='adaptive'),
        )
        print("Диалог открыт")
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    # Проверяем наличие аватарки
    bot_info = item.get('Бот', {})
    if isinstance(bot_info, dict):
        image_path = bot_info.get('image_path')
        avatar = ft.CircleAvatar(
            content=ft.Image(src=image_path, fit='contain') if image_path and os.path.exists(image_path) else ft.Icon(ft.Icons.PERSON),
            width=50,
            height=50,
        )
        title = bot_info.get('text', '-')
    else:
        # Если поле "Бот" содержит строку
        avatar = ft.CircleAvatar(
            content=ft.Icon(ft.Icons.PERSON),
            width=50,
            height=50,
        )
        title = bot_info

    # Создаем карточку
    return ft.Card(
        content=ft.ListTile(
            leading=avatar,
            title=ft.Text(title),
            on_click=on_click
        )
    )

# Главная функция приложения
def main(page: ft.Page):
    page.title = "Bot Cards"
    page.scroll = "adaptive"

    # Загрузка данных
    data = load_data(r"echobots1\storage\data\output\main.json")

    # Создание карточек
    cards = [create_card(item, page) for item in data]

    # Добавление карточек на страницу
    print("Добавление карточек на страницу")
    page.add(ft.Column(cards, spacing=10))

ft.app(target=main)
