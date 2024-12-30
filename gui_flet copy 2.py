import flet as ft
import json
import os

# Функция для загрузки данных из JSON-файла
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        print(f"Загрузка данных из файла: {file_path}")
        return json.load(file)

# Функция для создания карточки
def create_card(item, page):
    def on_click(e):
        print(f"Клик по карточке: {item.get('Бот', {}).get('text', '-') if isinstance(item.get('Бот'), dict) else item.get('Бот')}")
        # Создаем содержимое для детального просмотра
        details = [
            ft.Text(f"Нынешний юз: {item.get('Нынешний юз', '-')}", selectable=True),
            ft.Text(f"Первый запуск: {item.get('Первый запуск', '-')}", selectable=True),
            ft.Text(f"Второй запуск: {item.get('Второй запуск', '-')}", selectable=True),
            ft.Text(f"Старый юз: {item.get('Старый юз', '-')}", selectable=True),
            ft.Text(f"Кд: {item.get('Кд', '-')}", selectable=True),
            ft.Text(f"Дата смерти: {item.get('Дата смерти', '-')}", selectable=True),
            ft.Text(f"Владелец: {item.get('Владелец', '-')}", selectable=True),
            ft.Text(f"Статус: {item.get('Статус', '-')}", selectable=True),
            ft.Text(f"Айди: {item.get('Айди', '-')}", selectable=True),
        ]

        # Добавляем ссылки
        for key in ['Каналы Ботов', 'Сурсы']:
            link = item.get(key)
            if link:
                print(f"Добавление кнопки для ссылки: {link}")
                details.append(ft.TextButton(key, on_click=lambda e: (print(f"Открытие ссылки: {link}"), page.launch_url(link))))

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
        dialog_one = ft.AlertDialog(
            title=ft.Text(item['Бот'].get('text', '-') if isinstance(item['Бот'], dict) else item['Бот']),
            content=ft.Column(details, scroll='adaptive'),
            actions=[ft.TextButton("Закрыть", on_click=lambda e: (print("Диалог закрыт"), setattr(page, 'dialog', None)))]
        )
        page.overlay.append(dialog_one)
        page.update()

    # Проверяем наличие аватарки
    bot_info = item.get('Бот', {})
    if isinstance(bot_info, dict):
        image_path = bot_info.get('image_path')
        avatar = ft.Image(src=image_path, fit='contain') if image_path and os.path.exists(image_path) else ft.Icon(ft.icons.PERSON, size=50)
        title = bot_info.get('text', '-')
    else:
        # Если поле "Бот" содержит строку
        avatar = ft.Icon(ft.icons.PERSON, size=50)
        title = bot_info

    # Создаем карточку с увеличенным размером
    return ft.Container(
        content=ft.Column([
            ft.Container(content=avatar, alignment=ft.alignment.center),
            ft.Text(title, weight="bold", size=18, text_align="center"),
        ], alignment="center"),
        padding=10,
        on_click=on_click,
        height=150,
        width=200,
        border_radius=ft.border_radius.all(8),
        bgcolor=ft.colors.SURFACE,
    )

# Главная функция приложения
def main(page: ft.Page):
    page.title = "Bot Cards"
    page.scroll = "adaptive"

    # Загрузка данных
    data = load_data(r"output\main.json")

    # Создание карточек
    cards = [create_card(item, page) for item in data]

    # Добавление карточек на страницу
    print("Добавление карточек на страницу")
    page.add(ft.ResponsiveRow([ft.Container(content=card) for card in cards], spacing=10))


ft.app(target=main)
