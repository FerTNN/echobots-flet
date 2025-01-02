import flet as ft
import json
import os
from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class Bot:
    name: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    raw_data: Dict[str, Any] = None

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'Bot':
        bot_info = data.get('Бот', {})
        if isinstance(bot_info, dict):
            # На всякий случай проверка link
            image_url = bot_info.get('link')
            if image_url and not image_url.startswith(('http://', 'https://')):
                image_url = None 
                
            return cls(
                name=bot_info.get('text', 'Unknown'),
                image_url=image_url,
                description=bot_info.get('text'),
                status=data.get('Статус'),
                raw_data=data
            )
        return cls(
            name=str(bot_info),
            description=str(bot_info),
            status=data.get('Статус'),
            raw_data=data
        )

class BotCatalog:
    def __init__(self, page: ft.Page):
        
        self.page = page
        self.page.title = "Каталог ботов"
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.page.padding = 20
        self.bots = []
        self.filtered_bots = []
        
        # Тема
        def change_theme(e):
            page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
            page.update()
            e.control.selected = not e.control.selected
            e.control.update()
        theme = ft.IconButton(
            icon=ft.Icons.SUNNY,
            selected_icon=ft.Icons.WB_SUNNY_OUTLINED,
            on_click=change_theme,
            selected=False,
            tooltip='Сменить тему')
        
        # Поле поиска        
        search = ft.TextField(
            label="Поиск ботов",
            prefix_icon=ft.Icons.SEARCH,
            on_change=self.filter_bots,
            expand=False)
        self.search_field = search
        self.search_theme = ft.Row([search, theme])
        
        # Сетка для отображения ботов
        self.grid_view = ft.GridView(
            expand=True,
            runs_count=3,
            max_extent=300,
            spacing=20,
            run_spacing=20,
            padding=20
        )
        
        # Компоновка элементов
        self.page.add(
            self.search_theme,
            self.grid_view
        )
        
        # Загрузка данных
        self.load_data()

    def load_data(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'main.json')
            print(f"Загрузка данных из файла: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            self.bots = [Bot.from_json(item) for item in data]
            self.filtered_bots = self.bots.copy()
            self.update_grid()
            # Уведомление о загрузке ботов
            snack = ft.SnackBar(content=ft.Text(f"Успешно загружено {len(self.bots)} ботов"), show_close_icon=True)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()
        # Обработка ошибки
        except Exception as ex:
            print(f"Ошибка при загрузке файла: {ex}")
            snack = ft.SnackBar(content=ft.Text(f"Ошибка при загрузке файла: {str(ex)}"), show_close_icon=True)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()

    # Фильтр через поиск
    def filter_bots(self, e):
        query = self.search_field.value.lower()
        self.filtered_bots = [
            bot for bot in self.bots
            if query in bot.name.lower() or
               (bot.description and query in bot.description.lower())
        ]
        self.update_grid()

    # Создание карточки бота
    def create_bot_card(self, bot: Bot) -> ft.Card:
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Container(
                            content=ft.Image(
                                src=bot.image_url if bot.image_url else None,
                                fit=ft.ImageFit.CONTAIN,
                                width=300,
                                height=200,
                            ) if bot.image_url else ft.Icon(
                                name=ft.Icons.PERSON,
                                size=64,
                                color=ft.Colors.BLUE_400,
                            ),
                            alignment=ft.alignment.center,
                            height=200,
                        ),
                        ft.Container(
                            content=ft.Text(
                                bot.name,
                                size=16,
                                weight=ft.FontWeight.W_500,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            padding=10,
                        ),
                    ],
                    spacing=0,
                ),
                on_click=lambda e: self.show_bot_details(bot),
            ),
        )

    # Обновление сетки карточек
    def update_grid(self):
        self.grid_view.controls = [
            self.create_bot_card(bot)
            for bot in self.filtered_bots
        ]
        self.page.update()

    # Отрытие карточки
    def show_bot_details(self, bot: Bot):
        details = []
        raw_data = bot.raw_data
        bot.image_url

        # Добавляем поля с возможностью копирования
        for key in ['Нынешний юз', 'Старый юз', 'Айди']:
            value = str(raw_data.get(key, '-'))
            if value not in ['-', '']:
                details.append(
                    ft.Row([
                        ft.Text(f"{key}: {value}", selectable=True),
                        ft.IconButton(
                            ft.Icons.COPY,
                            on_click=lambda e, v=value: self.copy_to_clipboard(v)
                        )
                    ])
                )

        # Остальные поля
        for key in ['Первый запуск', 'Второй запуск', 'Дата смерти', 'Владелец', 'Статус', 'Айди']:
            value = str(raw_data.get(key, '-'))
            details.append(
                ft.Text(
                    f"{key}: {value}",
                    selectable=True
                    )
                )

    # Обработка каналов и сурсов
        for key in ['Каналы Ботов', 'Сурсы']:
            value = str(raw_data.get(key, '-'))
            if "http://" in value or "https://" in value:
                # Кнопка для ссылки
                details.append(
                    ft.TextButton(
                        text=f"{key}",
                        on_click=lambda e, v=value: self.open_link(v)
                    )
                )
            else:
                # Отображаем текст, если ссылки нет
                details.append(ft.Text(f"{key}: {value}", selectable=True))
        
        # Кд
        cooldown = raw_data.get('Кд', None)
        if cooldown:
            details.append(ft.Text("Кд:", weight=ft.FontWeight.BOLD))

            if isinstance(cooldown, dict):  # Если Кд содержит текст и другие данные
                text = cooldown.get('text', None)
                link = cooldown.get('link', None)
                # Отображение текста
                if text:
                    details.append(ft.Text(text, selectable=True))
                # Отображение изображения
                if link:
                    details.append(
                        ft.Container(
                            content=ft.Image(
                                src=link,
                                fit=ft.ImageFit.CONTAIN,
                                width=400,
                                height=500,
                            ),
                            alignment=ft.alignment.center,
                        )
                    )
            else:  # Если Кд — это просто строка
                details.append(ft.Text(cooldown, selectable=True))                

        # Обработка примечаний
        notes = raw_data.get('Примечания', None)
        if notes:
            details.append(ft.Text("Примечания:", weight=ft.FontWeight.BOLD))

            if isinstance(notes, dict):  # Если примечания содержат текст и другие данные
                text = notes.get('text', None)
                link = notes.get('link', None)
                # Отображение текста
                if text:
                    details.append(ft.Text(text, selectable=True))
                # Отображение изображения
                if link and (link.startswith('http://') or link.startswith('https://')):
                    details.append(
                        ft.Image(src=link)
                    )
            else:  # Если примечания — это просто строка
                details.append(ft.Text(notes, selectable=True))
                details.append(ft.Text('Картинки нет', selectable=True, color=ft.Colors.RED_400))
        
        # ALertDialog для отображения
        dialog = ft.AlertDialog(
            title=ft.Text(bot.name),
            content=ft.Column(details, scroll=ft.ScrollMode.AUTO),
            actions=[
                ft.TextButton("Закрыть", on_click=lambda e: self.close_dialog(dialog))
            ],
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()

    # Копирование
    def copy_to_clipboard(self, text):
        self.page.set_clipboard(text)
        snack = ft.SnackBar(content=ft.Text("Скопировано в буфер обмена"), show_close_icon=True)
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    # Закрыть AlertDialog
    def close_dialog(self, dialog):
        dialog.open = False
        self.page.update()
        
    # Открытие ссылки
    def open_link(self, url):
        os.system(f"start {url}")  
        snack = ft.SnackBar(content=ft.Text("Открытие ссылки"))
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

def main(page: ft.Page):
    BotCatalog(page)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)