import json

# Загрузка данных из файла
with open('main.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Преобразование данных
for item in data:
    if isinstance(item.get("Бот"), str):  # Если значение "Бот" - строка
        item["Бот"] = {
            "text": item["Бот"],
            "link": "",
            "image_path": ""
        }

# Сохранение результата в новый файл
with open('updated_main.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Преобразование завершено. Результат сохранён в 'updated_main.json'.")
