import json
import base64
from pathlib import Path

# Путь к файлу JSON
json_file_path = "extras/main.json"

# Загрузка данных из JSON
with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Преобразование изображений в Base64
for entry in data:
    bot_info = entry.get("Бот")
    # Проверяем, является ли bot_info словарём
    if isinstance(bot_info, dict):
        image_path = bot_info.get("image_path")
        
        if image_path and Path(image_path.strip()).exists():
            with open(image_path.strip(), "rb") as img_file:
                base64_string = base64.b64encode(img_file.read()).decode("utf-8")
                bot_info["base64_image"] = base64_string
        else:
            bot_info["base64_image"] = None
    else:
        entry["base64_image"] = None  # Добавляем поле для записей, где "Бот" не является словарём

# Сохранение данных обратно в JSON
output_file_path = "extras/main copy.json"
with open(output_file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Файл сохранен с Base64: {output_file_path}")
