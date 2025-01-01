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
            # Здесь можно добавить логику для замены локальных путей на веб-ссылки
            image_url = bot_info.get('link')
            if image_url and not image_url.startswith(('http://', 'https://')):
                image_url = None  # Игнорируем локальные пути
                
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
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        self.bots = []
        self.filtered_bots = []
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
        
        # Поле поиска с исправленной иконкой
        self.search_field = ft.Row([
            ft.TextField(
            label="Поиск ботов",
            prefix_icon=ft.Icons.SEARCH,
            on_change=self.filter_bots,
            expand=False), theme])
        
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
            self.search_field,
            self.grid_view
        )
        
        # Загружаем данные при инициализации
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
            
            # Обновленное уведомление
            snack = ft.SnackBar(content=ft.Text(f"Успешно загружено {len(self.bots)} ботов"))
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()
            
        except Exception as ex:
            print(f"Ошибка при загрузке файла: {ex}")
            snack = ft.SnackBar(content=ft.Text(f"Ошибка при загрузке файла: {str(ex)}"))
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()

    def filter_bots(self, e):
        query = self.search_field.value.lower()
        self.filtered_bots = [
            bot for bot in self.bots
            if query in bot.name.lower() or
               (bot.description and query in bot.description.lower())
        ]
        self.update_grid()

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

    def update_grid(self):
        self.grid_view.controls = [
            self.create_bot_card(bot)
            for bot in self.filtered_bots
        ]
        self.page.update()

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

        # Добавляем остальные поля
        for key in ['Первый запуск', 'Второй запуск', 'Дата смерти', 'Владелец', 'Статус', 'Айди']:
            value = str(raw_data.get(key, '-'))
            details.append(
                ft.Text(
                    f"{key}: {value}",
                    selectable=True
                    )
                )

    # Обрабатываем специальные поля 'Каналы Ботов' и 'Сурсы'
        for key in ['Каналы Ботов', 'Сурсы']:
            value = str(raw_data.get(key, '-'))
            if "http://" in value or "https://" in value:
                # Создаем кнопку для ссылки
                details.append(
                    ft.TextButton(
                        text=f"{key}",
                        on_click=lambda e, v=value: self.open_link(v)
                    )
                )
            else:
                # Отображаем текст, если ссылки нет
                details.append(ft.Text(f"{key}: {value}", selectable=True))

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
        
        # Создаем и показываем диалог
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

    def copy_to_clipboard(self, text):
        self.page.set_clipboard(text)
        snack = ft.SnackBar(content=ft.Text("Скопировано в буфер обмена"))
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def close_dialog(self, dialog):
        dialog.open = False
        self.page.update()
        
    def open_link(self, url):
        os.system(f"start {url}")  # Открывает ссылку в браузере
        snack = ft.SnackBar(content=ft.Text("Ссылка открыта в браузере"))
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

def main(page: ft.Page):
    BotCatalog(page)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)