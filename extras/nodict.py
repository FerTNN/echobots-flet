import json

# Загрузка данных из файла
with open('main.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Преобразование данных
result = []
for item in data:
    if isinstance(item.get("Бот"), dict):
        text = item["Бот"].get("text", "")
        link = item["Бот"].get("link", "")
        image_path = item["Бот"].get("image_path", "")
        result.append({"text": text, "link": link, "image_path": image_path})

# Сохранение результата в новый файл
with open('transformed_data.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print("Преобразование завершено. Результат сохранён в 'transformed_data.json'.")
