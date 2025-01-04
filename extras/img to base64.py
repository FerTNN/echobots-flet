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
    for key, value in entry.items():
        if isinstance(value, dict) and "image_path" in value:
            image_path = value["image_path"].strip()
            if Path(image_path).exists():
                with open(image_path, "rb") as img_file:
                    base64_string = base64.b64encode(img_file.read()).decode("utf-8")
                    value["base64_image"] = base64_string
            else:
                value["base64_image"] = None
                print(image_path)

# Сохранение данных обратно в JSON
output_file_path = "extras/main copy.json"
with open(output_file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print(f"Файл сохранен с Base64: {output_file_path}")
